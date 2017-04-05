'''
Control the suits&cases run.

Test_main.py controls the preset cases , test cases.We can use command the test cases random or repeat.
First, it run init_settings(), get preset cases which you choosed.Second,in the init_env(), run the preset cases. Third, in the init_env(), it run the test cases.If you want be random or repeat
the test cases, you can scan in the init_env().

@author: U{zhibinw<zhibinw@qti.qualcomm.com>}
@author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
@author: U{c_ywan<c_ywan@qti.qualcomm.com>}

@version: version 1.0.0
@requires: python 2.7+
@license: license

@see: L{test main<test_main>}
@note: Because SU.update() method will reload in init_env(), so we must import settings.common as SC after invoking  init_env()
'''

import os
import sys
import signal
reload(sys)
sys.setdefaultencoding("utf-8")
if len(sys.argv) >= 2:
    TEST_ENV_DIR = sys.argv[1]#get test_main.py file location
else:
    # get path 'data/test_env_xxx/' from argument 'data/test_env_xxx/test_main.py'
    l = len('test_main.py')
    TEST_ENV_DIR = sys.argv[0][0:-l]
os.chdir(TEST_ENV_DIR)
import settings.update as SU
SU.update()
SU.auto_match_platform()

import fs_wrapper
import traceback
from logging_wrapper import *
from utility_wrapper import end_test_runners_accessibility,init_acessibility_socket, set_can_continue,init_tls_thrift_client,notify_monitor_service_change
from test_loader import TestLoader
from background_case_pool.bg_test_loader import BgTestLoader,BACKGROUND_CASE_POOL
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher
from test_case_base import TestCaseBase
import capacity.capacity as CC

SUIT_PLUG_IN_FUNCTION_NAME = 'suit_plug_in'
TAG='test_main'

def init_env(currentTime=1,global_number=1):
    '''
    Run preset test cases.  Lead data(SU.update()). You must update the data(SU.update()),before you run the preset test case. Because some preset case will use data which in data(SU.update()).
    '''
    init_logging_file(current_number,global_number,TEST_ENV_DIR)
    #clear the last crash dir
    clear_crash()

    '''
    Some jobs just only need be done once and need write log in log files.
    And the log files must be exist firstly.
    So put the jobs here and they only run once when current time is 1 or is in reboot status.
    '''
    #if monitor before crash, then continue to auto monitor service change.
    global is_init_env
    if (current_number == 1 or (is_in_reboot_status() and not is_init_env)):
        if not init_acessibility_socket():
            return

        if SC.PRIVATE_HOSTLOGGING_ENABLE_FEATURE:
            l = len(SC.PUBLIC_LOG_PATH)
            init_server_side_log()
            serial_number = get_serial_number_from_pc()
            log_path = SC.PRIVATE_HOSTLOGGING_LOG_SAVE_PATH + serial_number + logging_wrapper.log_root[l:].replace("/", "\\")
            set_log_path_on_server_side(log_path)
            mkdir_on_server_side(log_path)
            init_qxdm_success = load_configuration(SC.PRIVATE_HOSTLOGGING_QXDM_CONFIGURATION) and comPort(str(SC.PRIVATE_HOSTLOGGING_COM_NUMBER))
            set_init_qxdm_success(init_qxdm_success)
            if not init_qxdm_success:
                log_test_framework(TAG,"Error : init QXDM failed.")
            clear_adb_log()

        re_list = IsPreconditionOk()

        if len(re_list) > 0 :
            print("precondition check failed, the reasons reasons list:")
            for x in re_list:
                print(x)
            if(get_platform_info() == 'Linux-Phone'):
                interact_with_user_by_list("ERROR!!!", "precondition check failed  reasons list", re_list)
            return False

        # init capacity list
        CC.get_capacity_list()

        if int(SC.PUBLIC_RUNNING_REPEAT_NUMBER) == 1:
            send_value_to_qsst(SEND_CYCLE_TIME,'.')
        else:
            send_value_to_qsst(SEND_CYCLE_TIME,currentTime)
        notify_monitor_service_change()

        if not is_in_reboot_status():
            #start to record track
            startSuc = start_new_track(get_timestring_log_name(), "recording " + get_timestring_log_name())
            if not startSuc:
                log_test_framework("test_main","notification:start new track failed!!")
            init_settings()

        else:
            resume_current_track()

        #go_back the STK pop dialog
        #register_condition_action_watcher("com.android.stk", VIEW_BUTTON , ID_TYPE_ID, "button_ok",
        #                        ACTION_GO_BACK,VIEW_BUTTON , ID_TYPE_ID, "button_ok")
        log_test_framework("test_main","stkDialog condition watcher")

        #low battery
        register_condition_action_watcher("com.android.systemui", VIEW_BUTTON , ID_TYPE_ID, "level_percent",
                                ACTION_GO_BACK,VIEW_BUTTON , ID_TYPE_ID, "level_percent" )
        log_test_framework("test_main","low battery watcher")

        is_init_env = True
        #class 0 mms
        #register_condition_action_watcher("com.android.mms", VIEW_BUTTON , ID_TYPE_TEXT, "cancel",
        #                        ACTION_CLICK,VIEW_BUTTON , ID_TYPE_TEXT, "cancel" )
        #log_test_framework("test_main","mms class0 watcher")

        # incomingcall will reject
        #register_app_watcher("incomingcall", VIEW_IMAGE_VIEW , ID_TYPE_ID, "incomingCallWidget", ACTION_LEFT_DRAG )
        #register_condition_action_watcher("phone", VIEW_IMAGE_VIEW , ID_TYPE_ID, "incomingCallWidget",
        #                        ACTION_LEFT_DRAG ,VIEW_IMAGE_VIEW, ID_TYPE_ID, "incomingCallWidget")
        #log_test_framework("test_main","reject incomingCallWidget watcher")

    if int(SC.PUBLIC_RUNNING_REPEAT_NUMBER) == 1:
        send_value_to_qsst(SEND_CYCLE_TIME,'.')
    else:
        send_value_to_qsst(SEND_CYCLE_TIME,currentTime)
    return True

