'''
   utility for qsst python framework

   This module used to provide utilities for qsst python framework,
   support low level operations as initial socket connection, generate
   command line to communicate with server, interact with server and
   so on.

   you can use all the interface in qsst python framework, but not for
   cases. If you want to add some common function utils for framework ,
   you can also added them here.


   @author: U{zhibinw<zhibinw@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:
'''

from exception import SocketException,AssertFailedException
import sys
import os
import time
import subprocess
import signal
import thread
import fs_wrapper
import inspect
import settings.common as SC
from logging_wrapper import *
from platform_check import get_platform_info

from thrift_gen_uiautomator.QSST import Uiautomator_Thrift_Interface
from thrift_gen_qsstservice.QSST import QSST_Thrift_Interface
from thrift_gen_mytrackserver.MyTrack import LocalMyTrackInterface
from thrift_gen_qsstservice.GroupTest import GroupTestMEService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from threading import local
from tls_thriftclient_bean import ThriftClient

'''tags used for request'''
SEPERATOR = "&sp;"
ACTION_tag = "action="
DEST_VIEW_TYPE_tag = "dest_view_type="
DEST_VIEW_ID_TYPE_tag = "dest_view_id_type="
DEST_VIEW_ID_tag = "dest_view_id="
VALUE_tag = "value="
LENGTH_tag = "len="

ACTION_END = '0'

'''tags used for response'''
STATUS_END = '-1'
STATUS_ACTION_NOT_SUPPORT = '0'
STATUS_OK_WITHOUT_RESULT = '1'
STATUS_OK_WITH_RESULT = '2'
STATUS_ASSERT_FAILED = '3'

SPACE = ' '
LOG_tag = 'utility_wrapper'
API_INFO_TAG = 'API_INFO'

#current client that's being used
port_uiautomator = 7702
port_qsst = 7701
localport_mytrackservice = 7703
port_grouptest_meserver = 3000
localport_grouptest_meserver = 7000
transport_grouptest = None
protocol_grouptest = None
client_grouptest = None

tls_thriftClient = None
#if assert failes during one case or not, why used this ?
current_case_continue_flag = True

def assert_type_string(i):
    '''
    check whether the input parameter  is a string.
    set L{current_case_continue_flag<current_case_continue_flag>}
    to false if fails.

    @type i: string
    @param i: the parameter to be checked.

    @todo: should raise an exception, not set flag.
    '''
    if not type(i) in [type(''), type(u'')]:
        log_test_framework(LOG_TAG, "parameter invalid")
        current_case_continue_flag = False

def assert_type_int(i):
    '''
    check whether the input parameter is an integer.
    set L{current_case_continue_flag<current_case_continue_flag>}
    to false if fails.

    @type i: int
    @param i: the parameter to be checked.

    @todo: should raise an exception, not set flag.
    '''
    if not type(i) in [type(0)]:
        log_test_framework(LOG_TAG, "parameter invalid")
        current_case_continue_flag = False

#given inputs, generate a cmd string
#note that all inputs are strings, except for value_list, it is a list
def generate_cmd(action, dest_view_type, dest_view_id_type, dest_view_id, value_list):
    '''
    generate a command line request for uiautomator server to perform an ui detection or operation. Lots of operations in L{case utility<case_utility>} used this api to generate requests, which can be your reference.

    @type action:int
    @param action: which action you want to perform.
    @type dest_view_type: int
    @param dest_view_type: the view's type you want to operate.
    @type dest_view_id_type: int
    @param dest_view_id_type: the id type you want to identify your view,which may be resource id,text,index,desc and so on, refer L{case_utility<case_utility>}
    @type value_list:list
    @param value_list: all other values, refer L{case_utility<case_utility>}.

    '''
    cmd_string = ACTION_TAG + action
    if len(dest_view_type) > 0:
        temp = SEPERATOR + DEST_VIEW_TYPE_TAG + dest_view_type
        cmd_string += temp
    if len(dest_view_id_type) > 0:
        temp = SEPERATOR + DEST_VIEW_ID_TYPE_TAG + dest_view_id_type
        cmd_string += temp
    if len(dest_view_id) > 0:
        temp = SEPERATOR + DEST_VIEW_ID_TAG + dest_view_id
        cmd_string += temp
    if len(value_list) > 0:
        for value in value_list:
            if len(value) > 0:
                temp = SEPERATOR + VALUE_TAG + value
                cmd_string += temp
    temp = LENGTH_TAG + str(len(cmd_string)) + SEPERATOR
    cmd_string = temp + cmd_string
    return cmd_string

