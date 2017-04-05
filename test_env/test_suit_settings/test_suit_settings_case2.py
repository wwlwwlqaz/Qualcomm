'''
   this case test local update function.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{TestCaseBase <TestCaseBase>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import fs_wrapper
import settings.common as SC
from qrd_shared.case import *
from case_utility import *
from utility_wrapper import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase

class test_suit_settings_case2(TestCaseBase):
    '''
    test_suit_settings_case2 is a class for settings case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        reboot = get_reboot_status("test_suit_settings", "test_suit_settings_case2")
        if not reboot:
            click_textview_by_text(settings.get_value("about_phone"))
            click_textview_by_text(settings.get_value("system_update"))
            click_textview_by_text(settings.get_value("local_updates"))
            click_textview_by_text("update_for_autotest")
            save_reboot_status("test_suit_settings","test_suit_settings_case2")
            click_textview_by_id("button1")
            pause_python_process()
        else:
            restore_reboot_status()
            settings.whether_open_gps(True)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

