#coding=utf-8
'''
   Write an new mail, send ,receive, read and reply


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
#    Write an new mail, send ,receive, read and reply
#precondition:
#    login gmail
#steps:
#    Write mail
#    send mail
#    receive mail
#    read mail
#    reply mail
############################################

class test_suit_gmail_case3(TestCaseBase):
    '''
    test_suit_gmail_case3 is a class for gmail case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        sleep(5)

        launcher.launch_from_launcher('gmail')

        wait_fun = lambda:search_text(gmail.get_value("waiting_for_sync"),1,0)
        wait_for_fun(wait_fun,False,20)

        # write an new mail
        click_imageview_by_id("compose")

        subject = "auto.test"

        click_textview_by_id("to",1,0)
        ime.IME_input(1,SC.PRIVATE_GMAIL_GMAIL_ACCOUNT_SEQUENCE)

        #input subject
        click_textview_by_id("subject")
        ime.IME_input_english(1,subject)

        #input content
        ime.IME_input_english(1,"test.email")
        #entertext_edittext_by_id("body_text",content)

        #send mail
        send_email()

        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

def send_email():
    '''
    send mail 

    '''
    click_imageview_by_id("send")
