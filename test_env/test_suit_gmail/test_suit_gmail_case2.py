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

class test_suit_gmail_case2(TestCaseBase):
    '''
    test_suit_gmail_case2 is a class for gmail case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        launcher.launch_from_launcher('gmail')

        wait_fun = lambda:search_text(gmail.get_value("waiting_for_sync"),1,0)
        wait_for_fun(wait_fun,False,20)

        #receive mail
        receive_email()

        # write an new mail
        click_imageview_by_id("compose")

        '''for i in range(1,61):
            ime.IME_input_english(1,"test")
            body_text = body_text + "Hello World  "
            print("i="+str(i))'''

        subject = "auto.test.gmail.sample"

        click_textview_by_id("to",1,0)
        ime.IME_input(1,SC.PRIVATE_GMAIL_GMAIL_ACCOUNT_SEQUENCE)

        #input subject
        click_textview_by_id("subject")
        ime.IME_input_english(1,subject)

        #input content
        body_text = "t"
        for i in range(0,15):
            ime.IME_input_english(1,body_text)
        #entertext_edittext_by_id("body_text",content)

        #send mail
        send_email()

        #receive mail
        receive_email()

        #read mail
        click_in_list_by_index(0)

        while not search_text(gmail.get_value("inbox"),1,0,"1"):
            sleep(1)

        for i in range(1,3):
            scroll_to_bottom()
            sleep(1)
            scroll_to_top()
            sleep(1)

        #reply mail
        click_imageview_by_desc(gmail.get_value("reply"))
        sleep(1)

        click_textview_by_id("to")
        send_key(KEY_DEL)
        ime.IME_input(1,SC.PRIVATE_GMAIL_GMAIL_ACCOUNT_SEQUENCE)

        click_textview_by_id("body_text")
        ime.IME_input_english(1,"Thanks")
        #entertext_edittext_by_id("body_text","Thanks!")

        #send mail
        send_email()
        goback()

        #receive mail
        receive_email()

        # delete an email
        click_in_list_by_index(0)
        while not search_text(gmail.get_value("inbox"),1,0,'1'):
            sleep(1)

        click_imageview_by_id("delete")
        goback()

        #click_checkbox_by_index(0)
        #click_imageview_by_id("delete")
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

def send_email():
    '''
    send mail 

    '''
    click_imageview_by_id("send")

    loading_fun = lambda:search_text(gmail.get_value("sending"),1,0)
    wait_for_fun(loading_fun,False,10)

def receive_email():
    '''
    receive email 

    '''
    click_imageview_by_id("refresh")
    sleep(5)