def init_settings():
    '''
    Load preset test cases. Find test suit which in test_suit_setting.After run preset test case, it will tag the suit False. When run the test case , preset case will not run again.
    '''
    global test_loader
    #TODO: use class to call settings suit
    fs_wrapper.run_init_settings = True
    suit_name = "test_suit_settings"
    suit_py_module_name = "settings.test_suit_settings"
    test_suit = test_loader.loadTestSuitFromName(suit_py_module_name, suit_name)
    suit_results = []
    #call main entry function
    if test_suit != None:
        test_suit.test_suit_run(suit_results)
    fs_wrapper.run_init_settings = False

def end_test():
    '''
    Run test cases. Random or repeat test cases. First, lead test suit list. Second,repeat case 1~x x is be defined on Settings config.Third, random test case if you choose on  Settings config.
    '''
    import logging_wrapper

    #end track and export track as KML
    end_current_track_and_export_kml(get_log_root())

    #move the crash to the current log dir
    move_crash()
    clear_status()
    #back to auto test after end
    set_can_continue()
    launcher = Launcher()
    launcher.launch_from_launcher('auto_test')
    end_test_runners_accessibility()
    log_root = logging_wrapper.log_root
    if os.path.exists(log_root):
        log_status = log_root + os.sep + "log_status.qsst"
        logging_wrapper.__write_log(SERVICE_END_TIME + DIVIDE + get_file_timestring(), log_status)

    enableTouchPanel()
    if SC.PRIVATE_HOSTLOGGING_ENABLE_FEATURE:
        quit_qxdm()

def runInteractiveCase():
    #interactive_case_on_the_forward,interactive_case_on_the_last,disable
    if SC.PUBLIC_CHOOSE_INTERACTIVE_CASE_MODE == 'interactive_case_on_the_forward':
        try:
            suit_results = []
            suit = test_loader.loadInteractivityTestSuit()
            suit.test_suit_run(suit_results)
            suit2 = test_loader.loadUnInteractivityTestSuit()
            suit2.test_suit_run(suit_results)
        except Exception as e:
            log_test_framework(TAG,"Error :" + str(e))
            log_test_framework(TAG,"Traceback :" + traceback.format_exc())
    if SC.PUBLIC_CHOOSE_INTERACTIVE_CASE_MODE == 'interactive_case_on_the_last':
        try:
            suit_results = []
            suit2 = test_loader.loadUnInteractivityTestSuit()
            suit2.test_suit_run(suit_results)
            suit = test_loader.loadInteractivityTestSuit()
            suit.test_suit_run(suit_results)
        except Exception as e:
            log_test_framework(TAG,"Error :" + str(e))
            log_test_framework(TAG,"Traceback :" + traceback.format_exc())

def IsPreconditionOk():
    check_filenames = os.listdir('check_precondition')

    result_list = []
    for check_filename in check_filenames :
        if check_filename.find('__init__.py') != -1  or check_filename.find('.pyc') != -1 :
            continue
        check_file = os.path.splitext(check_filename)[0]

        check_module = __import__('check_precondition' + '.' + check_file,
                                  globals(), locals(), ['verify'], -1)
        re_check = check_module.verify()
        if re_check != 'ok':
            log_test_framework(TAG, " check fail " + re_check)
            result_list.append(re_check)
    return result_list

def monitor_stop_event():
    os_info = get_platform_info()
    if os_info == "Linux-Phone":
        signal.signal(signal.SIGUSR2, OnStopSignal_handler)

