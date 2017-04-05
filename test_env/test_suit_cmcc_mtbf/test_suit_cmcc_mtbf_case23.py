#coding=utf-8
'''
   Open the music player, play music, turn off the music player.


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

class test_suit_cmcc_mtbf_case23(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case23 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_cmcc_mtbf_case23"

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        cmccMTBF.launch_app_by_name("music_player")
        click_textview_by_text(cmccMTBF.get_value('music_songs'))
        #select two songs to play for more than five seconds
        click_in_list_by_index(0)
        #check whether the play is started
        if not is_view_enabled_by_id(VIEW_BUTTON,'pause'):
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, "player start failed.", logging_wrapper.SEVERITY_HIGH)
            return False
        #wait the player to play a song for more than 5 seconds
        sleep(6)
        #click the pause button to stop the player
        click_button_by_id('pause')
        goback()
        click_in_list_by_index(1)
        if not is_view_enabled_by_id(VIEW_BUTTON,'pause'):
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, "player start failed.", logging_wrapper.SEVERITY_HIGH)
            return False
        sleep(6)
        click_button_by_id('pause')
        goback()
        goback()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, "success.", logging_wrapper.SEVERITY_HIGH)
        return True