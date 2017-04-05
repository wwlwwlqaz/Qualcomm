#coding=utf-8
'''
   Login doubanfm, switch channels,switch songs, collect songs.


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
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
import settings.common as SC
from test_case_base import TestCaseBase
from qrd_shared.case import * 
import time
############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    Login, switch channels,switch songs, collect songs
#steps:
#    Login
#    switch channels
#    switch songs
#    collect songs
#    exit
############################################

class test_suit_doubanfm_case1(TestCaseBase):
    '''
    test_suit_doubanfm_case1 is a class for doubanfm case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        sleep(2)

        start_time = time.time()
        while time.time() - start_time < 60:
            #remove guide info
            if search_view_by_id("close_guidance"):
                click_button_by_id("close_guidance",1,0)

            #remove use-3G info
            if search_text(doubanfm.get_value("3G_info"),1,0):
                click_button_by_text(doubanfm.get_value("go_on"),1,0)

            if search_view_by_id("settingButton"):
                break

        #Login
        if not search_text(doubanfm.get_value("settings"),1,0):
            click_button_by_id("settingButton",1,0)
        sleep(1)
        click_textview_by_text(doubanfm.get_value("settings"),1,0)

        if search_text(doubanfm.get_value("login"),1,0):
            click_button_by_id("accountButton",1,0)

            #input account *************
            click_textview_by_id("text_name",1,0)
            ime.IME_input(1,SC.PRIVATE_DOUBANFM_ACCOUNT_SEQUENCE)
            goback()

            #input password *************
            sleep(1)
            click_textview_by_id("text_password",1,0)
            ime.IME_input(1,SC.PRIVATE_DOUBANFM_PASSWORD_SEQUENCE)

            #click_button_by_id("button_login",1,0)
            sleep(2)

            #whether login successful
            InvokeFuncByCurRunTarget(self,"test_suit_doubanfm","test_suit_doubanfm_case1_adaptive","doubanfm")


        goback()

        #switch channels,songs, collect songs
        for i in range(1,2):
            #switch channels
            if i % 2 == 0 :
                drag_by_param(50,25,100,25,10)
            else:
                drag_by_param(50,25,0,25,10)
            sleep(3)

            #switch songs
            click_button_by_id("skipButton",1,0)
            sleep(1)

            start_time = time.time()
            while time.time() - start_time < 60 and search_view_by_id("pictureProgress"):
                sleep(1)

            #collect songs
            click_button_by_id("likeButton",1,0)
            sleep(3)

        #exit app
        click_button_by_id("settingButton",1,0)
        sleep(1)
        click_textview_by_text(doubanfm.get_value("exit"),1,0)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))