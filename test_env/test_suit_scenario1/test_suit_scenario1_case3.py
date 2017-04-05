'''
   loop call test_suit_scenario1_case2 1000 times.


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
from logging_wrapper import log_test_case, take_screenshot, log_test_framework
from test_case_base import TestCaseBase

class test_suit_scenario1_case3(TestCaseBase):
    '''
    test_suit_scenario1_case3 is a class for scenario1 case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_scenario1_case3"
    '''@var TAG: tag of test_suit_scenario1_case3'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        success = 0
        count = 1000
        for i in range(0, count):
            if call("test_suit_scenario1", "test_suit_scenario1_case2"):
                success += 1
        log_test_framework(self.TAG, "total:" + success + "/" + count)
        if success < count:
            set_cannot_continue()
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

