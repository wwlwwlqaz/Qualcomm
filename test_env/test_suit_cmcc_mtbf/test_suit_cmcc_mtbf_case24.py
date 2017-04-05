#coding=utf-8
'''
   Create and delete a folder in the file manager.


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

class test_suit_cmcc_mtbf_case24(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case24 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_cmcc_mtbf_case24"
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        cmccMTBF.launch_app_by_name("file_explorer")
        #enter the folder view and choose Phone storage, it is specified on 8x26
        click_textview_by_text(cmccMTBF.get_value('file_explorer_folder'))
        click_textview_by_text(cmccMTBF.get_value('file_explorer_phone_storage'))
        #create a folder named with '010'
        send_key(KEY_MENU)
        click_textview_by_text(cmccMTBF.get_value('file_explorer_new_folder'))
        entertext_edittext_on_focused('010')
        click_button_by_text(cmccMTBF.get_value('file_explorer_confirm'))
        #wait for the dialog to disappear
        sleep(5)
        #check whether the 010 folder exists
        if not is_view_enabled_by_text(VIEW_TEXT_VIEW,'010'):
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, "creating a folder named with 010 is failed", logging_wrapper.SEVERITY_HIGH)
            return False
        #delete the '010' folder
        send_key(KEY_MENU)
        click_textview_by_text(cmccMTBF.get_value('file_explorer_delete'))
        click_textview_by_text('010')
        click_button_by_text(cmccMTBF.get_value('file_explorer_ok'))
        click_button_by_text(cmccMTBF.get_value('file_explorer_confirm'))
        sleep(5)
        #check whether the deletion succeeds
        if is_view_enabled_by_text(VIEW_TEXT_VIEW,'010'):
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, "deleting a folder named with 010 is failed", logging_wrapper.SEVERITY_HIGH)
            return False
        #exit file explorer
        goback()
        goback()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "success.", logging_wrapper.SEVERITY_HIGH)
        return True