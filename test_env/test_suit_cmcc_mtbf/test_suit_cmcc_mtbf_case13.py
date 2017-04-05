#coding=utf-8
import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, save_fail_log, print_report_line
import logging_wrapper

class test_suit_cmcc_mtbf_case13(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case13 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        TAG = "test_suit_cmcc_mtbf_case13"
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'call brower 13')
        cmccMTBF.launch_app_by_name("browser")
        download_address_txtfile = 'http://218.206.177.209:8080/waptest/fileDownLoad?file=Text&groupname=11&fenzu=WAP2.0'
#Cer_MTBF_13   ����      http://218.206.177.209:8080/waptest/fileDownLoad?file=Text&groupname=11&fenzu=WAP2.0
#Cer_MTBF_14   ����      http://218.206.177.209:8080/waptest/fileDownLoad?file=mp3&groupname=11&fenzu=WAP2.0
#Cer_MTBF_15   ����      http://218.206.177.209:8080/waptest/fileDownLoad?file=Picture&groupname=11&fenzu=WAP2.0
#Cer_MTBF_16   ����      http://218.206.177.209:8080/waptest/fileDownLoad?file=Video&groupname=11&fenzu=WAP2.0

        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'download_address_txtfile :  ' + download_address_txtfile)
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'download_address_txtfile:  ' + download_address_txtfile)
        case_flag = cmccMTBF.download_url_browser(download_address_txtfile, 3)
        if case_flag :
            qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'Download the text file and open success', logging_wrapper.SEVERITY_HIGH)

