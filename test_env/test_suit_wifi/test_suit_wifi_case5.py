#coding=utf-8
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import test_suit_wifi

class test_suit_wifi_case5(TestCaseBase):
    def test_case_main(self, case_results):
        print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR])

        sleep(1)

        if not settings.is_wifi_connected(SC.PRIVATE_WIFI_HYDRA_SSID):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'WIFI not connected')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            set_cannot_continue()

        #party APK for streaming video
        launcher.launch_from_launcher('youku')
        sleep(10)
        if search_view_by_id("moon1"):
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            sleep(3)
            if search_text(unicode("是否要在桌面创建快捷方式")):
                click_button_by_text(unicode('否'))

        if not search_view_by_id("scrollContainer"):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'cannot play video')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            set_cannot_continue()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))


    def test_case_end(self):
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'end')
