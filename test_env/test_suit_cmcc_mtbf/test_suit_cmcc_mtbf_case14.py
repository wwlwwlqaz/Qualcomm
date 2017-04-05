import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case14(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case14 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        TAG = "test_suit_cmcc_mtbf_case14"
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'call brower 14')
        cmccMTBF.launch_app_by_name("browser")
        download_address_audiofile = 'http://121.35.242.200/WEBFILE/News/4/20080919124207_12157_1229046.wma'
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'download_address_audiofile :  ' + download_address_audiofile)
        case_flag = cmccMTBF.download_url_browser(download_address_audiofile, 3)
        if case_flag :
            qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'Download the audio file and open success', logging_wrapper.SEVERITY_HIGH)
