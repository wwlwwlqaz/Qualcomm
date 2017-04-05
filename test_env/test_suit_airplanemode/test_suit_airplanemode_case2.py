'''
    file level operations airplane mode on/off/emergency etc. test:

    1.Long press power key->turn on "Airplane mode".
    2.Long press power key->turn off "Airplane mode"
    3.Turn Airplane mode on..MO emergency call to check response..Emergency call can be MO successfully;

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @see: L{test_loader <test_loader>}
    @see: L{test_case_base<test_case_base>}
    @see: L{test_suit_base<test_suit_base>}

    @note:
    @attention: should be merged have done by others
        Airplane mode can be turn off successfully and both SLOT1&SLOT, signals can restore after ending the call.
        1.Airplane mode can be turned on successfully and have plane icon on SLOT1&SLOT2 signal icon.
        2.The voice call and data call cannot be made.
        3.Airplane mode can be tured off successfully and the Two SIM cards can be registered to the right networks.
        4.The voice call and data call can be made successfully."

    @bug:
    @warning:
    @todo:
        1. Airplane mode is on.
        2. Power off the phone.
        3. Power on the phone and deactivate the Airplane mode(By settings and power key)"

'''
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_airplanemode_case2(TestCaseBase):

    def IS_AirplaneMode_on(self):
        """
        This function get the airplan mode.
        @rtype: boolean
        @return:  True -airplan mode on, False-airplan mode off
        """

        send_key(KEYCODE_POWER, LONG_PRESS)
        if search_text(notificationBar.get_value('airplanemodeon')):
            goback()
            return True
        else:
            goback()
            return False

    def AirplaneMode_turnoff(self):
        """
        This function set the airplan mode off.
        @return:  none
        """

        send_key(KEYCODE_POWER, LONG_PRESS)
        if search_text(notificationBar.get_value('airplanemodeon')):
            click_textview_by_text(notificationBar.get_value('airplanemode'))
        goback()
        return
        #notificationBar.drag_down()

    def AirplaneMode_turnon(self):
        """
        This function set the airplan mode on.
        @return:  none
        """

        send_key(KEYCODE_POWER, LONG_PRESS)
        if search_text(notificationBar.get_value('airplanemodeoff')):
            click_textview_by_text(notificationBar.get_value('airplanemode'))
        goback()
        return



    def emergency_call(self,emergency_number):
        """
        This function make call emergency call
        @type  emergency_number: number
        @param emergency_number: for example 911,112
        @return:  none
        """

        start_activity('com.android.contacts','.activities.DialtactsActivity')
        drag_by_param(0, 50, 100, 50, 10)
        drag_by_param(0, 50, 100, 50, 10)

        phone.dial(emergency_number)
        sleep(3)
        phoneOn = True

        case_flag = False
        if phoneOn:
            if search_view_by_id("endButton") :
                if is_cdma():
                    sleep(5)
                    if search_text("00:"):
                        case_flag = True
                else:
                    case_flag = True
        if case_flag :
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'success emergency_call')
            click_button_by_id("endButton")
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'fail emergency_call')

    def test_case_main(self, case_results):
        """
        This function entry for airplan mode function test
        @return:  none
        """

        self.AirplaneMode_turnon()
        self.emergency_call('112')

        if (self.IS_AirplaneMode_on()):
            self.AirplaneMode_turnoff()
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'after emergency call, airplane mode turn off')
        #self.emergency_call('112')