def OnStopSignal_handler(a, b):
    '''
        something jobs when click stop button to kill python.
    '''
    log_test_framework(TAG, "stop qsst-----")

    #end track and export track as KML
    end_current_track_and_export_kml(get_log_root())

    #record exit time in current suit qsst.
    qsst_log_path = logging_wrapper.qsst_log_path
    if os.path.exists(qsst_log_path):
        logging_wrapper.__write_log(PREFIX_END_TIME + DIVIDE + get_timestring(), qsst_log_path)
    #record exit time in current repeat time qsst.
    if (logging_wrapper.get_logging_filepath()).split(os.sep)[-2].isdigit():
        logging_wrapper.__write_log("SUITS_END_TIME" + DIVIDE +get_file_timestring(), logging_wrapper.get_logging_filepath()+ "log_status_"+str(TestCaseBase.cycle_index)+".qsst")
    #record exit time in log_status.qsst
    log_root = logging_wrapper.log_root
    if os.path.exists(log_root):
        log_status = log_root + os.sep + "log_status.qsst"
        logging_wrapper.__write_log(SERVICE_END_TIME + DIVIDE + get_file_timestring(), log_status)
    #exit
    sys.exit()

if __name__ == '__main__':

    #import settings.common as SC
    import settings.common as SC
    import logging_wrapper

    if SC.PUBLIC_DISABLE_TOUCHPANEL:
        SU.reset_disable_touchpanle_setting()
        print("reset disable touch panle setting false")
        test_env_xxx=TEST_ENV_DIR[TEST_ENV_DIR.index('test_env'):]
        DisableTouchPanel(test_env_xxx)
    else:
        print ('disable setting is false')

    # load all test suits and cases
    global test_loader
    test_loader = TestLoader()
    print ('test_loader')
    bg_test_loader = BgTestLoader()
    print ('test back ground loader')
    global_number = SC.PUBLIC_RUNNING_REPEAT_NUMBER

    #init the status , include to know whether is it in reboot status
    init_status()
    print ('status')
    last_current_time = get_last_current_time()
    init_tls_thrift_client()    
    print ('init thrift')
    create_python_log_rlock()
    is_run_bg_case = False
    global is_init_env
    is_init_env = False
    monitor_stop_event()

    for current_number in range(int(last_current_time),int(global_number)+1):
        TestCaseBase.cycle_index = current_number
        #init the env each report time
        if not init_env(current_number, global_number) :
            log_test_framework(TAG, "failed  init env")
            break
        log_test_framework(TAG, "Current report " + str(current_number) + "/" + str(global_number))
        try:
            #run background cases. only need when run normally or run after reboot at the first circle time.
            if (current_number == 1 or (is_in_reboot_status() and not is_run_bg_case)):
                try:
                    bg_suit_list = bg_test_loader.loadBgTestSuit('./' + BACKGROUND_CASE_POOL + '/')
                    if bg_suit_list != None and len(bg_suit_list.bg_test_cases) > 0:
                        #report suits count
                        log_test_framework(TAG,"All background test cases (" + str(len(bg_suit_list.bg_test_cases)) + ") :")
                        # run all background test cases
                        bg_suit_list.test_suit_run()
                    is_run_bg_case = True
                except Exception as e:
                    log_test_framework(TAG,"Error :" + str(e))
                    log_test_framework(TAG,"Traceback :" + traceback.format_exc())

            #run interactive case
            if SC.PUBLIC_CHOOSE_INTERACTIVE_CASE_MODE == 'disable':
                if SC.PUBLIC_RANDOM_ORDER:
                    try:
                        suit_results = []
                        suit = test_loader.loadRandomTestSuit()
                        suit.test_suit_run(suit_results)
                    except Exception as e:
                        log_test_framework(TAG,"Error :" + str(e))
                        log_test_framework(TAG,"Traceback :" + traceback.format_exc())
                else:
                    suit_list = test_loader.loadTestSuit('./')
                    if suit_list != None and len(suit_list) > 0:
                        #report suits count
                        log_test_framework(TAG,"All test suites (" + str(len(suit_list)) + ") :")
                        # run all test suits
                        suit_results = []
                        for suit in suit_list:
                            log_test_framework(TAG,"Suit : " + suit.name)
                            try:
                                suit.test_suit_run(suit_results)
                            except Exception as e:
                                log_test_framework(TAG,"Error :" + str(e))
                                log_test_framework(TAG,"Traceback :" + traceback.format_exc())
            if SC.PUBLIC_CHOOSE_INTERACTIVE_CASE_MODE == 'interactive_case_on_the_forward' or SC.PUBLIC_CHOOSE_INTERACTIVE_CASE_MODE == 'interactive_case_on_the_last':
                runInteractiveCase()
        except Exception as e:
            log_test_framework(TAG,"Error :" + str(e))
            log_test_framework(TAG,"Traceback :" + traceback.format_exc())

        log_test_framework("test_main","\n all suit finished.")
        if (logging_wrapper.get_logging_filepath()).split(os.sep)[-2].isdigit():
            logging_wrapper.__write_log("SUITS_END_TIME" + DIVIDE +get_file_timestring(), logging_wrapper.get_logging_filepath()+ "log_status_"+str(current_number)+".qsst")
 #   end_test()

