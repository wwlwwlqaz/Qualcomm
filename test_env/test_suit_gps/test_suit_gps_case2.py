import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_gps_case2(TestCaseBase):
    def test_case_main(self, case_results):
        case_flag = False
        settings.whether_open_gps(True)

        launcher.launch_from_launcher('qualcomm_dlt')
        click_menuitem_by_text("Options")
        click_textview_by_text("Edit Config")
        click_textview_by_text("Fix Param Settings")
        click_textview_by_text("Number of Fixes")
        clear_edittext_by_index(0)

        ime.IME_input_number(1,SC.PUBLIC_GPS_FIX_NUMBER,'c-n')
        click_button_by_index(0)
        goback()
        goback()
        goback()
        register_update_watcher("com.qualcomm.qct.dlt",VIEW_BUTTON,ID_TYPE_ID,"button1",ACTION_CLICK)
        click_button_by_id("main_start_button")
        click_textview_by_text('Signal Graph', searchFlag = TEXT_CONTAINS)

        sleep(60)

        click_textview_by_text('Pos Info', searchFlag = TEXT_CONTAINS)

        fun = lambda:search_text("Min/Max/Avg/Med TTF:",isScrollable = 0, searchFlag = TEXT_CONTAINS)
        if wait_for_fun(fun,True,5):
            case_flag = True
        sleep(2)
        goback()
        if not case_flag:
            click_button_by_index(0)
        goback()

        unregister_update_watcher("com.qualcomm.qct.dlt")
        if not case_flag:
            set_cannot_continue()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))