import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case22(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case18 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case22"
        #open browser
        cmccMTBF.launch_app_by_name("browser")
        #delete cache & history & cookie data
        click_menuitem_by_text(cmccMTBF.getValByCurRunTarget("browser_settings"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_Privacy"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_clear_cache"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_ok"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_clear_history"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_ok"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_clear_cookie"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("browser_ok"))
        goback() 
        sleep(1)
        goback()
        sleep(1)
        goback()
        i = 0
        for i in range(0,2):
            #open baidu
            cmccMTBF.launch_app_by_name("browser")
            click_textview_by_id('url')
            entertext_edittext_by_id('url','www.youku.com')
            sleep(2)
            send_key(KEY_ENTER)
            sleep(15)
            click(400,600)
            sleep(10)
            click(400,600)
            sleep(15)
            cmccMTBF.browser_exit_browser()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "Open Sina success.", logging_wrapper.SEVERITY_HIGH)
        return True