def end_test_runners_accessibility():
    '''
    stop the uiautomator server to end
    the current test, it will close client socket at the same time.
    '''
    from case_utility import send_value_to_qsst,BOOL_TRUE,SEND_END_CASE
    #send value to let qsst service know that test run over. Consider that user use "adb shell python .." to run QSST.
    send_value_to_qsst(SEND_END_CASE,BOOL_TRUE)

    log_test_framework(LOG_TAG, "end test runner")
    kill_by_name('uiautomator')

def close_thriftclient():

    thriftClient = get_tls_thrift_client()
    thriftClient.transport_qsst.close()
    thriftClient.transport_uiautomator.close()
    global transport_grouptest
    transport_grouptest.close()

def can_continue():
    '''
    return L{current_case_continue_flag<current_case_continue_flag>}

    @todo: should not use this, enhance to exceptions.
    '''
    global current_case_continue_flag
    return current_case_continue_flag

def set_cannot_continue():
    '''
    set L{current_case_continue_flag<current_case_continue_flag>} to False.
    This global flag used to judge if test can continue or not.

    @todo:should not use this ,enhance to exceptions.
    '''
    global current_case_continue_flag
    current_case_continue_flag = False

def set_can_continue():
    '''
    set L{current_case_continue_flag<current_case_continue_flag>} to True.

    @todo:should not use this, enhance to exceptions.
    '''
    global current_case_continue_flag
    current_case_continue_flag = True

def kill_by_name(pro_name):
    '''
    kill a process by given it's process name.

    @type pro_name: string
    @param pro_name: process name.
    @return: none
    '''
    os_info = get_platform_info()
    ps_cmd = None
    if os_info == "Linux-Phone":
        ps_cmd = ['ps']
    else:
        ps_cmd = ['adb', 'shell', 'ps']
    p = subprocess.Popen(ps_cmd,stdout=subprocess.PIPE)
    out = p.communicate()[0]
    for line in out.splitlines():
        if pro_name in line:
            pid = int(line.split()[1])
            if os_info == "Linux-Phone":
                os.kill(pid,signal.SIGKILL)
            else:
                subprocess.call(['adb', 'shell', 'kill', str(pid)])

def Host_Start_Uiautomator():
    print("before launch uiautomator")
    if(SC.PUBLIC_ENABLE_USER_RELEASE_ONLINE_DEBUG == False):
        os.system('adb shell uiautomator translatecases &')
    if(SC.PUBLIC_ENABLE_USER_RELEASE_ONLINE_DEBUG == True):
        os.system('adb shell su -c uiautomator translatecases &')

