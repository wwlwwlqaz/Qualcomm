import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    make 100 times calls to check whether is connected successfully or not.
#precondition:
#    the network normal
#steps:
#    1. open the Phone program or open the dial pad interface; (non-smart phones no such step can be omitted)
#    2. enter a phone number and dial.
#    3. confirm it's connected and wait 5 seconds before end the call.
#    4. return idel interface.
############################################

class test_suit_cmcc_mtbf_case2(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case2 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case2"
        cmccMTBF.launch_app_by_name("phone")

        success_times = 0
        global case_flag
        case_flag = False
        define_case_success_times = 95

        for i in range(0,100):
            sleep(1)
            #go to Dial Activity.
            drag_by_param(0,50,100,50,10)
            drag_by_param(0,50,100,50,10)

            phoneNumber = SC.PRIVATE_CMCC_MTBF_DIAL_NUMBER

            #MO
            #dial number
            #call
            #make sure whether get though
            phoneOn = cmccMTBF.phone_phone_call(phoneNumber)

            if phoneOn:
                sleep(5)
                success_times = success_times + 1
                if search_view_by_id("endButton"):
                    click_button_by_id("endButton")

        if(success_times < define_case_success_times):
            case_flag = False
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'make calls failure: success time -- ' + str(success_times), logging_wrapper.SEVERITY_HIGH)
        else:
            case_flag = True
            qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'make calls success: success times -- ' + str(success_times), logging_wrapper.SEVERITY_HIGH)

        