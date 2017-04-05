'''
   Login gmail


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
#    Login gmail
#precondition:
#    There is a gmail account
#steps:
#    Login gmail
############################################

class test_suit_gmail_case1(TestCaseBase):
    '''
    test_suit_gmail_case1 is a class for gmail case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        #Login
        sleep(5)

        start_activity('com.android.settings','.Settings')
        scroll_to_bottom()
        local_assert(settings.add_google_account(SC.PRIVATE_GMAIL_GMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_GMAIL_GMAIL_PASSWORD_SEQUENCE),True)

        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