def init_acessibility_socket():
    '''
    Initialize server side socket, it will start up uiautomator socket.
    If used on PC , it will use also used adb forward  tcp:6100 to remote uiautomator
    socket running on device.
    '''
    kill_by_name('uiautomator')
    osInfo = get_platform_info()
    if(osInfo == "Windows" or osInfo == "Linux-PC"):
        if(SC.PUBLIC_ENABLE_USER_RELEASE_ONLINE_DEBUG == False):
            os.system('adb shell am startservice -n com.android.qrdtest/.QsstService')
            qsst_forward_cmd = 'adb forward tcp:'+str(port_qsst)+' tcp:'+str(port_qsst)
            os.system(qsst_forward_cmd)
            os.system('adb shell am startservice -n com.android/.MyTrackService')
            mytrackservice_forward_cmd = 'adb forward tcp:'+str(localport_mytrackservice)+' tcp:'+str(localport_mytrackservice)
            os.system(mytrackservice_forward_cmd)
        if(SC.PUBLIC_ENABLE_USER_RELEASE_ONLINE_DEBUG == True):
            os.system('adb shell su -c am startservice -n com.android.qrdtest/.QsstService')
            qsst_forward_cmd = 'adb forward tcp:'+str(port_qsst)+' tcp:'+str(port_qsst)
            os.system(qsst_forward_cmd)
            os.system('adb shell su -c am startservice -n com.android/.MyTrackService')
            mytrackservice_forward_cmd = 'adb forward tcp:'+str(localport_mytrackservice)+' tcp:'+str(localport_mytrackservice)
            os.system(mytrackservice_forward_cmd)

        #subprocess.Popen(["adb", "shell", "uiautomator translatecases &"],stdout=subprocess.PIPE)
        thread.start_new_thread(Host_Start_Uiautomator, ())
        uiautomator_forward_cmd = 'adb forward tcp:'+str(port_uiautomator)+' tcp:'+str(port_uiautomator)
        os.system(uiautomator_forward_cmd)
        forwardCmd = 'adb forward tcp:'+str(localport_grouptest_meserver)+' tcp:'+str(port_grouptest_meserver)
        print forwardCmd
        os.system(forwardCmd)
        #subprocess.Popen(cmd)
        pass
    elif(osInfo == "Linux-Phone"):
        os.system('am startservice -n com.android.qrdtest/.QsstService')
        os.system('uiautomator translatecases &')
        os.system('am startservice -n com.android/.MyTrackService')
    time.sleep(10)
    if not init_thrift_client():
        return False
    return True

#use thread local storage to storage thrift qsst client and thrift uiautomator client in each thread
#so in each thread can interact with qsst server and uiautomator server by owner clients.
def init_tls_thrift_client():
    global tls_thriftClient
    tls_thriftClient= local()
    tls_thriftClient.thriftClient = ThriftClient()

def set_tls_thrift_client(thriftClient):
    tls_thriftClient.thriftClient = thriftClient

def get_tls_thrift_client():
    return tls_thriftClient.thriftClient

def init_thrift_client():
    try:
      transport_qsst = TSocket.TSocket('localhost', port_qsst)
      # Buffering is critical. Raw sockets are very slow
      transport_qsst = TTransport.TBufferedTransport(transport_qsst)
      # Wrap in a protocol
      protocol_qsst = TBinaryProtocol.TBinaryProtocol(transport_qsst)
      # Create a client to use the protocol encoder
      transport_qsst.open()

      #set thrift qsst client
      thriftClient = ThriftClient()
      thriftClient.transport_qsst = transport_qsst
      thriftClient.protocol_qsst = protocol_qsst
      thriftClient.client_qsst = QSST_Thrift_Interface.Client(protocol_qsst)

      transport_uiautomator = TSocket.TSocket('localhost', port_uiautomator)
      # Buffering is critical. Raw sockets are very slow
      transport_uiautomator = TTransport.TBufferedTransport(transport_uiautomator)
      # Wrap in a protocol
      protocol_uiautomator = TBinaryProtocol.TBinaryProtocol(transport_uiautomator)
      # Create a client to use the protocol encoder
      transport_uiautomator.open()

      global transport_grouptest
      global protocol_grouptest
      global client_grouptest
      osInfo = get_platform_info()
      if(osInfo == "Windows" or osInfo == "Linux-PC"):
        transport_grouptest = TSocket.TSocket('localhost', localport_grouptest_meserver)
      elif(osInfo == "Linux-Phone"):
        transport_grouptest = TSocket.TSocket('localhost', port_grouptest_meserver)
      transport_grouptest = TTransport.TBufferedTransport(transport_grouptest)
      protocol_grouptest = TBinaryProtocol.TBinaryProtocol(transport_grouptest)
      client_grouptest = GroupTestMEService.Client(protocol_grouptest)
      print str(client_grouptest)
      transport_grouptest.open()

      #set thrift uiautomator client
      thriftClient.transport_uiautomator = transport_uiautomator
      thriftClient.protocol_uiautomator = protocol_uiautomator
      thriftClient.client_uiautomator = Uiautomator_Thrift_Interface.Client(protocol_uiautomator)

      #set thrift mytrackservice client
      transport_mytrackservice = TSocket.TSocket('localhost', localport_mytrackservice)
      transport_mytrackservice = TTransport.TBufferedTransport(transport_mytrackservice)
      protocol_mytrackservice = TBinaryProtocol.TBinaryProtocol(transport_mytrackservice)
      transport_mytrackservice.open()

      thriftClient.transport_mytrackservice = transport_mytrackservice
      thriftClient.protocol_mytrackservice = protocol_mytrackservice
      thriftClient.client_mytrackservice = LocalMyTrackInterface.Client(protocol_mytrackservice)

      set_tls_thrift_client(thriftClient)

      return True
    except Thrift.TException, tx:
      log_test_framework(LOG_TAG, 'exception'+ str(tx._get_message))
      return False

