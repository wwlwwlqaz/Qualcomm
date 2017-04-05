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
#    rename an item in FileExplorer
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

class test_suit_ui_file_explorer_case02(TestCaseBase):
    tag = 'ui_file_explorer_case02'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: goto specific dir in FileExplorer
        #
        goto_dir('/Phone storage/DCIM/Camera','Folder')
        
        #
        # STEP 2: choose an item to rename
        #
        if can_continue(): 
            # prefer choosing a 'QT'... folder
            #ori_path = get_view_text_by_id(VIEW_TEXT_VIEW,'tv_path',isVerticalList=0)
            ori_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
            try:
                # 'QT...' dir
                ori_name = get_text('QT',isVerticaList=1,isScrollable=1,searchFlag=TEXT_STARTS_WITH)
            except:
                log_test_case(self.tag, "no 'QT...' dir to rename in folder:" + ori_path)
                try:
                    # other item is also OK
                    ori_name = get_view_text_by_id('text')
                    log_test_case(self.tag, "use ori_name:" + ori_name + 'to test rename utility')
                except:
                    # no item to rename, case fail
                    log_test_case(self.tag, "no item in folder:" + ori_path)
                    set_cannot_continue()
            
        #
        # STEP 3: rename
        #
        if can_continue():
            new_folder_name = rand_name()
            global current_case_continue_flag
            current_case_continue_flag = rename(self.tag,ori_path,ori_name,new_folder_name)

            
        #
        # STEP 4: confirm whether new folder is created correctly
        #
        if can_continue():
            #goto_dir('/Phone storage')
            new_folder_name = '(?i)' + new_folder_name
            func = lambda:search_text(new_folder_name,searchFlag=TEXT_MATCHES_REGEX)
            if wait_for_fun(func,True,15):
                case_flag = True

                # recovery
                try:
                    flag = rename(self.tag,ori_path,new_folder_name,ori_name)
                    if flag:log_test_framework(self.tag, "RECOVERY has done! old_name\'"+new_folder_name+"\'to new_name\'"+ ori_name+"\'")
                    else:log_test_framework(self.tag,"RECOVERY is wrong! rename() return False")
                except:log_test_framework(self.tag, "RECOVERY is wrong! rename() throw exception")
        
      
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "rename item in file_explorer is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))



def rename(case_TAG,ori_path,old_name,new_name):
    tag = 'rename(old_name,new_name)'
    try:scroll_to_top()
    except:pass
    
    try:
        click_textview_by_text(old_name, searchFlag=TEXT_MATCHES_REGEX, clickType=LONG_CLICK)
        click_imageview_by_desc('More options')
        click_textview_by_text('Rename')
    except:
        take_screenshot()
        log_test_case(case_TAG, "WRONG when rename %s to %s in %s."%(old_name,new_name,ori_path))
        return False
    
    entertext_edittext_on_focused(new_name, isScrollable=0, isClear=1)
    click_button_by_text('OK')
    return True
    
    
    
