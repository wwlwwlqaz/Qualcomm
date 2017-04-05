'''
   make calls by slot 2.


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
from test_suit_phone_case1 import pre_settings
############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    make calls by slot 2
#precondition:
#    exist slot 2
#steps:
#    switch voice call to always ask(if switch before, ignore it)
#    dial number
#    call
#    make sure whether get though
############################################

class test_suit_phone_case2(TestCaseBase):
    '''
    test_suit_phone_case2 is a class for phone case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''

        start_activity('com.android.contacts','.activities.DialtactsActivity')

        #switch voice call to always ask(if switch before, ignore it)
        pre_settings()

        call_repeat_times = int(SC.PRIVATE_PHONE_CALL_REPEAT_TIMES)
        define_case_success_times = int(SC.PRIVATE_PHONE_DEFINE_CASE_SUCCESS_TIMES)
        call_time = int(SC.PRIVATE_PHONE_CALL_TIME)

        success_times = 0
        global case_flag
        case_flag = False

        for i in range(0,call_repeat_times):
            sleep(3)

            #go to Dial Activity.
            drag_by_param(0,50,100,50,10)
            drag_by_param(0,50,100,50,10)

            phoneNumber = SC.PRIVATE_PHONE_GSM_WCDMA_CALL_PHONENUMBER

            #MO
            #dial number
            #call
            #make sure whether get though
            phoneOn = phone.phone_call(phoneNumber, "", 1)

            if phoneOn:
                sleep(call_time)
                success_times = success_times + 1
                if search_view_by_id("endButton"):
                    click_button_by_id("endButton")

        if(success_times < define_case_success_times):
            case_flag = False
            case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], False))
        else:
            case_flag = True
            case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'end')
        if can_continue() and case_flag == True:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            save_fail_log()
