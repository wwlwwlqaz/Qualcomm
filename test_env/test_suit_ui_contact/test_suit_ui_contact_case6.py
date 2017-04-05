'''
@author: wxiang

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_ui_contact_case6(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for add a new contact from dialer

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_contact_case6 : case Start')
        global case_flag
        case_flag = False
        
        phoneNumber = '10086'
        phonename = 'addFromDialer'
        # PREDEFINED_NUMBERS = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
        
        # launch dialer
        start_activity('com.android.dialer', '.DialtactsActivity')
        phone.go_home()
        sleep(2)
        if is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'floating_action_button', isScrollable=0):
            log_test_framework("ui_contact_case6 :", "xxxxxxxxxx1")
            click_imageview_by_id('floating_action_button')
        """
        # clear  dial panel 
        if get_view_text_by_id(VIEW_EDIT_TEXT, 'digits', isScrollable=0).strip() != '':
            log_test_framework("ui_contact_case6 :", "xxxxxxxxxx2")
            click_textview_by_id('digits')
            sleep(1)
            click_imageview_by_id('deleteButton', clickType=LONG_CLICK)
        else:
            log_test_framework("ui_contact_case6 :", "xxxxxxxxxx3")
        """
        """
        if get_view_text_by_id(VIEW_EDIT_TEXT, 'digits', isScrollable=0) != '':
            click_textview_by_id('digits', clickType=LONG_CLICK)
            click_imageview_by_id('deleteButton')
        """
        '''if search_view_by_id('deleteButton'):
            click_imageview_by_id("deleteButton", 1, 0, 0, LONG_CLICK)
        else:
            log_test_framework("ui_contact_case6 :", "dial panel is empty without any input number")'''
       
        for i in range(0, len(phoneNumber)):
            # click_imageview_by_id(str(PREDEFINED_NUMBERS[phoneNumber[i]]))
            """
            click_textview_by_text(str(phoneNumber[i]), isScrollable=0, searchFlag=TEXT_MATCHES)
            sleep(1)
            """
            sleep(1)
            if is_view_enabled_by_text(VIEW_TEXT_VIEW, str(phoneNumber[i]), isScrollable=0):
                log_test_framework("ui_contact_case6 :", "xxxxxxxxxx4")
                click_textview_by_text(str(phoneNumber[i]), isScrollable=0, searchFlag=TEXT_MATCHES)
            
            
                             
        case_flag = contact.add_contact_from_dial(phoneNumber, phonename)
        
        sleep(2)
        log_test_framework("ui_contact_case6 :", "Finally delete contacts added from dial panel")
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        click_textview_by_text('All contacts', isScrollable=0)
        contact.del_all_contact(phonename, phoneNumber, '')
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "success" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "fail", SEVERITY_HIGH)
        
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        
        
              

    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case6 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case6 : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case6 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case6 : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case6 : \tfail')
            save_fail_log()
