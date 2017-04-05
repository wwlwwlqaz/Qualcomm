import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case21(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case18 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case21"
        #delete sound audio 
        cmccMTBF.launch_app_by_name("file_explorer")
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("record_folder"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("sd_card"))
        sleep(2)
        while search_text('.amr', searchFlag=TEXT_CONTAINS):
            click_textview_by_text('.amr', searchFlag=TEXT_CONTAINS, clickType=LONG_CLICK)
            click_button_by_text(cmccMTBF.getValByCurRunTarget("record_delete"))
            click_button_by_text(cmccMTBF.getValByCurRunTarget("record_ok"))
        goback()
        goback()
        #open calendar
        cmccMTBF.launch_app_by_name("record")
        #save record
        click_button_by_id('recordButton')
        sleep(5)
        click_button_by_id('stopButton')
        click_button_by_text(cmccMTBF.getValByCurRunTarget("record_done"))
        click_button_by_text(cmccMTBF.getValByCurRunTarget("record_ok"))
        goback()
        #play sound record
        cmccMTBF.launch_app_by_name("music_player")
        click_button_by_id('playlisttab')
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("music_your_recordings"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("music_your_recordings"))
        goback()
        goback()
        goback()
        goback()
        #delete sound audio 
        cmccMTBF.launch_app_by_name("file_explorer")
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("record_folder"))
        click_textview_by_text(cmccMTBF.getValByCurRunTarget("sd_card"))
        sleep(2)
        while search_text('.amr', searchFlag=TEXT_CONTAINS):
            click_textview_by_text('.amr', searchFlag=TEXT_CONTAINS, clickType=LONG_CLICK)
            click_button_by_text(cmccMTBF.getValByCurRunTarget("record_delete"))
            click_button_by_text(cmccMTBF.getValByCurRunTarget("record_ok"))
        goback()
        goback()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "Record , open and delete the audio file success.", logging_wrapper.SEVERITY_HIGH)
        return True