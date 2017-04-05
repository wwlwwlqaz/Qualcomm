import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case15(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case15 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case15"
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'call brower 15')
        cmccMTBF.launch_app_by_name("browser")
        download_address_picturefile = 'http://218.206.177.209:8080/waptest/fileDownLoad?file=Picture&groupname=11&fenzu=WAP2.0'
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'download_address_picturefile :  ' + download_address_picturefile)
        case_flag = cmccMTBF.download_url_browser(download_address_picturefile, 3)
        if case_flag :
            qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'Download the picture file and open success', logging_wrapper.SEVERITY_HIGH)
