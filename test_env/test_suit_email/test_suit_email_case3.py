#coding=utf-8
'''
   Write an new email, send,receive, read and reply


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
#    Write an new email, send,receive, read and reply
#precondition:
#    login email
#steps:
#    receive emails
#    write an new email and send
#    receive emails
#    read email
#    reply email
############################################

class test_suit_email_case3(TestCaseBase):
    '''
    test_suit_email_case3 is a class for gmail case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        launcher.launch_from_launcher('email')

        ######Write an new email, send ,receive, read and reply Beign
        #receive emails
        receive_email()

        # write an new email
        click_imageview_by_id("compose",1,0)
        sleep(2)

        subject = "email.sample"

        click_textview_by_id("to",1,0)
        ime.IME_input(1,SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE)

        #input subject
        click_textview_by_id("subject")
        ime.IME_input_english(1,subject)

        #input content
        body_text = "t"
        for i in range(0,15):
            ime.IME_input_english(1,body_text)

        '''body_text = ""
        for i in range(1,61):
            body_text = body_text + "Hello World  "
        subject = "auto_test_email_sample"
        email.write_email(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT, subject, body_text)
        '''

        #send mail
        click_imageview_by_id("send")

        #read mail
        receive_email()

        click_in_list_by_index(0)
        sleep(2)

        for i in range(1,3):
            scroll_to_bottom()
            sleep(2)
            scroll_to_top()
            sleep(2)

        #reply email
        click_button_by_id("reply",1,0)
        sleep(1)
        click_textview_by_id("body_text")
        ime.IME_input_english(1,"Thanks")

        #send mail
        click_imageview_by_id("send")
        goback()
        ######Write an new email, send ,receive, read and reply Beign
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

def receive_email():
    '''
    receive email 

    '''
    click_imageview_by_id("refresh",1,0)
    loading_fun = lambda:search_text(email.get_value("status_loading_messages"),1,0)
    wait_for_fun(loading_fun,False,20)