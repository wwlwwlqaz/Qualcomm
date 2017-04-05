#coding=utf-8
'''
   Open file manager, delete all files, confirm the deletion, exit.


   @author: U{huchenpeng<chenpenghu@cienet.com.cn>}
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
from case_utility import *
from test_case_base import TestCaseBase
from qrd_shared.case import *
import logging_wrapper

class test_suit_cmcc_mtbf_case17(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case17 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_cmcc_mtbf_case17"

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        #enter Download directory
        cmccMTBF.launch_app_by_name("file_explorer")
        click_textview_by_text(cmccMTBF.get_value('file_explorer_folder'))
        click_textview_by_text(cmccMTBF.get_value('file_explorer_phone_storage'))
        click_textview_by_text(cmccMTBF.get_value('file_explorer_download_folder'))
        #enter delete mode
        while cmccMTBF.file_explorer_check_file_exist():
            cmccMTBF.file_explorer_delete_file()
        if not  cmccMTBF.file_explorer_check_file_exist():
            qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "success.", logging_wrapper.SEVERITY_HIGH)
            return True
        qsst_log_case_status(logging_wrapper.STATUS_FAILED, "Delete all files failed.", logging_wrapper.SEVERITY_HIGH)
        return False
