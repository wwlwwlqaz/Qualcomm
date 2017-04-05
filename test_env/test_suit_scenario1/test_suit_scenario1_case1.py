'''
   this case is responsible for open wifi and add a google account.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
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
from qrd_shared.case import *
from case_utility import *
from utility_wrapper import *
from logging_wrapper import log_test_case, take_screenshot,log_test_framework
from test_case_base import TestCaseBase
import settings.common as SC

class test_suit_scenario1_case1(TestCaseBase):
    '''
    test_suit_scenario1_case1 is a class for scenario1 case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_scenario1_case1"
    '''@var TAG: tag of test_suit_scenario1_case1'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        success = 0
        launcher.launch_from_launcher("system_settings")
        count = 0
        flag = True
        while(flag):
            if not settings.enable_wifi(SC.PUBLIC_WIFI_NAME, SC.PUBLIC_WIFI_PASSWORD_SEQUENCE):
                count += 1
                if count == 3:
                    flag = False
            else:
                success += 1
                flag = False

        if not settings.add_google_account(SC.PRIVATE_GMAIL_GMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_GMAIL_GMAIL_PASSWORD_SEQUENCE):
            log_test_framework(self.TAG, "add google account fail.")
            set_cannot_continue()
        else:
            success += 1
            if call("test_suit_playstore", "test_suit_playstore_case2"):
                success += 1

        if success < 3:
            set_cannot_continue()
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

