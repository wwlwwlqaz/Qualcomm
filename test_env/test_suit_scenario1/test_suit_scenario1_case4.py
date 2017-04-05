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
from logging_wrapper import *
from test_case_base import TestCaseBase

class test_suit_scenario1_case4(TestCaseBase):
    '''
    test_suit_scenario1_case3 is a class for scenario1 case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_scenario1_case4"
    '''@var TAG: tag of test_suit_scenario1_case4'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''

        fail_num = 0
        if not call("test_suit_renren", "test_suit_renren_case1"):
            qsst_log_case_status(STATUS_FAILED, "renren case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_doubanfm", "test_suit_doubanfm_case1"):
            qsst_log_case_status(STATUS_FAILED, "doubanfm case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_weibo", "test_suit_weibo_case1"):
            qsst_log_case_status(STATUS_FAILED, "weibo case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_email", "test_suit_email_case5"):
            qsst_log_case_status(STATUS_FAILED, "send email case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_camera", "test_suit_camera_case7"):
            qsst_log_case_status(STATUS_FAILED, "share with weibo case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_camera", "test_suit_camera_case8"):
            qsst_log_case_status(STATUS_FAILED, "share with renren case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_mms", "test_suit_mms_case5"):
            qsst_log_case_status(STATUS_FAILED, "send sms case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1
        if not call("test_suit_phone", "test_suit_phone_case4"):
            qsst_log_case_status(STATUS_FAILED, "phone case failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            fail_num += 1

        notificationBar.clear_all()
        if TestCaseBase.cycle_index%10 == 0:
            goToSleepMode(10*60)
        if fail_num > 0:
            qsst_log_case_status(STATUS_FAILED, "test_suit_scenario1_case4 failed at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)
            return False
        qsst_log_case_status(STATUS_SUCCESS, "test_suit_scenario1_case4 success at" + str(TestCaseBase.cycle_index) + "times.", SEVERITY_HIGH)

