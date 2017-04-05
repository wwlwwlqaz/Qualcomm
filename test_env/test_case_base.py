'''
   Base class of all case.

   This module defines the life cycle of test case .
   and makes the case subclass just need to care about the test functions.

   1.test_case_run() function is the entry which the test suit will call it .
   In this function , it will call test_case_init() to init some information about this case.
   then, test_case_main() function will be called, and subclasses just need to override it,and do itself things.
   last, test_case_end() function will be called, and execute to exit this application.

   2.in addition, exit_app() function is used to exit the application after this case is ending.
   it usually call the launcher.back_to_launcher() to exit.
   of course, subclass also can override it and complete itself steps to exit the application.

   3.If you want to add some common function for all the test case ,
   you can add them here.

   @author: U{c_lqiang<c_lqiang@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{test_suit_base<test_suit_base>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import signal
import fs_wrapper
import traceback
from utility_wrapper import set_can_continue, getprop_suspend, OnshakeSignal_handler , enableTouchPanel
from logging_wrapper import *
from qrd_shared.launcher.Launcher import Launcher
import logging_wrapper
import case_utility
import capacity.capacity as CC
import settings.common as SC

CASE_RUN_SELF=111
CASE_BE_REFERED=222
CASE_BE_CALLED=333

class TestCaseBase(object):
    """Base class for test case"""
    global launcher
    '''cycle index of repeat case'''
    cycle_index = 1
    '''record server side adb pid'''
    global adb_main_log_pid
    adb_main_log_pid = -1
    global adb_radio_log_pid
    adb_radio_log_pid = -1
    global adb_events_log_pid
    adb_events_log_pid = -1
    global capture_log
    capture_log = False
    def __init__(self, name, suit_name, app_name, enabled=True,run_Reason=CASE_RUN_SELF):
        self.name = name
        self.suit_name = suit_name
        self.app_name = app_name
        self.enabled = enabled
        self.launcher = Launcher()
        self.runReason=run_Reason

    def test_case_init(self):
        '''
        init the test case . such as: set the L{current_case_continue_flag<current_case_continue_flag>} to True;
        save the current case name; init the logging; launcher this application
        '''
        case_config_map = fs_wrapper.get_test_case_config(self.name, self.suit_name)
        global case_des
        case_des = case_config_map.get(fs_wrapper.CASE_DESCRIPTION)
        if case_des == None:
            case_des = ''

        #if auto insert case waypoint.
        if SC.PRIVATE_TRACKING_AUTO_INSERT_CASE_WAYPOINT:
            if int(SC.PUBLIC_RUNNING_REPEAT_NUMBER) == 1:
                case_utility.insert_waypoint(case_utility.START_RUN + self.name, case_des)
            else:
                case_utility.insert_waypoint(case_utility.START_RUN + '(' + str(self.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ') ' + self.name, case_des)

        if getprop_suspend():
            log_test_case('TestCaseBase', 'enable touch panel')
            enableTouchPanel()
            log_test_case('TestCaseBase', 'end enable touch panel')

        if getprop_suspend() :
            signal.signal(signal.SIGUSR1, OnshakeSignal_handler)
            log_test_case('suspend', 'suspended, wait for shake-signal from java resume --- 3')
            signal.pause()
            log_test_case('Finally!!!', 'good luck, already gotten signal and resumed.... --- 4')
        log_test_framework(self.name, 'case init...')
        set_can_continue()
        if(self.runReason== CASE_BE_REFERED):
            (ori_suit_name, ori_case_name) = self.original_ClassName.rsplit('.', 1)
            set_cur_case_name(ori_case_name)
        elif(self.runReason==CASE_RUN_SELF):
            set_cur_case_name(self.name)
        qsst_log_case_init()
        clear_logcat()
        #deal with watcher ANR and FC
        global enable_watcher_anr_fc
        enable_watcher_anr_fc = case_config_map.get(fs_wrapper.CASE_ENABLE_WATCHER_ANR_AND_FC)
        if(enable_watcher_anr_fc == '0'):
            case_utility.disable_watcher_anr_fc()

    def test_case_end(self):
        '''
        end the test case . call L{exit_app<exit_app>} to exit the application
        '''
        #if auto insert case waypoint.
        if SC.PRIVATE_TRACKING_AUTO_INSERT_CASE_WAYPOINT:
            if int(SC.PUBLIC_RUNNING_REPEAT_NUMBER) == 1:
                case_utility.insert_waypoint(case_utility.END + self.name, case_des)
            else:
                case_utility.insert_waypoint(case_utility.END + '(' + str(self.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ') ' + self.name, case_des)

        #deal with watcher ANR and FC
        global enable_watcher_anr_fc
        if(enable_watcher_anr_fc == '0'):
            case_utility.enable_watcher_anr_fc()
        self.exit_app()
        log_test_framework(self.name, 'case end')

        self.stop_capture_adb_qxdm_log()

    def test_case_notification(self):
        '''
        send notification to tell user that the current case is starting
        '''
        import settings.common as SC
        if fs_wrapper.run_init_settings:
            case_utility.update_notificationbar('presettings is running...')
        else:
            set_can_continue()
            if(self.runReason == CASE_BE_REFERED):
                (ori_suit_name, ori_case_name) = self.original_ClassName.rsplit('.', 1)
            elif(self.runReason==CASE_RUN_SELF):
                ori_suit_name=self.suit_name
                ori_case_name=self.name
            else:
                return
            case_description=self.case_config_map.get(fs_wrapper.CASE_DESCRIPTION)
            if(case_description==None or case_description==""):
                note_case_info=ori_case_name
            else:
                note_case_info=case_description
            suit_config_map=fs_wrapper.get_test_suit_config(ori_suit_name)
            suit_description=suit_config_map.get(fs_wrapper.SUIT_DESCRIPTION)
            if(suit_description==None or suit_description=="" ):
                note_suit_info=ori_suit_name
            else:
                note_suit_info=suit_description
            #case_utility.update_notificationbar('(' + str(self.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ')' + self.suit_name + '.' + self.name)
            log_test_framework('notify', '(' + str(self.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ')' + note_suit_info + '.' + note_case_info)
            case_utility.update_notificationbar('(' + str(self.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ')' + note_suit_info + '.' + note_case_info)

    def test_case_run(self, case_results):
        '''
        the entry of the case.through this method to control the case life cycle.

        @type case_results: array
        @param case_results: the case result array.
        '''
        try:
            self.test_case_notification()
            '''init the case'''
            self.test_case_init()
            check_capacity_result = self.check_capacity()
            if check_capacity_result != "":
                qsst_log_case_status(logging_wrapper.UNSUPPORTED_CASE, "Unsupported case, need capacity:" + check_capacity_result, logging_wrapper.SEVERITY_HIGH)
                self.test_case_end()
                return False
            self.start_capture_adb_qxdm_log()
        except Exception as e:
            '''if an exception occurs,we will set the status of this case to STATUS_FAILED'''
            self.dealwith_exception(e)
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, str(e), logging_wrapper.SEVERITY_HIGH)
            self.test_case_end()
            return False
        try:
            # lanch this app from launcher
            self.launcher.launch_from_launcher(self.app_name)
            success = self.test_case_main(case_results)
        except Exception as e:
            '''if an exception occurs,we will set the status of this case to STATUS_FAILED'''
            str_context = get_context_info()

            if str_context == None:
                str_exception = "CONTEXT:"+str_context+" "+logging_wrapper.DIVIDE+str(e)
            else:
                str_exception = str(e)
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, str_exception, logging_wrapper.SEVERITY_HIGH)
            self.dealwith_exception(e)
            self.test_case_end()
            return False
        self.test_case_end()
        if success == None:
            return True
        return success


    def test_case_main(self, case_results):
        '''
        the subclass need to override this function to do itself things

        @type case_results: array
        @param case_results: the case result array.
        '''
        case_results.append((self.name, False))

    def __str__(self):
        return '[Case][Name: %s, SuitName: %s, enabled: %d]' % (self.name, self.suit_name, self.enabled)

    @staticmethod
    def createInstance(class_name, *args, **kwargs):
        '''
        give the class name and the args to create a test instance

        @type class_name: string
        @param class_name: class name of this case
        @type args: reference
        @param args: arguments the case needs
        '''
        (module_name, class_name) = class_name.rsplit('.', 1)
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        o = class_meta(*args, **kwargs)
        return o

    # exit the app , the default behavior is to click the back key
    # if your app is not fit , please override this method
    def exit_app(self):
        '''
        exit this application. the subclass can override to complete itself steps to exit it own application
        '''
        try:
            self.launcher.back_to_launcher()
            return True
        except Exception as e:
            self.dealwith_exception(e)
            return False

    def dealwith_exception(self, e):
        '''
        deal with the exception.such as: save the exception stack or exception message
        '''
        save_fail_log()
        log_test_framework('TestCaseBase','Exception is :' + str(e))
        log_test_framework('TestCaseBase','Traceback :' + traceback.format_exc())

    def check_capacity(self):
        case_capacity=self.case_config_map.get(fs_wrapper.CASE_DEPEND_CAPACITY)
        if case_capacity == None:
            return ""
        capacities = case_capacity.split(",")
        for capacity in capacities:
            if not capacity in CC.capacity_list:
                return capacity
        return ""

    def start_capture_adb_qxdm_log(self):
        #start capture adb log and qxdm log on server side
        global adb_main_log_pid
        global adb_radio_log_pid
        global adb_events_log_pid
        global capture_log
        disable_hostlogging = self.case_config_map.get(fs_wrapper.CASE_DISABLE_HOSTLOGGING)
        if (not fs_wrapper.run_init_settings) and (not disable_hostlogging == "true") and SC.PRIVATE_HOSTLOGGING_ENABLE_FEATURE:
            l = len(SC.PUBLIC_LOG_PATH)
            log_path = get_log_path_on_server_side()
            init_qxdm_success = get_init_qxdm_success()
            adb_log_path = log_path + "\\" + self.suit_name + "\\" + self.name + "\\adblog"
            qxdm_log_path = log_path + "\\" + self.suit_name + "\\" + self.name + "\\qxdmlog"
            case_utility.mkdir_on_server_side(adb_log_path)
            case_utility.mkdir_on_server_side(qxdm_log_path)
            adb_main_log_pid = case_utility.start_capture_adblog("adb logcat -v time >> " + adb_log_path + "\\main.log")
            adb_radio_log_pid = case_utility.start_capture_adblog("adb logcat -v time -b radio >> " + adb_log_path + "\\radio.log")
            adb_events_log_pid = case_utility.start_capture_adblog("adb logcat -v time -b events >> " + adb_log_path + "\\events.log")
            capture_log = True

    def stop_capture_adb_qxdm_log(self):
        #stop capture adb log and qxdm log on server side
        disable_hostlogging = self.case_config_map.get(fs_wrapper.CASE_DISABLE_HOSTLOGGING)
        if capture_log and (not fs_wrapper.run_init_settings) and (not disable_hostlogging == "true") and SC.PRIVATE_HOSTLOGGING_ENABLE_FEATURE:
            case_utility.stop_capture_adblog(adb_main_log_pid)
            case_utility.stop_capture_adblog(adb_radio_log_pid)
            case_utility.stop_capture_adblog(adb_events_log_pid)
            case_utility.clear_adb_log()
            l = len(SC.PUBLIC_LOG_PATH)
            log_path = get_log_path_on_server_side()
            init_qxdm_success = get_init_qxdm_success()
            path = log_path + "\\" + self.suit_name + "\\" + self.name + "\\qxdmlog\\"
            if init_qxdm_success:
                if not case_utility.save_item_store(path.replace("\\\\", "\\")):
                    log_test_framework(self.name, "Save item failed [" + path.replace("\\\\", "\\") + "].")
                if not case_utility.clear_view_items():
                    log_test_framework(self.name, "clear view failed.")