def wakeUpSignalHandler(a,b):
    '''
    wake up handler for sleep, not used currently.
    '''
    log_test_framework(LOG_TAG, "device wakes up");


def OnshakeSignal_handler(a, b):
    log_test_framework(LOG_TAG, "get device shake java to python signal,--- 1")


def getprop_suspend():
    os_info = get_platform_info()
    ps_cmd = None
    if os_info == "Linux-Phone":
        ps_cmd = ['getprop','python.process.suspend']
    else:
        ps_cmd = ['adb', 'shell', 'getprop','python.process.suspend']
    p = subprocess.Popen(ps_cmd,stdout=subprocess.PIPE)
    out = p.communicate()[0]
    for line in out.splitlines():
        if 'true' in line:
            log_test_framework(LOG_TAG, "suspend_flag = true, ---2 getprop");
            return True
    log_test_framework(LOG_TAG, "suspend_flag = false, ---2  getprop");
    return False

def kpi_path():
    '''
    This function used to save the log on the path. Weight and Data also on the path.
    @return: kpi_path
    '''
    osInfo = get_platform_info()
    kpi_path = sys.path[0] + os.sep + 'kpi'+os.sep
    return kpi_path

def kpi_log_value(category,casename,value):
    '''
    This function used to load-in data.
    @type category: string
    @param category: Category name,such as "launch-time","fps"
    @type casename: string
    @param casename:Test case name,such as "camera_001","browser"
    @type value: int
    @param value: such as 1000,200
    @return: kpi_log_value(category,casename,value)
    '''
    path = log_path()
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        log = open(path + 'kpi_log.Qsst', 'ab')
    except Exception:
        print "utility.py kpi_log_value() log.txt lose"
    log.write("#" + category + ":" + casename + ":" + str(value)+ "\n")
    log.close()

def InvokeFuncByCurRunTarget(context, location,test_case,diff_api):
    '''
    This function used to get phone software version number.
    @type location: string
    @param location: platform file location.
    @type test_case:
    @param test_case:Test_case_name & adaptive.
    @type diff_api: string
    @param diff_api: replace api
    @return: replace api
    '''
    import settings.common as SC
    platform_choose =''
    for i in os.listdir(location +'/platform/'):
        if i == SC.PUBLIC_PHONE_PLATFORM_TYPE:
            platform_choose = i
    try:
        if platform_choose !='':
            platform_version = SC.PUBLIC_PHONE_PLATFORM_TYPE
        else:
            platform_version = "default"
        module_meta = __import__(location+".platform."+platform_version+"."+test_case, globals(), locals(),diff_api)
        fun_meta = getattr(module_meta, diff_api)
        result = fun_meta(context)
        if result == False:
            return False
        else:
            return True
    except Exception as e:
            log_test_framework(LOG_TAG,"Error :" + str(e))
            return False

