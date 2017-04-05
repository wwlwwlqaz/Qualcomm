'''
   make calls by slot 1.


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
from logging_wrapper import log_test_case,save_fail_log
from test_case_base import TestCaseBase
from qrd_shared.case import *
import test_suit_phone

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    make calls by slot 1
#precondition:
#    exist slot 1
#steps:
#    switch voice call to always ask
#    dial number
#    call
#    make sure whether get though
############################################

class test_suit_phone_case4(TestCaseBase):
    '''
    test_suit_phone_case4 is a class for phone case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''

        start_activity('com.android.contacts','.activities.DialtactsActivity')
        sleep(3)
        #go to Dial Activity.
        drag_by_param(0,50,100,50,10)
        drag_by_param(0,50,100,50,10)
        phoneOn = phone.phone_call("10086", "", 2)

        if phoneOn:
            if search_view_by_id("endButton"):
                click_button_by_id("endButton")
        else:
            qsst_log_case_status(STATUS_FAILED, "phone case failed.", SEVERITY_HIGH)
            return False
        qsst_log_case_status(STATUS_SUCCESS, "phone case success.", SEVERITY_HIGH)