#coding=utf-8
'''
   delete email


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
from test_suit_email_case3 import receive_email

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    delete email
#precondition:
#    login email
#steps:
#    receive emails
#    delete email
############################################

class test_suit_email_case4(TestCaseBase):
    '''
    test_suit_email_case4 is a class for gmail case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        launcher.launch_from_launcher('email')

        #receive emails
        receive_email()

        #delete an email
        scroll_to_top()
        click_in_list_by_index(0)
        sleep(2)

        click_imageview_by_id("delete",1,0)
        goback()

        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
