#coding=utf-8
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

class test_suit_cmcc_mtbf_case12(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case12 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_cmcc_mtbf_case12"
    '''@var TAG: tag of test_suit_cmcc_mtbf_case12'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        cmccMTBF.launch_app_by_name("browser")
        for i in range(0, 5):
            cmccMTBF.browser_clear_browser_history_cookie()
            boo = cmccMTBF.browser_access_browser("www.sina.com.cn", u"新浪")
            if not boo:
                qsst_log_case_status(logging_wrapper.STATUS_FAILED, "Open Sina failed at " + str(i) + "times.", logging_wrapper.SEVERITY_HIGH)
                return False
        cmccMTBF.browser_exit_browser()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "Open Sina success.", logging_wrapper.SEVERITY_HIGH)
        return True
