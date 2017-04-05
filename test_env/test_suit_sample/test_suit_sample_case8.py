#coding=utf-8
import fs_wrapper
import settings.common as SC
from qrd_shared.case import *
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from thrift_gen_qsstservice.GroupTest.constants import *
from settings import common

expected_group_member = 3
group_name = 'test_group_1'
role_name_A = 'A'
role_name_B = 'B'
role_name_C = 'C'
action_send_sms = "send sms"
action_end_call = "end call"

class test_suit_sample_case8(TestCaseBase):
    '''
    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_grouptest_case1"
    def test_case_main(self, case_results):
        #(DEVICE_NAME_KEY,SLOT1_PHONE_NUMBER_KEY,ACT_AS_HOST_KEY,ROLE_NAME_KEY,GROUP_NAME_KEY)
        deviceInformation = dict()
        deviceName = get_serial_number()
        deviceInformation[DEVICE_NAME_KEY] = deviceName
        deviceInformation[ACT_AS_HOST_KEY] = str(common.PUBLIC_ACT_AS_GROUP_TEST_HOST)
        deviceInformation[GROUP_NAME_KEY] = group_name
        deviceInformation[ROLE_NAME_KEY] = ' '
        deviceInformation[SLOT1_PHONE_NUMBER_KEY] = common.PUBLIC_SLOT1_PHONE_NUMBER
        try:
            init_group_database()
            attend_group(deviceInformation)
            wait_for_group_members(expected_group_member,group_name,deviceInformation[ACT_AS_HOST_KEY])
            if(common.PUBLIC_ACT_AS_GROUP_TEST_HOST == True):
                set_role_name(deviceName,role_name_A)
                set_status(STATUS_READY_VALUE,deviceName)
                #assign the roles
                members = get_group_members(group_name)
                log_test_framework(self.TAG, "get_group_members:" +str(members))
                roleArray = [role_name_B,role_name_C]
                i = 0
                for member in members:
                    if(cmp(member[ACT_AS_HOST_KEY],'True')!=0):
                        set_role_name(member[DEVICE_NAME_KEY],roleArray[i])
                        i+=1
                log_test_framework(self.TAG, "assign roles finished")
                #wait for all members ready
                wait_for_members_ready(expected_group_member,group_name)
                log_test_framework(self.TAG, "all members are ready")
                #call B
                phoneNumberB = get_slot1_number_by_role_name(role_name_B,group_name)
                launcher.launch_from_launcher('phone')
                #go to Dial Activity.
                drag_by_param(0,50,100,50,10)
                drag_by_param(0,50,100,50,10)
                phone.phone_call(phoneNumberB, "", 2)
                sleep(20)
                deliver_action_by_role_name(action_send_sms,role_name_C,group_name)
                sleep(60)
                deliver_action_by_role_name(action_end_call,role_name_B,group_name)
                set_status(STATUS_FINISHED_VALUE,deviceName)
                wait_for_members_finished(expected_group_member,group_name);
                resultB = get_test_result_by_role_name(role_name_B,group_name)
                resultC = get_test_result_by_role_name(role_name_C,group_name)
                if( (cmp(resultB,RESULT_SUCCESS_VALUE)==0)and(cmp(resultC,RESULT_SUCCESS_VALUE)==0) ):
                    destroy_group(group_name)
                    return True
                else:
                    destroy_group(group_name)
                    return False

            else:
                roleName = wait_for_role_name(deviceName)
                if(cmp(roleName,role_name_B)==0):
                    set_status(STATUS_READY_VALUE,deviceName)
                    log_test_framework(self.TAG, "B is ready")
                    func = lambda:search_view_by_id("incomingCallWidget")
                    if wait_for_fun(func, True, 500000):
                        #answer the phone
                        drag_by_param(50,75,100,50,10)
                        sleep(2)
                        phone_time = lambda:search_text("00:")
                        wait_for_fun(phone_time,True,5)
                        sleep(3)
                        wait_for_action(deviceName)
                        action = consume_one_action(deviceName)
                        if(cmp(action,action_end_call)==0):
                            if search_view_by_id("endButton"):
                                click_button_by_id("endButton")
                                set_test_result(RESULT_SUCCESS_VALUE,deviceName)
                                set_status(STATUS_FINISHED_VALUE,deviceName)
                            else:
                                set_test_result(RESULT_FAILURE_VALUE,deviceName)
                                set_status(STATUS_FINISHED_VALUE,deviceName)
                                wait_for_group_destroyed(group_name)
                                return False
                        else:
                            set_test_result(RESULT_FAILURE_VALUE,deviceName)
                            set_status(STATUS_FINISHED_VALUE,deviceName)
                            wait_for_group_destroyed(group_name)
                            return False

                if(cmp(roleName,role_name_C)==0):
                    set_status(STATUS_READY_VALUE,deviceName)
                    log_test_framework(self.TAG, "C is ready")
                    wait_for_action(deviceName)
                    action = consume_one_action(deviceName)
                    if(cmp(action,action_send_sms)==0):
                        phoneNumberA = get_slot1_number_by_role_name(role_name_A,group_name)
                        launcher.launch_from_launcher('mms')
                        try:
                            mms.send_sms(3, phoneNumberA, 'TestMessage')
                        except Exception, tx:
                            log_test_framework(self.TAG, "send_sms exception is "+str(tx))

                        set_test_result(RESULT_SUCCESS_VALUE,deviceName)
                        set_status(STATUS_FINISHED_VALUE,deviceName)
                    else:
                        set_test_result(RESULT_FAILURE_VALUE,deviceName)
                        set_status(STATUS_FINISHED_VALUE,deviceName)
                        wait_for_group_destroyed(group_name)
                        return False

        except Exception, tx:
            set_status(STATUS_FINISHED_VALUE,deviceName)
            log_test_framework(self.TAG, "exception is "+str(tx))

        wait_for_group_destroyed(group_name)
        return True
