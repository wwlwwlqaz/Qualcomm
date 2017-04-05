#coding=utf-8
'''
   setting email


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{TestCaseBase <TestCaseBase>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    setting email
#precondition:
#    login email
#steps:
#    setting signature
#    setting quick responses
#    setting check frequency
############################################

class test_suit_email_case2(TestCaseBase):
    '''
    test_suit_email_case2 is a class for email case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        launcher.launch_from_launcher('email')

        sleep(2)

        loading_fun = lambda:search_text(email.get_value("status_loading"),1,0)
        wait_for_fun(loading_fun,False,20)

        click_menuitem_by_text(email.get_value("settings_action"),1,0)
        click_textview_by_text(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT,1,0)
        '''
        #setting signature
        click_textview_by_text(email.get_value("account_settings_signature_label"),1,0)

        ime.IME_input_english(1,"auto.test")
        #entertext_edittext_by_index(0,"auto_test_email",1,0)
        sleep(1)
        click_button_by_text(email.get_value("okay_action"),1,0)

        #setting quick responses

        click_textview_by_text(email.get_value("account_settings_edit_quick_responses_label"),1,0)
        click_button_by_id("create_new")
        ime.IME_input_english(1,"Thanks")
        #entertext_edittext_by_index(0,"I will reply your email later.Thanks!",1,0)
        sleep(1)
        click_button_by_text(email.get_value("message_view_attachment_save_action"),1,0)
        goback()
        '''

        #setting check frequency
        click_textview_by_text(email.get_value("account_settings_mail_check_frequency_label"),1,0)
        click_in_list_by_index(2)
        goback()
        goback()
        ######Email Setting End
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
