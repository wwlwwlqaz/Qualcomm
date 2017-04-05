from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#     1.Home screen, long press blank space.
############################################

class test_suit_launcher_case3(TestCaseBase):
    def test_case_main(self,case_results):
        send_key(KEYCODE_POWER, LONG_PRESS)
        click_textview_by_text(launcher.get_value("power_off"))
        click_button_by_text(launcher.get_value("btn_ok"))
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
