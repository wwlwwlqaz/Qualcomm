import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_shieldbox_case2(TestCaseBase):
    def test_case_main(self, case_results):
        shieldbox.open_shield_box()
        # launcher.launch_from_launcher('phone')
        global case_flag
        for i in range(0, 2):
            case_flag = False

            drag_by_param(0, 50, 100, 50, 10)
            drag_by_param(0, 50, 100, 50, 10)
            # MO
            phoneOn = False
            if i == 0:
                phoneOn = phone.phone_call(SC.PUBLIC_SLOT1_DIAL_NUMBER, SC.PUBLIC_SMART_NUMBER, i)
            else:
                phoneOn = phone.phone_call(SC.PUBLIC_SLOT2_DIAL_NUMBER, "", i)

            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Before shield box close  phoneOn :' + str(phoneOn))

            if phoneOn:
                shieldbox.close_shield_box()
            else:
                if search_view_by_id("endButton"):
                    click_button_by_id("endButton")
                case_flag = False
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "cannot MO" + '\tfail ')
                return
            if not self.is_endcall():
                case_flag = False
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "cannot end call in 40 seconds" + '\tfail ')
                return
            shieldbox.open_shield_box()
            sleep(20)

            launcher.back_to_launcher()
            launcher.launch_from_launcher('phone')
            drag_by_param(0, 50, 100, 50, 10)
            drag_by_param(0, 50, 100, 50, 10)

            # MO
            phoneOn = False
            if i == 0:
                phoneOn = phone.phone_call(SC.PUBLIC_SLOT1_DIAL_NUMBER, SC.PUBLIC_SMART_NUMBER, i)
            else:
                phoneOn = phone.phone_call(SC.PUBLIC_SLOT2_DIAL_NUMBER, "", i)
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'After shield box close  phoneOn :' + str(phoneOn))
            if phoneOn:
                if search_view_by_id("endButton"):
                    click_button_by_id("endButton")
                case_flag = True
            else:
                case_flag = False
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR],"cannot MO after 20 seconds" + '\tfail')
                return
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def test_case_end(self):
        if not case_flag:
            set_cannot_continue()
        TestCaseBase.test_case_end(self)

    def is_endcall(self):
        t = 0
        while search_view_by_id("endButton") and t < 40:
            if search_text("00:"):
                is_end = True
                sleep(1)
            t = t + 1
        if is_end:
            return True
        else:
            return False
