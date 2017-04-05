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
#    modify a picture in gallery
#precondition:
#    have 1 photo in gallery at least
############################################
import os,re,datetime
from test_suit_ui_gallery import *
import test_suit_ui_file_explorer.test_suit_ui_file_explorer as suit_FE


photo_info_index = {'Title':1,'Time':2, }

class test_suit_ui_gallery_case05(TestCaseBase):
    tag = 'ui_gallery_case05'
    def test_case_main(self, case_results):
        case_flag = False
        
        work_dir = '/sdcard/DCIM/Camera'
        suit_FE.preprocess(self.tag,work_dir,floor=1)
        
        #
        # STEP 1: choose a photo to modify
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
        # STEP:
        #
        if can_continue():
            (title1,time1) = get_current_pic_details()
            log_test_case(self.tag,'old title:%s\t time:%s'%(title1,time1))
            
            
            click_menuitem_by_text('Edit',waitForView=1)
           # click_button_by_id('photopage_bottom_control_edit',waitForView=1)
            click_imageview_by_id('geometryButton',waitForView=1)
            click_view_by_container_id('category_panel_container','android.view.View',4)
            click_button_by_id('draw_color_button01')
            drag_by_param(startX = random.randint(1,99), startY = random.randint(25,75), endX = random.randint(1,99), endY = random.randint(25,75), stepCount = 2)
            sleep(2)
                #drag_by_param(startX = random.randint(1,99), startY = random.randint(1,99), endX = random.randint(1,99), endY = random.randint(1,99), stepCount = 2)
                #sleep(2)
            click_button_by_id('applyFilter',waitForView=1)
            click_textview_by_text('Save',waitForView=1)
            
            
            (title2,time2) = get_current_pic_details()
            log_test_case(self.tag,'new title:%s\t time:%s'%(title2,time2))


            # check if time is change
            if time2 != time1:
                case_flag = True
        
        #
        # STEP 4: exit
        #
        exit_cur_case(self.tag)


        
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "modify photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))