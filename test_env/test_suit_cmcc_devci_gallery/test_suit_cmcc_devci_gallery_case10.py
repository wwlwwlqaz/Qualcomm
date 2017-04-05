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



class test_suit_cmcc_devci_gallery_case10(TestCaseBase):
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
        gallery.gallery_widget()           
        if wait_for_fun(lambda:search_view_by_desc("Apps"), True, 5):            
            log_test_framework("cmcc_devci_gallery_case10:", "case pass")
            case_flag = True       
        elif search_text('has stopped'):
            log_test_framework("cmcc_devci_gallery_case10:", "Popup has stopped")
            take_screenshot()
            click_textview_by_text('OK')
            sleep(2)
        else:
            log_test_framework("cmcc_devci_gallery_case10:", "case fail")

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
            
