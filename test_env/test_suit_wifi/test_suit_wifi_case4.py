#coding=utf-8
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import test_suit_wifi

class test_suit_wifi_case4(TestCaseBase):
    def test_case_main(self, case_results):
        print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR])
        sleep(1)

        if not settings.is_wifi_connected(SC.PRIVATE_WIFI_HYDRA_SSID):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'WIFI not connected')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            set_cannot_continue()

        #play streaming music
        launcher.launch_from_launcher('browser')
        #clear the browser cache
        click_menuitem_by_text(browser.get_value("menu_preferences"))
        click_textview_by_text(browser.get_value("pref_privacy_security_title"))
        click_textview_by_text(browser.get_value("pref_privacy_clear_cache"))

        if search_text(browser.get_value("dialog_ok_button")):
            click_button_by_text(browser.get_value("dialog_ok_button"))

        goback()
        goback()

        #addressing config web address
        click_textview_by_id("url")
        send_key(KEY_DEL)
        #input address url "douban.fm/radio"
        ime.IME_input_english(1,"douban.fm","p")
        ime.IME_input(1,['num_sign','sign_8','num_sign'],input_type="p")
        ime.IME_input_english(1,"radio")
        sleep(30)

        #check connected
        scroll_down()
        if search_view_by_id("favicon"):
            click_button_by_id("favicon")
        sleep(2)
        if not search_text(unicode("豆瓣")):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'cannot play streaming audio')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '\tfail')
            local_assert(True,False)
        goback()
        goback()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def test_case_end(self):
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'end')
