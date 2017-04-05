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



class test_suit_cmcc_devci_gallery_case7(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch camera
    Step2:check if the gallery can show the pics and videos correctly
    Verification: 
    ER1:phone number would display as URI
    ER2:DUT would go into Dialer"
    
    '''
    
    
    def test_case_main(self, case_results):
        global case_flag , TAG        
        case_flag = False
        TAG = "Dev-ci cases: Gallery "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """

        take_screenshot()
        send_key(KEY_HOME)
        sleep(1)
        long_click(969,814)        
        if wait_for_fun(lambda:search_text("WALLPAPERS"), True, 5):
            click_textview_by_id("wallpaper_button")
            if wait_for_fun(lambda:search_view_by_id("wallpaper_item_label"), True, 5):
                click_textview_by_text("My photos")
                sleep(3)
                if search_text("Open from"):
                    click_textview_by_text("Snapdragon Gallery")
                    sleep(2)
                long_click(290,539)
                if wait_for_fun(lambda:search_text("OPEN"), True, 5):
                    click_textview_by_text("OPEN")
                if wait_for_fun(lambda:search_view_by_id("set_wallpaper_button"), True, 5):
                    click_button_by_id("set_wallpaper_button")
                    if wait_for_fun(lambda:search_text("Home screen"), True, 5):
                        click_textview_by_text("Home screen")
                        if wait_for_fun(lambda:search_view_by_desc("Apps"), True, 6):
                            log_test_framework("cmcc_devci_gallery_case7:", "set wallpaper successfully")
                            case_flag = True       
        elif search_text('has stopped'):
            log_test_framework("cmcc_devci_gallery_case7:", "Popup has stopped")
            take_screenshot()
            click_textview_by_text('OK')
            sleep(2)
        elif search_text("isn't responding"):
            take_screenshot()
            sleep(5)
            click_textview_by_text("OK")
            log_test_framework("cmcc_devci_gallery_case7:", "ANR")
        else:
            log_test_framework("cmcc_devci_gallery_case7:", "case fail")

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
            
