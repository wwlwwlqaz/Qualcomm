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
#    create a new folder in FileExplorer
#precondition:
#    
#step:
#    1.goto FileExplorer; 
#            if not, goto step4
#    2.try to create a new folder; 
#            if not, goto step4
#    3.confirm whether new floder is created correctly;
#            if not, goto step4
#    4.exit to end case
############################################
import os,re,string
from test_suit_ui_file_explorer import *

class test_suit_ui_file_explorer_case01(TestCaseBase):
    tag = 'ui_file_explorer_case01'    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: goto specific dir in FileExplorer
        #
        goto_dir('/Phone storage/DCIM/Camera','Folder')
        
        #
        # STEP 2: try to create a new folder
        #
        if can_continue():
            try:
                #click_imageview_by_desc('More options')
                #click_textview_by_text('New folder')
                click_menuitem_by_text('New folder')
            except:
                #cur_path = get_view_text_by_id(VIEW_TEXT_VIEW,'tv_path',isVerticalList=0)
                cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
                log_test_case(self.tag, "no 'New folder' button in current folder:" + cur_path)
                set_cannot_continue()
            
            # give the new folder a random name(prefix 'QT')
            if can_continue():
                new_folder_name = rand_name()
                entertext_edittext_on_focused(new_folder_name, isScrollable=0, isClear=1)
                click_button_by_text('OK')
                
        #
        # STEP 3: confirm whether new folder is created correctly
        #
        if can_continue():
            new_folder_name = '(?i)' + new_folder_name # ignore case
            func = lambda:search_text(new_folder_name, searchFlag=TEXT_MATCHES_REGEX)
            if wait_for_fun(func,True,20):
                #print "I found it!!!"
                #os.system('am start -n com.android.music/com.android.music.MusicBrowserActivity')
                case_flag = True
        
      
        #
        # STEP 4: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "creat a new folder in file_explorer is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
