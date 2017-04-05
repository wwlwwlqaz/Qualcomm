'''
@author: c_caijie
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.mms.Mms import *



class test_suit_stress_test_camera1_case000021(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch Camera;
    Step2: tap thumbnail to view the snapshot;
    Step3:switch from  right to left; 
    Step4:switch from left to right;
    Verification: 
    ER4:No exception.    
    '''
    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG, testresult, success_flag, i, success_time1, right_to_left_flag, left_to_right_flag, success_time2, fail_time1, fail_time2
        case_flag = False
        right_to_left_flag = False
        left_to_right_flag = False
        testresult1 = []
        testresult2 = []
        success_time1 = 0
        fail_time1 = 0
        success_time2 = 0
        fail_time2 = 0
        iterationNum = 200
        TAG = "Dev-ci cases: Camera "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """
        if search_text("Close app", searchFlag=TEXT_CONTAINS):
            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
            sleep(2) 
                    
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 10):
            click_button_by_id('permission_allow_button')
        if wait_for_fun(lambda:search_text('OK'), True, 5):            
            click_textview_by_text('OK')
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
            log_test_framework("step1:", "Launch camera pass")            
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_delete"), True, 5):
                    log_test_framework("step2:", "tap thumbnail to view the snapshot pass")
                    '''
                    from right to left
                    '''
                    for i in range(iterationNum):
                        print_log_line('from right to left iteration %d'%(i+1))
                        success_flag = False
                        drag_by_param(90, 50, 10, 50, 10)
                        sleep(2)
                        if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                            log_test_framework("step3:", "switch from  right to left pass")
                            success_flag = True
                        if success_flag == True:
                            testresult1.append('%d.Pass'%(i+1))
                            success_time1=success_time1+1
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                        else:
                            testresult1.append('%d.Fail'%(i+1))
                            take_screenshot()
                            fail_time1=fail_time1+1
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                            if search_text("Close app", searchFlag=TEXT_CONTAINS):
                                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                                click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                                sleep(2)
                            start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                            if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):            
                                if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                                    click_imageview_by_id("preview_thumb")
                                    sleep(3)
                    if success_time1 == iterationNum:
                        right_to_left_flag = True
                    print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'from right to left success:%d fail:%d iteration:%d'%(success_time1,fail_time1,iterationNum))
                    print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult1)                     
                    
                    
                    '''
                    from left to right
                    '''
                    for i in range(iterationNum):
                        print_log_line('from from left to right iteration %d'%(i+1))
                        success_flag = False
                        drag_by_param(90, 50, 10, 50, 10)
                        sleep(2)
                        if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                            log_test_framework("step4:", "switch from left to right pass")
                            success_flag = True
                        if success_flag == True:
                            testresult2.append('%d.Pass'%(i+1))
                            success_time2=success_time2+1
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                        else:
                            testresult2.append('%d.Fail'%(i+1))
                            take_screenshot()
                            fail_time2=fail_time2+1
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                            if search_text("Close app", searchFlag=TEXT_CONTAINS):
                                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                                click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                                sleep(2)
                            start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                            if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):            
                                if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                                    click_imageview_by_id("preview_thumb")
                                    sleep(3)
                    if success_time2 == iterationNum:
                        left_to_right_flag = True
                    print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'from left to right success:%d fail:%d iteration:%d'%(success_time2,fail_time2,iterationNum))
                    print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult2)
                    case_flag = right_to_left_flag and left_to_right_flag       
        if search_text("isn't responding", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs ANR")            
            take_screenshot()
            if search_text("Close app", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                sleep(2)
            if search_text("Close", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close")
                sleep(2)            
        elif search_text("Unfortunately", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs crash")
            take_screenshot()
            if search_text("OK", searchFlag=TEXT_CONTAINS):
                click_button_by_text("OK")
                sleep(2)
            if search_text("Close", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close")
                sleep(2)            
        elif search_text("stopped", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Popup has stopped")
            take_screenshot()
            if search_text("Close", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close")
                sleep(2)            
            if search_text("OK", searchFlag=TEXT_CONTAINS):
                click_button_by_text("OK")
                sleep(2)       
        elif search_text("Close app", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Popup Close app error")
            take_screenshot()            
            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
            sleep(2)
        send_key(KEY_BACK)
        sleep(1)
        send_key(KEY_BACK)
        sleep(1)
        send_key(KEY_HOME)
        sleep(1)        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "", SEVERITY_HIGH)
        
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        
        
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : end')
        if can_continue() and case_flag == True:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tfail')
        save_fail_log()
            
