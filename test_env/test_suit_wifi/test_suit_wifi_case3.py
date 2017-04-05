#coding=utf-8
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import test_suit_wifi

class test_suit_wifi_case3(TestCaseBase):
    def test_case_main(self, case_results):
        print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR])

        sleep(1)

        if not settings.is_wifi_connected(SC.PRIVATE_WIFI_HYDRA_SSID):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'WIFI not connected')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            set_cannot_continue()

        #start to auto-trigger MT call
        #TriggerMTCall(xxx)
        #timeout is 1 min, checking whether MT happened

        #if not search_view_by_id("incomingCallWidget"):
        #    log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'No incoming call')
        #    print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
        #    set_cannot_continue()
        #reject the phone
        #drag_by_param(50,75,10,75,10)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def test_case_end(self):
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'end')
