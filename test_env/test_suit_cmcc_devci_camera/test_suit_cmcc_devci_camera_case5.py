'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.mms.Mms import *



class test_suit_cmcc_devci_camera_case5(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch camera
    Step2:Take a photo
    Verification: 
    ER1:phone number would display as URI
    ER2:DUT would go into Dialer"
    
    '''
    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Camera "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
#         if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
#             phone.permission_allow()        
#         if wait_for_fun(lambda:search_text('Yes'), True, 5):           
#             click_textview_by_text('Yes')
#         if wait_for_fun(lambda:search_text('OK'), True, 5):           
#             click_textview_by_text('OK')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 10):
            click_imageview_by_id('scene_mode_switcher')
            if wait_for_fun(lambda:search_text("Portrait"), True, 5):
                click_textview_by_text('Portrait')
                sleep(5)
            if search_text('AUTO') == False:
                log_test_framework("cmcc_devci_camera_case5:", "Switch Portrait pass")
                if search_view_by_id('shutter_button'):
                    click_button_by_id('shutter_button')
                    if wait_for_fun(lambda:search_view_by_id('remaining_photos_text'), True, 10):            
                        case_flag = True
            elif search_text('has stopped'):
                log_test_framework("cmcc_devci_camera_case5:", "Switch Portrait then camera has stopped")
                take_screenshot()
                click_textview_by_text('OK')
                sleep(2)
        elif search_text('has stopped'):
            log_test_framework("cmcc_devci_camera_case5:", "Camera has stopped")
            take_screenshot()
            click_textview_by_text('OK')
            sleep(2)        
        elif search_text("isn't responding"):                
                take_screenshot()
                sleep(5)
                click_textview_by_text("OK")
                log_test_framework("cmcc_devci_camera_case5:", "ANR")
        else:
            log_test_framework("cmcc_devci_camera_case5:", "Take Portrait photo fail")
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
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ': case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tfail')
            save_fail_log()
            
