#coding=utf-8
import fs_wrapper
import settings.common as SC
from qrd_shared.case import *
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from thrift_gen_qsstservice.GroupTest.constants import *
from settings import common
import test_suit_ui_message.test_suit_ui_message as uiMessage
import test_suit_grouptest as GT

expected_group_member = 2
group_name = 'group_sms_send_receive'
role_name_A = 'A'
role_name_B = 'B'
action_read_sms = "read sms"

class test_suit_grouptest_case02(TestCaseBase):
    '''
    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_grouptest_case02"
    def test_case_main(self, case_results):
        log_test_case(self.TAG, 'start')
        #(DEVICE_NAME_KEY,SLOT1_PHONE_NUMBER_KEY,ACT_AS_HOST_KEY,ROLE_NAME_KEY,GROUP_NAME_KEY)
        deviceInformation = dict()
        GT.deleteOldSerialNumber()
        deviceName = get_serial_number()
        deviceInformation[DEVICE_NAME_KEY] = deviceName
        deviceInformation[ACT_AS_HOST_KEY] = str(common.PUBLIC_ACT_AS_GROUP_TEST_HOST)
        deviceInformation[GROUP_NAME_KEY] = group_name
        deviceInformation[ROLE_NAME_KEY] = ' '
        deviceInformation[SLOT1_PHONE_NUMBER_KEY] = common.PUBLIC_SLOT1_PHONE_NUMBER
        log_test_case('deviceInformation', 'end')
        try:
            init_group_database()
            attend_group(deviceInformation)
            log_test_case('attend_group()', 'end')
            wait_for_group_members(expected_group_member,group_name,deviceInformation[ACT_AS_HOST_KEY])
            log_test_case('wait_for_group_members()', 'end')
            
            if(common.PUBLIC_ACT_AS_GROUP_TEST_HOST == True):
                log_test_case('HOST', 'start')
                set_role_name(deviceName,role_name_A)
                set_status(STATUS_READY_VALUE,deviceName)
                #assign the roles
                members = get_group_members(group_name)
                log_test_framework(self.TAG, "get_group_members:" +str(members))
                roleArray = [role_name_B]
                i = 0
                for member in members:
                    if(cmp(member[ACT_AS_HOST_KEY],'True')!=0):
                        set_role_name(member[DEVICE_NAME_KEY],roleArray[i])
                        i+=1
                log_test_framework(self.TAG, "assign roles finished")
                #wait for all members ready
                wait_for_members_ready(expected_group_member,group_name)
                log_test_framework(self.TAG, "all members are ready")
                
                #send sms to B
                log_test_case('HOST', 'send sms start')
                phoneNumberB = get_slot1_number_by_role_name(role_name_B,group_name)
                log_test_case('slot1 number in phone B',phoneNumberB)
                content = 'This is group test, send sms'
                log_test_case('send mms','start')
                send_mms(phoneNumberB, content)
                log_test_case('send mms','end')

                sleep(20)
                log_test_case('HOST', 'deliver action to B')
                deliver_action_by_role_name(action_read_sms,group_name)

                set_status(STATUS_FINISHED_VALUE,deviceName)
                wait_for_members_finished(expected_group_member,group_name);
                log_test_case('HOST', 'wait_for_members_finished() finished')
                resultB = get_test_result_by_role_name(role_name_B,group_name)
                if( cmp(resultB,RESULT_SUCCESS_VALUE)==0 ):
                    destroy_group(group_name)
                    return True
                else:
                    destroy_group(group_name)
                    return False

            else:# here is slave B' code
                log_test_case('SLAVE', 'start')
                roleName = wait_for_role_name(deviceName)
                if(cmp(roleName,role_name_B)==0):
                    set_status(STATUS_READY_VALUE,deviceName)
                    log_test_case('SLAVE', "B is ready")
                    launcher.launch_from_launcher('mms')
                    num1 = uiMessage.get_unread_number()
                    func = lambda:uiMessage.get_unread_number()>num1
                    if wait_for_fun(func, True, 500000):
                        #read the message
                        phoneNumberA = get_slot1_number_by_role_name(role_name_A,group_name)
                        content = 'This is group test, send sms'
                        log_test_case('Host phoneNumber',phoneNumberA)
                        if uiMessage.msg_exist(phoneNumberA,content) is True:
                            set_test_result(RESULT_SUCCESS_VALUE,deviceName)
                            set_status(STATUS_FINISHED_VALUE,deviceName)
                
                set_test_result(RESULT_FAILURE_VALUE,deviceName)
                set_status(STATUS_FINISHED_VALUE,deviceName)
                wait_for_group_destroyed(group_name)
                return False


        except Exception, tx:
            set_status(STATUS_FINISHED_VALUE,deviceName)
            log_test_framework(self.TAG, "exception is "+str(tx))

        wait_for_group_destroyed(group_name)
        return True
