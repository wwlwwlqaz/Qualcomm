import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case18(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case18 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case18"
        #Login Google account
        sleep(5)
        start_activity('com.android.settings','.Settings')
        scroll_to_bottom()
        local_assert(cmccMTBF.calendar_add_google_account(SC.PRIVATE_GMAIL_GMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_GMAIL_GMAIL_PASSWORD_SEQUENCE),True)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        #open calendar
        cmccMTBF.launch_app_by_name("calendar")
        #delete event
        cmccMTBF.calendar_delete_calendar_event()
        i = 0
        for i in range(0,5):
            #new an event
            sleep(1)
            click(300,300)
            sleep(2)
            click(300,300)
            entertext_edittext_by_id('title','meeting')
            click_textview_by_text(cmccMTBF.getValByCurRunTarget("calendar_done"))
            #delete event
            cmccMTBF.calendar_delete_calendar_event()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "Add and remove event success.", logging_wrapper.SEVERITY_HIGH)
        return True
