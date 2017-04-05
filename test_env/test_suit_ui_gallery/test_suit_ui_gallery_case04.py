#coding=utf-8

import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import fs_wrapper
from case_utility import *
from utility_wrapper import *

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#    delete a picture in gallery
#precondition:
############################################
import os,re,subprocess,shlex
from test_suit_ui_gallery import *
import test_suit_ui_file_explorer.test_suit_ui_file_explorer as suit_FE


class test_suit_ui_gallery_case04(TestCaseBase):
    tag = 'ui_gallery_case04'
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: before operation, record the photo number
        #
        work_dir = '/sdcard/DCIM/Camera'
        num1 = suit_FE.preprocess(self.tag,work_dir,floor=1)
        log_test_case(self.tag, "num1 = "+str(num1))
        
        
        
        #
        # STEP 2: DELETE photo in gallery
        #
        N_album = len(ALBUM_LOCATION)
        n = 0
        func = lambda:search_view_by_id('up')
        while(n<N_album):   # click album
            click(ALBUM_LOCATION[n][0],ALBUM_LOCATION[n][1])
            if wait_for_fun(func,flag = True,timeout = 3):  # now click photo
                if is_view_enabled_by_text(VIEW_TEXT_VIEW,'Grid view',isScrollable=0):
                    click_textview_by_text('Grid view')
                    click_textview_by_text('Filmstrip view')
                '''
                w_rate = getDisplayWidth()/1080
                h_rate = getDisplayHeight()/1920
                click(550*w_rate,942*h_rate)
                '''
                break
            n += 1

        if n<N_album:
            pass
        elif n==N_album:
            set_cannot_continue()
            log_test_case(self.tag, "WRONG: cannot find album")
        else:
            set_cannot_continue()
            log_test_case(self.tag,"WRONG: what happened? why n>N_album??")
            
        
        #
        # STEP 3: after DELETE
        #
        if can_continue():
            click_menuitem_by_text('Delete')
            click_button_by_text('OK',isScrollable=0,waitForView=1)
            
            num2 = suit_FE.num_of_filetype_in_folder(work_dir,'.jpg')
            log_test_case(self.tag, "num2 = "+str(num2))
            if num2==num1-1:
                case_flag = True
            
                
        
        #
        #  STEP 5: exit
        #
        exit_cur_case(self.tag)        
        
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "delete photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))