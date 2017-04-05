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



class test_suit_cmcc_devci_filemanager_case2(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch camera
    Step2:Check camera
    Verification: 
    ER1:phone number would display as URI
    ER2:DUT would go into Dialer"
    
    '''
    
    
    def test_case_main(self, case_results):
        
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Filemanager "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """
        send_key(KEY_HOME)
        sleep(1)
        long_click(969,814)        
        if wait_for_fun(lambda:search_text("WALLPAPERS"), True, 5):
            click_textview_by_id("wallpaper_button")
            if wait_for_fun(lambda:search_view_by_id("wallpaper_item_label"), True, 5):
                click_textview_by_text("My photos")
                sleep(3)
            if wait_for_fun(lambda:search_view_by_desc("Show roots"), True, 3):
                click_imageview_by_desc("Show roots")    
        start_activity('com.cyanogenmod.filemanager','com.cyanogenmod.filemanager.activities.NavigationActivity')
        if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
            phone.permission_allow()                   
        if wait_for_fun(lambda:is_view_enabled_by_id(VIEW_BUTTON, "ab_actions"), True, 5) or is_view_enabled_by_text(VIEW_TEXT_VIEW, "Android") or search_view_by_id("ab_search"):                
            log_test_framework("cmcc_devci_filemanager_case1:", "Launch filemanager pass")
            send_key(KEY_BACK)
            send_key(KEY_BACK)
            send_key(KEY_HOME)
            if wait_for_fun(lambda:search_view_by_desc("Apps"), True, 3):
                log_test_framework("cmcc_devci_filemanager_case1:", "Exit pass")
                case_flag = True
        if search_text('has stopped'):
            log_test_framework("cmcc_devci_filemanager_case1:", "Popup has stopped")
            take_screenshot()
            if search_text("OK"):
                click_button_by_text("OK")
                sleep(2)
            if search_text("Close"):
                click_button_by_text("Close")
                sleep(2)            
        elif search_text("Unfortunately"):
            take_screenshot()
            if search_text("OK"):
                click_button_by_text("OK")
                sleep(2)
            if search_text("Close"):
                click_button_by_text("Close")
                sleep(2)
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs Crash")
            
        elif search_text("isn't responding"):
            take_screenshot()
            if search_text("OK"):
                click_button_by_text("OK")
                sleep(2)
            if search_text("Close"):
                click_button_by_text("Close")
                sleep(2)
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs ANR")
        else:
            log_test_framework("cmcc_devci_filemanager_case1:", "Launch filemanager fail")                


       
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
            
