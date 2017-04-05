import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case20(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case18 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case20"
        #open alarm
        cmccMTBF.launch_app_by_name("clock")
        click_button_by_id('alarms_button')
        #delete alarms
        while search_view_by_id('alarm_item') == True:
            click_button_by_id('timeDisplayMinutes',clickType=LONG_CLICK)
            click_textview_by_desc(cmccMTBF.getValByCurRunTarget("alarm_delete_alarm"))
            click_textview_by_text(cmccMTBF.getValByCurRunTarget("calendar_ok"))
        i = 0
        for i in range(0,5):
            #add alarms
            click_button_by_id('menu_item_add_alarm')
            if search_view_by_id('cancel_button') == True:
                click_button_by_id('cancel_button')
            else:
                sleep(1)
            #delete alarms
            while search_view_by_id('alarm_item') == True:
                click_button_by_id('timeDisplayMinutes',clickType=LONG_CLICK)
                click_textview_by_desc(cmccMTBF.getValByCurRunTarget("alarm_delete_alarm"))
                click_textview_by_text(cmccMTBF.getValByCurRunTarget("calendar_ok"))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "Add and remove alarm success.", logging_wrapper.SEVERITY_HIGH)
        return True
