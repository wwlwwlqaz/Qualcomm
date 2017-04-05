'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
import string


class test_suit_cmcc_devci_contact_case9(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    
    def test_case_main(self, case_results):
        global case_flag, case_flag_add, case_flag_join,case_flag_groupA,case_flag_groupB
        case_flag = False
        case_flag_add = False
        case_flag_join = False
        case_flag_groupA = False
        case_flag_groupB = False
        global TAG
        TAG = "Dev-ci cases: Contact "
        log_test_framework(TAG, self.name + " -Start")
        
        
        """
        cases contnets you need to add
        """
        
        contact_list = [ ['contactA', '10086'], ['contactB', '10010']]
        
        # launch contact
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        contact.go_home()
        
        # click "All contacts" sheet to lock view
        click_textview_by_text(SC.PRIVATE_CONTACT_CONTACTS_OPTION, isScrollable=0)
        
        # we need to delete all contact 
        contact.contact_to_display()
        local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1, SC.PRIVATE_CONTACT_SIM2))
        
        log_test_framework(self.name, "Now add new contactA and B  ")
        for i in range(0, 2):
            scroll_to_top()
            click_imageview_by_desc('add new contact')
            click_textview_by_id('account_type')
            sleep(1)
            click_textview_by_text('PHONE')
            click_textview_by_id('group_list')
            if i == 0: 
                click_textview_by_text('Coworkers')
            if i == 1: 
                click_textview_by_text('Family')
            goback()
            sleep(3)
            contact.add_contact_into_phone(contact_list[i][0], contact_list[i][1])
            
        if search_text(contact_list[0][0]) and search_text(contact_list[1][0]):
            log_test_framework(self.name, "Contact A/B create successfully")
            case_flag_add = True
        else:
            log_test_framework(self.name, "Contact A/B create failed")
            case_flag_add = False
            set_cannot_continue()
        
        if can_continue():
            click_textview_by_text(contact_list[0][0])
            if is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'menu_edit', isScrollable=0):
                click_textview_by_id('menu_edit')
                sleep(1)
                #click_imageview_by_desc('More options')
                #click_button_by_index(1)
                send_key(KEY_MENU)
                sleep(1)
                click_textview_by_text('Join')
                click_textview_by_text(contact_list[1][0])
                click_imageview_by_id('save_menu_item')
                scroll_to_bottom()
                if search_text(contact_list[0][0]) and search_text(contact_list[1][1]) and (not search_text(contact_list[1][0])):
                    log_test_framework(self.name, "Contact B have been joined into A editer")
                    case_flag_join = True
                else:
                    log_test_framework(self.name, "Contact B combined with contact A Failed")
                    set_cannot_continue()
        else:
            take_screenshot()
        
        if can_continue():
            contact.go_home()
            # click "Group" sheet to lock view
            click_textview_by_text('GROUPS', isScrollable=0)
            # index 6 = Coworker
            # index 7 = number of     Coworker
            # index 8 = Family
            # index 9 = number of Family
            # index 10= Friend
            # index 11= number of Friend
            coworker = get_view_text_by_index(VIEW_TEXT_VIEW, 6)
            coworker_counter = get_view_text_by_index(VIEW_TEXT_VIEW, 7)
            family = get_view_text_by_index(VIEW_TEXT_VIEW, 8)
            family_counter = get_view_text_by_index(VIEW_TEXT_VIEW, 9)
            log_test_framework(self.name, '####Groups detailed info--->####' + coworker + ' : ' + coworker_counter + ' ' + family + ' : ' + family_counter)
            local_assert(1, string.atoi(coworker_counter.split(' ')[0]))
            local_assert(1, string.atoi(family_counter.split(' ')[0]))
            
            click_textview_by_text('Coworkers')
            if search_text(contact_list[0][0]):
                case_flag_groupA=True
            #local_assert(True, search_text(contact_list[0][0]))
            click_imageview_by_desc('Navigate up')
            click_textview_by_text('Family')
            if search_text(contact_list[0][0]):
                case_flag_groupB=True
        
        contact.go_home()
            
        case_flag=case_flag_add and case_flag_join and case_flag_groupA and case_flag_groupB

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
    
