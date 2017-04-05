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
from qrd_shared.case import *
from case_utility import *
from utility_wrapper import *
import logging_wrapper
from test_case_base import TestCaseBase

class test_suit_cmcc_mtbf_case4(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case4 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_cmcc_mtbf_case4"
    '''@var TAG: tag of test_suit_cmcc_mtbf_case4'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        cmccMTBF.launch_app_by_name("mms")
        for i in range(0, 20):
            cmccMTBF.messaging_delete_all_threads()
            boo = cmccMTBF.messaging_check_draft_function('18918799780', 'message')
            if not boo:
                qsst_log_case_status(logging_wrapper.STATUS_FAILED, "Check draft function failed at " + str(i + 1) + " times.", logging_wrapper.SEVERITY_HIGH)
                return False
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "Draft function pass.", logging_wrapper.SEVERITY_HIGH)
        return True
