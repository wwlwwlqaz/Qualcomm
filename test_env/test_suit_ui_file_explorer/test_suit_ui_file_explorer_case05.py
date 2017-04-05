#coding=utf-8

import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import fs_wrapper
from case_utility import *
import settings.common as SC
from utility_wrapper import *

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#    delete all items in FileExplorer
#precondition:
#    multiple 'QT..' items in path
#        or pictures in DCIM/Camera
#step:
#    1.goto FileExplorer; 
#            if not, goto step4
#    2.try to create a new folder; 
#            if not, goto step4
#    3.confirm whether new floder is created correctly;
#            if not, goto step4
#    4.exit to end case
############################################
import os,re,string,subprocess,shlex
from test_suit_ui_file_explorer import *
import test_suit_ui_gallery.test_suit_ui_gallery

class test_suit_ui_file_explorer_case05(TestCaseBase):
    tag = 'ui_file_explorer_case05'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 0: need some photo in work_dir for delete
        #
        
        #
        # STEP 1: goto work_dir in FileExplorer
        #
        work_dir = '/Phone storage/DCIM/Camera'
        number = preprocess(self.tag,work_dir,floor=3)
        goto_dir(work_dir,'Folder')
        
        #
        # STEP 2: choose an item to delete
        #
        try:
            #click_view_by_container_id('list','android.widget.TextView',0)
            click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
            click_button_by_id('selection_menu')
            if is_view_enabled_by_text(VIEW_TEXT_VIEW,'Select all',isScrollable=0):
                click_textview_by_text('Select all')
            elif is_view_enabled_by_text(VIEW_TEXT_VIEW,'Deselect all',isScrollable=0):
                goback()
        except:
            cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
            log_test_case(self.tag, "before DELETE: something wrong while selecting all in "+cur_path)
            set_cannot_continue()
            
        #
        # STEP 3: delete
        #
        if can_continue():
            try:
                click_textview_by_desc('Delete',isScrollable=0)
                click_button_by_text('OK')
            except:
                cur_path = get_view_text_by_id(VIEW_TEXT_VIEW,'tv_path',isVerticalList=1)
                log_test_case(self.tag, "no 'Delete' button in path:" + cur_path)
                set_cannot_continue()
                
                
        #
        # STEP 4: confirm whether delete is successfully
        #
        if can_continue():
            goto_dir(work_dir,'Folder',go_from_home_screen=False)
            if get_view_text_by_index(VIEW_TEXT_VIEW,4):
                a = get_view_text_by_index(VIEW_TEXT_VIEW,4)
                take_screenshot()
                cur_path = get_view_text_by_id(VIEW_TEXT_VIEW,'tv_path',isVerticalList=1)
                log_test_case(self.tag, "after DELETE: something still exist in path " + cur_path)
            else:
                case_flag = True
      
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "delete all items is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
