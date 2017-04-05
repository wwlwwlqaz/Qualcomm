#coding=utf-8
'''
   logging wrapper for qsst python framework

   This module is integrated the qsst logging frameword,
   support low level loggin operations as init the logging file,
   init suit logging , init case logging, record the logging to the file ,
   record the context information and so on .

   1.The api provided is used to write the log message to the different
   log file by the format.

   2.This module also provide to recording the suit name , case name ,
   and the count of total case ,the count of failed case and so on .
   you can use it by the get/set methods.

   3.If you want to add some common functions for the logging ,
   you an add here

   @author: U{c_lqiang<c_lqiang@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{test_case_base<test_case_base>}
   @see: L{test_suit_base<test_suit_base>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import time
import os
import sys
import subprocess
import shutil
from platform_check import get_platform_info
import fileinput
import threading
#from locale import str

TEST_ENV_DIR = sys.path[0]
'''used to save the autotest enviroment directory'''
DBG_CONSOLE = True
'''whether the logging need to print to the console'''
cur_suit_name=''
'''save the current suit name'''
cur_case_name=''
'''save the current case name'''
#save the context info
context_info = ''
'''save the context information'''
ignore_status = False
'''ignore the status of the case. if true,
the qsst_log_case_init() and qsst_log_case_status() will transform to the normal logging'''

SEVERITY_HIGH = 0
SEVERITY_CRITICAL = 1
SEVERITY_MEDIUM = 2
SEVERITY_LOW = 3

DIVIDE=":"
'''tag for separate the each prefix tags'''

'''prefix for logging '''

PREFIX_SUIT = "SUIT"
'''prefeix tag for suit'''
PREFIX_CASE = "CASE"
'''prefeix tag for case'''
PREFIX_DESC = "DESC"
'''prefeix tag for description'''
PREFIX_SEVERITY = "SEVERITY"
'''prefeix tag for serverity'''
PREFIX_STATUS = "STATUS"
'''prefeix tag for status'''
PREFIX_RESULT = "RESULT"
'''prefeix tag for result'''
PREFIX_START_TIME = "STARTTIME"
'''prefeix tag for starttime'''
PREFIX_END_TIME = "ENDTIME"
'''prefeix tag for endtime'''
PREFIX_MSG = "MSG"
'''prefeix tag for noemal message'''
PREFIX_RANDOM = "RANDOM"
'''prefix to indicate random case list'''
PREFIX_INTERACTIVE = "INTERACTIVE"
'''prefix to indicate interactive case list'''
PREFIX_UNINTERACTIVE = "UNINTERACTIVE"
'''prefix to indicate uninteractive case list'''
PREFIX_DESCRIPTION = "DESCRIPTION"
'''prefeix tag for case description'''
'''prefix for status '''
PREFIX_LOGGING_PATH = "LOGGING_PATH"
PREFIX_CURRENT_TIME = "CURRENT_TIME"
PREFIX_LOG_ROOT = "LOG_ROOT"
PREFIX_REBOOT = "REBOOT"
PREFIX_REPEAT_TIME = "REPEAT_TIME"
PREFIX_TEST_ENV_XXX = "TEST_ENV_XXX"
TOTAL_CASE = "TOTAL_CASE"
FAILED_CASE = "FAILED_CASE"
UNSUPPORTED_CASE = "UNSUPPORTED_CASE"
SUCCESS_CASE = "SUCCESS_CASE"
SERVICE_START_TIME = "SERVICE_START_TIME"
SERVICE_END_TIME = "SERVICE_END_TIME"

REBOOT_MANUAL = "MANUAL"
REBOOT_CRASH = "CRASH"

STATUS_SUCCESS = 0
'''tag for success'''
STATUS_FAILED = 1
'''tag for failed'''
STATUS_UNSUPPORTED = 2
'''tag for unsupported'''
STATUS_UNKNOWN = -1
'''tag for unknown'''

total_case = 0
'''total case in current suit'''
failed_case = 0
'''failed case in current suit'''
unsupported_case = 0
'''unsupported case in current suit'''

DATA_CRASH_DIR = "/data/data/com.android.qrdtest/crash/"
DATA_STATUS_DIR = "/data/data/com.android.qrdtest/status/"
DATA_MONITOR_STATUS_PATH = "/data/data/com.android.qrdtest/auto_monitor.qsst"

AUTO_LOGGING_ENV_CONTEXT_TYPE_DISABLE = "disable"
AUTO_LOGGING_ENV_CONTEXT_TYPE_CASE_END = "case_end"
AUTO_LOGGING_ENV_CONTEXT_TYPE_CASE_FAIL = "case_fail"
'''The type of env context info'''

LOG_TAG = "logging_wrapper"
log_root = ""

log_path_on_server_side = ""
init_qxdm_success = False

def init_logging_file(currentTime=1,repeatTime=1,test_env_xxx='/data/test_env'):
    '''
    ini the logging file which is saved the all python logs
    '''
    global python_log_path
    global osInfo
    global log_root
    global logging_filepath
    global status_path
    global python_log_name

    if log_root==None or log_root=="":
        osInfo = get_platform_info()
        if(osInfo == 'Linux-Phone'):
            import settings.common as SC
            log_root = SC.PUBLIC_LOG_PATH + '/'
            s = test_env_xxx.strip('/')[5:]
            __write_status(PREFIX_TEST_ENV_XXX + DIVIDE + s)
        elif(osInfo == 'Linux-PC' or osInfo == 'Windows'):
            os.system('adb root')
            global TEST_ENV_DIR
            log_root = TEST_ENV_DIR + os.sep + 'com.android.qrdtest'+os.sep
        if is_in_reboot_status():
            log_root = get_last_log_root()
            root_list = log_root.split('/')
            python_log_name = root_list[len(root_list)-2]
        else:
            python_log_name = get_file_timestring()
            log_root = log_root + python_log_name + os.sep
    log_status = log_root + os.sep + "log_status.qsst"
    if int(currentTime) == 1:
        __write_log(PREFIX_REPEAT_TIME + DIVIDE + str(repeatTime), log_status)
        __write_log(SERVICE_START_TIME + DIVIDE + get_file_timestring(), log_status)
    #if the repeat time is not 1. will create the child dir include the current time to save the log
    if int(repeatTime) > 1:
        logging_filepath = log_root + os.sep + str(currentTime)+ os.sep
        __write_log(PREFIX_LOGGING_PATH + DIVIDE + str(currentTime), log_status)
        __write_log("SUITS_START_TIME" + DIVIDE +get_file_timestring(), logging_filepath+ "log_status_"+str(currentTime)+".qsst")
    else:
        logging_filepath = log_root
        __write_log(PREFIX_LOGGING_PATH + DIVIDE + ".", log_status)
    python_log_path = logging_filepath + 'python.log'
    if not is_in_reboot_status():
        try:
            if not os.path.exists(logging_filepath):
                os.makedirs(logging_filepath)
        except OSError, why:
            print "Faild: %s " % str(why)
    #write the log path to status
    __write_status(PREFIX_LOG_ROOT+DIVIDE+log_root)
    __write_status(PREFIX_LOGGING_PATH+DIVIDE+logging_filepath)
    __write_status(PREFIX_CURRENT_TIME+DIVIDE+str(currentTime))
    chmod(status_path)

def qsst_log_suit_init():
    '''
    ini the logging file for the suit.and save the suit beginning information to the report logging file which suffix is "qsst"
    Notice: this logging file is different with the "python.log". this logging file is under each suit directory
    '''
    global qsst_log_path
    qsst_log_dir = logging_filepath+os.sep+cur_suit_name+os.sep
    if not os.path.exists(qsst_log_dir):
        os.makedirs(qsst_log_dir)
    qsst_log_path = qsst_log_dir+cur_suit_name+".qsst"
    if not is_suit_in_reboot_status(cur_suit_name):
        __write_log(PREFIX_SUIT+DIVIDE+cur_suit_name, qsst_log_path)
        __write_log(PREFIX_START_TIME+DIVIDE+get_timestring(), qsst_log_path)
        #write suit starting to status file
        __write_status(PREFIX_SUIT+DIVIDE+cur_suit_name)
    else:
        log_test_suit(cur_suit_name, "this suit is in the reboot status, so need not to init it")

def qsst_log_case_init():
    '''
    ini the logging file for the case.and save the case beginning information to the report logging file which suffix is "qsst"
    '''
    global qsst_log_path
    global total_case
    global ignore_status
    if ignore_status:
        qsst_log_msg("ignore init "+cur_case_name)
    elif is_case_in_reboot_status(cur_case_name):
        qsst_log_msg("reboot init "+cur_case_name)
    else:
        #total_case = total_case+1
        update_case_count(TOTAL_CASE, 1)
        __write_log(PREFIX_CASE+DIVIDE+cur_suit_name+DIVIDE+cur_case_name, qsst_log_path)
        #write case starting to status file
        __write_status(PREFIX_CASE+DIVIDE+cur_suit_name+DIVIDE+cur_case_name)
        from fs_wrapper import get_test_case_config,SUIT_DESCRIPTION
        case_config_map = get_test_case_config(cur_case_name, cur_suit_name)
        if case_config_map.has_key(SUIT_DESCRIPTION):
            __write_log(PREFIX_DESCRIPTION+DIVIDE+case_config_map.get(SUIT_DESCRIPTION), qsst_log_path)

def qsst_log_msg(msg):
    '''
    save a normal logging message to the report logging file.

    @type msg:string
    @param msg: logging message
    '''
    __write_log(PREFIX_MSG+DIVIDE+str(msg), qsst_log_path)

def qsst_log_case_status(status,desc,severity):
    '''
    save the current case status.

    @type status:int
    @param status: this status of the current cases. the values will be:
        L{STATUS_SUCCESS<STATUS_SUCCESS>},
        L{STATUS_FAILED<STATUS_FAILED>},
        L{STATUS_UNSUPPORTED<STATUS_UNSUPPORTED>},
        L{STATUS_UNKNOWN<STATUS_UNKNOWN>}.

    @type desc:String
    @param desc: the description of status, it will be the reason of this status
    @type severity:int
    @param severity: the severity of this case .the values will be:
        L{SEVERITY_HIGH<SEVERITY_HIGH>},
        L{SEVERITY_CRITICAL<SEVERITY_CRITICAL>},
        L{SEVERITY_MEDIUM<SEVERITY_MEDIUM>},
        L{SEVERITY_LOW<SEVERITY_LOW>}.
    '''
    global failed_case
    global ignore_status
    str_severity = __convert_severity(severity)
    str_status = __convert_status(status)
    __auto_log_env_context_info(status)
    if ignore_status:
        qsst_log_msg(PREFIX_SEVERITY+DIVIDE+str_severity)
        qsst_log_msg(PREFIX_STATUS+DIVIDE+str_status+DIVIDE+desc)
    else:
        if STATUS_FAILED == status:
            #failed_case = failed_case +1
            update_case_count(FAILED_CASE, 1)
        __write_log(PREFIX_SEVERITY+DIVIDE+str_severity, qsst_log_path)
        __write_log(PREFIX_STATUS+DIVIDE+str_status+DIVIDE+desc, qsst_log_path)

def __auto_log_env_context_info(status):
    '''
    auto log env context info with the status.

    @type status: int
    @param status: this status of the current cases. the values will be:
        L{STATUS_SUCCESS<STATUS_SUCCESS>},
        L{STATUS_FAILED<STATUS_FAILED>},
        L{STATUS_UNSUPPORTED<STATUS_UNSUPPORTED>},
        L{STATUS_UNKNOWN<STATUS_UNKNOWN>}.
    '''
    import settings.common as SC
    #config level: env_context_type is disable
    try:
        if SC.PUBLIC_AUTO_LOGGING_ENV_CONTEXT == AUTO_LOGGING_ENV_CONTEXT_TYPE_DISABLE:
            from fs_wrapper import get_test_case_config,CASE_AUTO_LOGGING_ENV_CONTEXT_ATTR,CASE_ITEMS_FOR_AUTO_LOGGING_ATTR
            case_config_map = get_test_case_config(cur_case_name, cur_suit_name)
            case_env_context_type = case_config_map.get(CASE_AUTO_LOGGING_ENV_CONTEXT_ATTR)
            case_env_context_items = case_config_map.get(CASE_ITEMS_FOR_AUTO_LOGGING_ATTR)
            if case_env_context_type == None:
                return
            elif case_env_context_type == AUTO_LOGGING_ENV_CONTEXT_TYPE_CASE_END:
                __write_log_env_context_info(case_env_context_items)
            elif case_env_context_type == AUTO_LOGGING_ENV_CONTEXT_TYPE_CASE_FAIL:
                if STATUS_FAILED == status:
                    __write_log_env_context_info(case_env_context_items)
            else:
                return
        #config level: env_context_type is case_end
        elif SC.PUBLIC_AUTO_LOGGING_ENV_CONTEXT == AUTO_LOGGING_ENV_CONTEXT_TYPE_CASE_END:
            __write_log_env_context_info(SC.PUBLIC_ENV_CONTEXT_ITEMS_FOR_AUTO_LOGGING)
        #config level: env_context_type is case_fail
        elif SC.PUBLIC_AUTO_LOGGING_ENV_CONTEXT == AUTO_LOGGING_ENV_CONTEXT_TYPE_CASE_FAIL:
            if STATUS_FAILED == status:
                __write_log_env_context_info(SC.PUBLIC_ENV_CONTEXT_ITEMS_FOR_AUTO_LOGGING)
    except AttributeError , why:
        log_test_framework(LOG_TAG, "write env context info failed:" + str(why))
        return

def qsst_log_suit_end():
    '''
    end the suit. and save the end information to the report file .
    '''
    global total_case
    global failed_case
    global unsupported_case
    __write_log(PREFIX_END_TIME+DIVIDE+get_timestring(), qsst_log_path)
    __write_log(PREFIX_RESULT+DIVIDE+str(total_case)+DIVIDE+str(total_case-failed_case-unsupported_case)+DIVIDE+str(failed_case)+DIVIDE+str(unsupported_case), qsst_log_path)
    #reset the count
    total_case = 0
    failed_case = 0
    unsupported_case = 0

def qsst_log_reboot_manual():
    qsst_log_msg(PREFIX_REBOOT+DIVIDE+REBOOT_MANUAL)
    __write_status(PREFIX_REBOOT+DIVIDE+REBOOT_MANUAL)

def qsst_log_reboot_crash(last_log_path, last_suit_name,reboot_reason):
    log_path = last_log_path+os.sep+last_suit_name+os.sep+last_suit_name+".qsst"
    line = PREFIX_REBOOT+DIVIDE+reboot_reason
    __write_log(PREFIX_MSG+DIVIDE+line, log_path)

    # we think default case status is fail, if this case carshed the phone.
    # we can set the default case status as FAILED_CASE, UNSUPPORTED_CASE or SUCCESS_CASE
    default_reboot_case_status = FAILED_CASE
    if default_reboot_case_status == FAILED_CASE:
        update_case_count(FAILED_CASE, 1)
        __write_log(PREFIX_SEVERITY+DIVIDE+__convert_severity(SEVERITY_HIGH), log_path)
        __write_log(PREFIX_STATUS+DIVIDE+__convert_status(STATUS_FAILED)+DIVIDE+"This case crash the phone.", log_path)
    elif default_reboot_case_status == UNSUPPORTED_CASE:
        update_case_count(UNSUPPORTED_CASE, 1)
        __write_log(PREFIX_SEVERITY+DIVIDE+__convert_severity(SEVERITY_HIGH), log_path)
        __write_log(PREFIX_STATUS+DIVIDE+__convert_status(STATUS_UNSUPPORTED)+DIVIDE+"Unsupported case.", log_path)

def qsst_log_restore_reboot():
    global last_log_root
    #last log path
    global last_log_path
    global last_suit_name
    global last_case_name
    global is_reboot_status
    global last_current_time

    last_log_root =""
    last_log_path =""
    last_suit_name=""
    last_case_name=""
    is_reboot_status = False
    last_current_time = 1
    global reboot_reason
    reboot_reason=""
    global random_case_list
    random_case_list=[]
    global interactive_case_list
    interactive_case_list=[]
    global uninteractive_case_list
    uninteractive_case_list=[]

def set_context_info(msg):
    '''
    save the context information to L{context_info<context_info>}.it is help developer to understand where the test is running.

    @type msg: string
    @param msg: context information.
    '''
    global context_info
    context_info = msg

def get_context_info():
    '''
    get the context information.

    @return: the context information
    '''
    global context_info
    return context_info

def set_ignore_status(ignore):
    '''
    set L{ignore_status<ignore_status>}.

    @type ignore: boolean
    @param ignore: if true, the qsst_log_case_init() and
    qsst_log_case_status() will transform to the normal logging.
    default values is False
    '''
    global ignore_status
    ignore_status = ignore

def move_crash():
    '''
    move the crash files to the logging dir.
    Notice: only run the autotest on the phone, can listen the foreclose/anr
    '''
    if os.path.exists(DATA_CRASH_DIR):
        #copy to the loggin path
        shutil.copytree(DATA_CRASH_DIR,logging_filepath+os.sep+"crash")
        clear_crash()

def clear_crash():
    '''
    rm the crash files in the data
    '''
    __clear_dir(DATA_CRASH_DIR)

def __write_status(line):
    global status_path
    #if the environment is not the android phone , can not create the status file
    if(osInfo == 'Linux-Phone'):
        __write_log(line, status_path)

def __write_log(line,log_file):
#    if not os.path.exists(log_file):
#        return False
    try:
        logDir, logName = os.path.split(log_file)
        if not os.path.exists(logDir):
            os.makedirs(logDir)
        fp = open(log_file,'a+')
        fp.write(str(line) + '\n')
        fp.close()
    except OSError:
        print "write logging failed: %s " % str(log_file)

def __convert_severity(severity):
    if SEVERITY_CRITICAL == severity:
        return "CRITICAL"
    elif SEVERITY_HIGH == severity:
        return "HIGH"
    elif SEVERITY_MEDIUM == severity:
        return "HIGH"
    else:
        return "LOW"

def __convert_status(status):
    if STATUS_UNSUPPORTED == status:
        return "UNSUPPORTED"
    elif STATUS_FAILED == status:
        return "FAILED"
    elif STATUS_SUCCESS == status:
        return "SUCCESS"
    else:
        return "UNKNOWN"

def create_python_log_rlock():
    '''
        RLock apply to writting python.log.
        Foreground case and background case will concurrent write the python.log
    '''
    global python_log_rlock
    python_log_rlock = threading.RLock()

def print_log_line(line):
    '''
    save a line logging message to the log file

    @type line: String
    @param line: the logging message
    '''
    if (DBG_CONSOLE):
        print(line)
    python_log_rlock.acquire()
    __write_log(get_timestring()+line + '\n', python_log_path)
    python_log_rlock.release()

#logging function for test suit
def log_test_suit(suit_name, msg):
    '''
    print a normal logging which is in the suit

    @type suit_name: String
    @param suit_name: suit name
    @type msg: String
    @param msg: the logging you want to print or save
    '''
    print_log_line('suit ' + suit_name + ' : ' + msg)

#logging function for test case
def log_test_case(case_name, msg):
    '''
    print a normal logging which is in the case

    @type case_name: String
    @param case_name: case name
    @type msg: String
    @param msg: the logging you want to print or save
    '''
    print_log_line('\tcase ' + case_name + ' : ' + msg)
    qsst_log_msg(msg)

def print_log(case_name, msg):
    '''
    print a normal logging which is in the case

    @type case_name: String
    @param case_name: case name
    @type msg: String
    @param msg: the logging you want to print or save
    '''
    print_log_line('\tcase ' + case_name + ' : ' + str(msg))

#logging function for the test framework
def log_test_framework(tag, msg):
    '''
    print a normal logging which is in the qsst ptyhon framework

    @type tag: String
    @param tag: tag to indentify where are you
    @type msg: String
    @param msg: the logging you want to print or save
    '''
    print_log_line('\t\tframework ' + tag + ' : ' + msg)

#take screenshot
def take_screenshot():
    '''take a screenshot and save to log/suit_name/case_name/'''
    make_case_log_dir()
    global osInfo
    if(osInfo == 'Linux-Phone'):
        cmd = 'screencap -p ' + get_case_logging_path() + get_file_timestring() + '.jpg'
        run_cmd(cmd)
    elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
        import settings.common as SC
        run_cmd(' mkdir ' + SC.PUBLIC_LOG_PATH)
        temp_file= ' ' + SC.PUBLIC_LOG_PATH + '/temp.jpg '
        cmd= 'screencap -p ' + temp_file
        run_cmd(cmd)
        cmd= 'adb pull '+temp_file + get_case_logging_path() + get_file_timestring() + '.jpg'
        os.system(cmd)

def print_report_line(line):
    '''
    print a normal logging message

    @type line: String
    @param line: the logging you want to print or save
    '''
    print_log_line('\t\trepost ' +  line)

#TODO this can move to utility
def get_file_timestring():
    '''
    get a time string which is using for the file, which format is like: %Y-%m-%d-%H_%M_%S

    @return: the time string
    '''
    time_string = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    return time_string

def get_timestring_log_name():
    '''
    get the file name of python log which use time string.

    @return: the file name of python log
    '''
    global python_log_name
    return python_log_name

def get_timestring():
    '''
    get a time string, which format is like: %Y-%m-%d %H:%M:%S

    @return: the time string
    '''
    time_string = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return time_string

def set_cur_case_name(case_name):
    '''
    set the value of L{cur_case_name<cur_case_name>}.
    @type case_name: String
    @param case_name: the current case name
    '''
    global cur_case_name
    cur_case_name = case_name

    from case_utility import send_value_to_qsst,SEND_CASE_NAME
    send_value_to_qsst(SEND_CASE_NAME,cur_case_name)

def get_cur_case_name():
    '''
    get the value of L{cur_case_name<cur_case_name>}.
    @return: the current case name
    '''
    global cur_case_name
    return cur_case_name

def set_cur_suit_name(suit_name):
    '''
    set the value of L{cur_suit_name<cur_suit_name>}.
    @type suit_name: String
    @param suit_name: the current suit name
    '''
    global cur_suit_name
    cur_suit_name = suit_name

    from case_utility import send_value_to_qsst,SEND_SUIT_NAME
    send_value_to_qsst(SEND_SUIT_NAME,cur_suit_name)

def get_cur_suit_name():
    '''
    get the value of L{cur_suit_name<cur_suit_name>}.
    @return: the current suit name
    '''
    global cur_suit_name
    return cur_suit_name

def get_case_logging_path():
    '''
    get the case logging path
    @return: case logging path
    '''
    return logging_filepath + cur_suit_name + os.sep + cur_case_name + os.sep
#    global osInfo
#    if(osInfo == 'Linux-Phone'):
#        return logging_filepath + cur_suit_name + '/' + cur_case_name + '/'
#    elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
#        return logging_filepath + cur_suit_name + '\\' + cur_case_name + '\\'


def make_case_log_dir():
    '''
    create the case log directory if it is not exist.
    '''
    try:
        if not os.path.exists(get_case_logging_path()):
            os.makedirs(get_case_logging_path())
    except OSError, why:
        print "Faild: %s " % str(why)

def do_logcat_capture():
    '''
    catch the logcat.
    '''
    make_case_log_dir()

    logcat_path = get_case_logging_path() + get_file_timestring() + '.logcat'
    cmd = 'logcat -d  -v time > ' + logcat_path
    log_test_framework('logging_wrapper','save log : ' + cmd)
    run_cmd(cmd)

def clear_logcat():
    '''
    clear the logcat.
    '''
    cmd = 'logcat -c '
    run_cmd(cmd)

def run_cmd(cmd):
    '''
    run a command
    '''
    #args = cmd.split(' ')
    global osInfo
    if(osInfo == 'Linux-Phone'):
        #subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        os.system(cmd)
    elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
        cmd='adb shell '+cmd
        #subprocess.Popen(['adb','shell',cmd],stdout=subprocess.PIPE)
        os.system(cmd)
def save_fail_log():
    '''
    save the log if the case failed. it will take the screenshot and catch the logcat
    '''
    take_screenshot()
    do_logcat_capture()

def is_in_reboot_status():
    '''
    is in the reboot status .
    @return: if true , it means, current is in the reboot status.
    '''
    global is_reboot_status
    return is_reboot_status

def get_logging_filepath():
    '''
    get  L{logging_filepath<logging_filepath>}.
    @return: return the value  L{logging_filepath<logging_filepath>}.
    '''
    global logging_filepath
    return logging_filepath

def get_last_log_path():
    '''
    get the last logging path before reboot.
    @return: return the logging path before reboot
    '''
    #last log path
    global last_log_path
    if is_in_reboot_status():
        return last_log_path
    else:
        return None

def get_last_log_root():
    '''
    get the last logging root
    @return: return the last logging root
    '''
    #last log path
    global last_log_root
    if is_in_reboot_status():
        return last_log_root
    else:
        return None

def get_log_root():
    '''
    get logging root
    @return: return the logging root
    '''
    #last log path
    global log_root
    return log_root

def get_last_current_time():
    global last_current_time
    if is_in_reboot_status():
        return last_current_time
    else:
        return 1

def get_reboot_reason():
    global reboot_reason
    if is_in_reboot_status():
        return reboot_reason
    return ""

def is_suit_in_reboot_status(suit_name):
    '''
    check whether suit is in reboot status.

    @type suit_name: string
    @param suit_name: the current suit name.
    @return: True: reboot status, False:no.

    '''
    global last_suit_name
    if not is_in_reboot_status():
        return False
    if last_suit_name == "":
        return False
    if last_suit_name == suit_name:
        return True
    else:
        return False

def is_case_in_reboot_status(case_name):
    '''
    check whether case is in reboot status.

    @type case_name: string
    @param case_name: the current case name.
    @return: True: reboot status, False:no.

    '''
    global last_case_name
    if not is_in_reboot_status():
        return False
    if last_case_name == "":
        return False
    if last_case_name == case_name:
        return True
    else:
        return False
def init_status():
    '''
    init the status.clear the status fileand add the time line
    Notice: this function need be called firstly
    '''
    global status_path
    global last_log_root
    #last log path
    global last_log_path
    global last_suit_name
    global last_case_name
    global last_current_time
    global is_reboot_status
    global reboot_reason
    global total_case
    global failed_case
    global unsupported_case
    global random_case_list
    global interactive_case_list
    global uninteractive_case_list
    #reset the reboot status
    qsst_log_restore_reboot()
    status_path = DATA_STATUS_DIR+"/status.qsst"
    if os.path.exists(status_path):
        #if the status path is exist. reay the info
        try:
            statusFile = open(status_path)
            lines = statusFile.readlines()
            for line in lines:
                line = line.strip("\n")
                line = line.strip(" ")
                if line == "":
                    continue
                #set the is_reboot_status=False,
                #it is means , only the last line is contain the reboot tag ,
                #it is the really reboot tag
                is_reboot_status = False
                index = line.find(DIVIDE)
                if index >0 and index < len(line):
                    prefix = line[:index]
                    sufix = line[index+1:]
                    if prefix == PREFIX_LOGGING_PATH:
                        #save the last log path
                        last_log_path = sufix
                    elif prefix == PREFIX_LOG_ROOT:
                        last_log_root = sufix
                    elif prefix == PREFIX_CURRENT_TIME:
                        last_current_time = sufix
                    elif prefix == PREFIX_CASE:
                        #read the last suit name , last case name
                        caseIndex = sufix.find(DIVIDE)
                        last_suit_name = sufix[:caseIndex]
                        last_case_name = sufix[caseIndex+1:]
                    elif prefix == PREFIX_REBOOT:
                        is_reboot_status = True
                        #save the reboot reason
                        reboot_reason = sufix
                        #if the crash reason is REBOOT_CRASH, so need to write the reason to the qsst log
                        if reboot_reason.startswith(REBOOT_CRASH ) :
                            qsst_log_reboot_crash(last_log_path, last_suit_name,reboot_reason)

                    elif prefix == TOTAL_CASE:
                        total_case = int(sufix)
                    elif prefix == FAILED_CASE:
                        failed_case = int(sufix)
                    elif prefix == UNSUPPORTED_CASE:
                        unsupported_case = int(sufix)
                    elif prefix==PREFIX_RANDOM:
                        divideIndex = sufix.find(DIVIDE)
                        suit_name=sufix[:divideIndex]
                        case_name=sufix[divideIndex+1:]
                        random_case_list.append((suit_name,case_name))
                    elif prefix ==PREFIX_INTERACTIVE:
                        divideIndex = sufix.find(DIVIDE)
                        suit_name=sufix[:divideIndex]
                        case_name=sufix[divideIndex+1:]
                        interactive_case_list.append((suit_name,case_name))
                    elif prefix ==PREFIX_UNINTERACTIVE:
                        divideIndex = sufix.find(DIVIDE)
                        suit_name=sufix[:divideIndex]
                        case_name=sufix[divideIndex+1:]
                        uninteractive_case_list.append((suit_name,case_name))
            statusFile.close()
        except IOError:
            #here can not use the log_test_framwork . cause this method is before init_log_file
            print ( "open the qsst status file failed.")
    #clear the status file
    #if not in the reboot status , clear it.
    if not is_reboot_status:
        clear_status()
        clear_file(DATA_MONITOR_STATUS_PATH)
        os.makedirs(DATA_STATUS_DIR)
        chmod(DATA_STATUS_DIR)

def clear_status():
    __clear_dir(DATA_STATUS_DIR)

def clear_file(destFile):
    if os.path.exists(destFile):
        os.remove(destFile)

def __clear_dir(destDir):
    if os.path.exists(destDir):
        shutil.rmtree(destDir)

def file_insert(file_name,line_no,content):
    """
    Insert content to one line before end of original file.
    """
    if os.path.exists(file_name):
        origi_line_no = 0

        fp = open(file_name)
        contents = fp.readlines()
        file_len = len(contents)

        for line in fileinput.input(file_name,inplace=1):
            # inplace must be set to 1
            # it will redirect stdout to the input file
            origi_line_no += 1
            line = line.strip()
            if origi_line_no == line_no:
                print content
                print line
            else:
                print line

            if origi_line_no == file_len and file_len < line_no:
                while(True):
                    origi_line_no += 1
                    if(origi_line_no == line_no):
                        print content
                        break
                    else:
                        print '\n'

def log_path():
    global logging_filepath
    path = logging_filepath
    return path

def __write_log_env_context_info(env_context_items):
    '''
    log the env context info in python.log and .qsst

    @type env_context_items: String
    @param env_context_items: the items of auto logging env context info
    '''
    if(env_context_items == ""):
        return ""

    log_test_framework(LOG_TAG, "__write_log_env_context_info:begin logging.")

    #get each functions
    items = env_context_items.split(',')
    for item in items:
        function_name = {
                'postion-mobile':               lambda: 'get_postion',
                'speed-mobile':                 lambda: 'get_speed',
                'temperate-battery-celsius':    lambda: 'get_battery_temperate',
                'temperate-battery-fahrenheit': lambda: 'get_battery_temperate',
                'orientation-mobile':           lambda: 'get_orientation',
                'ram-available':                lambda: 'get_available_ram',
                'rom-available':                lambda: 'get_available_rom',
                'rssi-wifi':                    lambda: 'get_wifi_rssi',
                }[item.replace(" ","")]()
        module_meta = __import__('case_utility', globals(), locals(), [function_name])
        fun_meta = getattr(module_meta, function_name)

        #deal with functions with args
        if item == "temperate-battery-celsius":
            args = '0'
            result = fun_meta(*args)
        elif item == "temperate-battery-fahrenheit":
            args = '1'
            result = fun_meta(*args)
        else:
            result = fun_meta()
        log_test_framework(LOG_TAG, item + ":" + unicode(str(result)))
        qsst_log_msg(item + DIVIDE + unicode(str(result)))
    log_test_framework(LOG_TAG, "__write_log_env_context_info:end logging.")

def chmod(filePath, mode = 777,recursive = True):
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        if recursive:
            os.system('chmod -R '+str(mode)+" "+filePath)
        else:
            os.system('chmod '+str(mode)+" "+filePath)

def __update_status_file_line(type, value):
    osInfo = get_platform_info()
    if not (osInfo == 'Linux-Phone'):
        return
    print type + str(value)
    global status_path
    f = open(status_path, 'r')
    lines = f.readlines()
    newLines = ''
    boo = False
    for line in lines:
         if line.find(type) >= 0:
              line = type + DIVIDE + str(value) + '\n'
              boo = True
         newLines += line
    f.close()

    f = open(status_path, 'w')
    if not boo:
        f.write(type + DIVIDE + str(value) + '\n')
    f.write(newLines)
    f.close()

def update_case_count(type, value):
    global total_case
    global failed_case
    global unsupported_case
    if type == TOTAL_CASE:
        total_case = total_case + value
        __update_status_file_line(type, total_case)
    elif type == FAILED_CASE:
        failed_case = failed_case + value
        __update_status_file_line(type, failed_case)
    elif type == UNSUPPORTED_CASE:
        unsupported_case = unsupported_case + value
        __update_status_file_line(type, unsupported_case)
def save_random_case_list(case_list):
    for case in case_list:
        __write_status(PREFIX_RANDOM+DIVIDE+case[0]+DIVIDE+case[1])
def restore_random_case_list():
    global random_case_list
    return random_case_list

def save_interactive_case_list(case_list):
    for case in case_list:
        __write_status(PREFIX_INTERACTIVE+DIVIDE+case[0]+DIVIDE+case[1])

def restore_interactive_case_list():
    global interactive_case_list
    return interactive_case_list

def save_uninteractive_case_list(case_list):
    for case in case_list:
        __write_status(PREFIX_UNINTERACTIVE+DIVIDE+case[0]+DIVIDE+case[1])

def restore_uninteractive_case_list():
    global uninteractive_case_list
    return uninteractive_case_list

def set_log_path_on_server_side(val):
    global log_path_on_server_side
    log_path_on_server_side = val;

def get_log_path_on_server_side():
    global log_path_on_server_side
    return log_path_on_server_side;

def set_init_qxdm_success(val):
    global init_qxdm_success
    init_qxdm_success = val;

def get_init_qxdm_success():
    global init_qxdm_success
    return init_qxdm_success;