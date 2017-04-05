#coding=utf-8
'''
   login email


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
#    login email
#precondition:
#    exist email account and wifi
#steps:
#    Add Email Account
############################################

class test_suit_email_case1(TestCaseBase):
    '''
    test_suit_email_case1 is a class for email case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        #Add Email Account Begin
        sleep(3)
        goback()
        local_assert(email.add_email_account(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_EMAIL_EMAIL_PASSWORD_SEQUENCE),True)

        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