def deal_remote_exception(ex):
    current_case_continue_flag = False
    log_test_framework(LOG_TAG, 'exception: '+str(ex))
    raise AssertFailedException(ex)


def DisableTouchPanel(test_env_xxx):
    print ('path is ' + test_env_xxx )
    if get_platform_info()=="Linux-Phone":
        os.system('sh /data/disableTouchPanel.sh '+test_env_xxx+' &')
    print ('disable Touch Panel')

def enableTouchPanel():
    print('enable Touch Panel')
    if get_platform_info()=="Linux-Phone":
        os.system('sh /data/EnableTouchPanel.sh &')

def notify_monitor_service_change():
    '''
    Notify Qsst Server to auto monitor service change, only run in Phone and items are not null.
    '''
    from case_utility import send_value_to_qsst,SEND_ITEMS_AUTO_MONITOR_SERVICE_CHANGE,BOOL_TRUE,BOOL_FALSE,SEND_FLAG_AUTO_MONITOR_SERVICE_CHANGE,SEND_TEST_ENV_DIR,SEND_LOG_ROOT
    import settings.common as SC
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        send_value_to_qsst(SEND_ITEMS_AUTO_MONITOR_SERVICE_CHANGE,SC.PUBLIC_SERVICE_CHANGE_ITEMS_FOR_AUTO_MONITOR)
        if(SC.PUBLIC_SERVICE_CHANGE_ITEMS_FOR_AUTO_MONITOR != ''):
            test_env = TEST_ENV_DIR[TEST_ENV_DIR.rfind('/')+1:]
            send_value_to_qsst(SEND_TEST_ENV_DIR,test_env)
            send_value_to_qsst(SEND_LOG_ROOT,get_log_root())
            send_value_to_qsst(SEND_FLAG_AUTO_MONITOR_SERVICE_CHANGE,BOOL_TRUE)
        else:
            send_value_to_qsst(SEND_FLAG_AUTO_MONITOR_SERVICE_CHANGE,BOOL_FALSE)

def api_log_decorator(function):
    '''
    A decorator function used to output api log info.
    How-to : Add @api_log_decorator just above the api function.
    '''
    def _api_log_decorator(*args, **kwargs):
        func_name = function.__name__
        inp_args = inspect.getargspec(function)
        params = inp_args[0]
        defaults = inp_args[3]
        log_str = ""

        params_dict = dict(enumerate(params))
        for p_key in params_dict.keys():
            params_dict[p_key] = {params_dict[p_key]:""}

        # deal with defaults value of the function
        if defaults:
            p_idx = len(params_dict) - len(defaults)
            for d_value in defaults:
                for k, v in params_dict[p_idx].items():
                    params_dict[p_idx][k] = d_value
                p_idx += 1

        # deal with args value of the params
        for a_idx in xrange(0, len(args)):
            for k,v in params_dict[a_idx].items():
                params_dict[a_idx][k] = args[a_idx]

        #deal with kwargs value of the params
        for k_key in kwargs.keys():
            for p_value in params_dict.values():
                if k_key in p_value:
                    p_value[k_key] = kwargs[k_key]

        # get log_info string
        log_str += "API: " + func_name
        if not params_dict:
            log_str += " Param: no params"
        for s_key, s_value in params_dict.iteritems():
            log_str += " Param[" + str(s_key+1) + "]:"
            for key, value in s_value.iteritems():
                if not value and isinstance(value, (str, unicode)):
                    log_str += str(key) + "=" + '""'
                else:
                    log_str += str(key) + "=" + str(value)

        log_test_framework(API_INFO_TAG, log_str)

        ret= function(*args, **kwargs)
        return ret
    return _api_log_decorator

def get_dict_from_results(results_str):
    info_dict = {}
    results_list = results_str.split(" ")
    for value in results_list:
        idx_list = value.split(":")
        info_dict[idx_list[0]] = idx_list[1]
    return info_dict