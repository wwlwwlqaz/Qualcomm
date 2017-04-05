#coding=utf-8
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import test_suit_wifi

class test_suit_wifi_case1(TestCaseBase):
    def test_case_main(self, case_results):
        print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR])

        sleep(1)

        settings.whether_open_mobile_data(False)
        settings.disable_wifi()
        sleep(1)

        click_textview_by_text(settings.get_value("wifi"))
        if search_text(settings.get_value("see_available_networks")):
            click_button_by_index(0)
        sleep(20)

        click_textview_by_text(SC.PRIVATE_WIFI_HYDRA_SSID)

        if search_text(settings.get_value("connected")):
            goback()
        elif search_text(settings.get_value("forget")):
            click_button_by_text(settings.get_value("connect"))
        else:
            #entertext_edittext_by_index(0, "K5x48Vz3")
            ime.IME_input(1,SC.PRIVATE_WIFI_HYDRA_PASSWORD_SEQUENCE)
            sleep(1)
            click_button_by_text(settings.get_value("connect"))
        sleep(20)

        #check display
        click_textview_by_text(SC.PRIVATE_WIFI_HYDRA_SSID)
        if not search_text(settings.get_value("connected")):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'WIFI is not connected')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            set_cannot_continue()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def test_case_end(self):
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'end')
