'''
   answer the phone call.


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
#    answer the phone call
#precondition:
#    exist slot
#steps:
#    answer the phone call
#    hang up
############################################

class test_suit_phone_case3(TestCaseBase):
    '''
    test_suit_phone_case3 is a class for phone case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''

        sleep(2)
        #send mms phone number
        slot1_number = SC.PUBLIC_SLOT1_PHONE_NUMBER
        #Hold Time: holding time for each call
        hold_time = int(SC.PRIVATE_PHONE_CALL_TIME)
        #No Answer Wait Time: time for waiting to connect
        no_answer_wait_time = int(SC.PRIVATE_PHONE_NO_ANSWER_WAIT_TIME)
        #Interval Time of Consecutive Calls: time between two calls, should be larger than < Hold Time + No Answer Wait Time + 10>,
        interval_time = hold_time + no_answer_wait_time + 15
        #Number Of Calls: how many calls want to make
        call_repeat_times = int(SC.PRIVATE_PHONE_CALL_REPEAT_TIMES)
        #success lower limit value
        define_case_success_times = int(SC.PRIVATE_PHONE_DEFINE_CASE_SUCCESS_TIMES)

        success_times = 0
        global case_flag
        case_flag = False

        #start to auto-trigger MT call
        mt_trigger_service_call(slot1_number, no_answer_wait_time, hold_time, interval_time, call_repeat_times, True)

        #sleep(2)

        for i in range(0,call_repeat_times):
            sleep(3)

            func = lambda:search_view_by_id("incomingCallWidget")
            if wait_for_fun(func, True, interval_time):
                #answer the phone
                drag_by_param(50,75,100,50,10)
                #reject the phone
                #drag_by_param(50,75,10,75,10)

                sleep(2)
                phone_time = lambda:search_text("00:")
                wait_for_fun(phone_time,True,5)
                sleep(hold_time)

                success_times = success_times + 1

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