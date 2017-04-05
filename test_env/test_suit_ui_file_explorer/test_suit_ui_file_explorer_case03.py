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
#    delete an item in FileExplorer
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
import test_suit_ui_gallery

class test_suit_ui_file_explorer_case03(TestCaseBase):
    tag = 'ui_file_explorer_case03'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: goto specific dir in FileExplorer
        #
        work_dir = '/Phone storage/DCIM/Camera'
        goto_dir(work_dir,'Folder')
        
        
        #
        # STEP 2: choose an item to delete
        #
        # prefer choosing a 'QT'... folder 
        cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
        # prefer deleting 'QT...' dir
        ori_name = get_text('QT',isVerticaList=1,isScrollable=1,searchFlag=TEXT_STARTS_WITH)
        
        if ori_name is '':
            # other item is also OK.  # delete the 1st item
            ori_name = get_view_text_by_index(VIEW_TEXT_VIEW,2)
            if ori_name is '':
                preprocess(self.tag,work_dir)
                goto_dir(cur_path)
                #click_view_by_container_id('list','android.widget.ListView',0)
                ori_name = get_view_text_by_index(VIEW_TEXT_VIEW,2)
        
        if ori_name is '':
            log_test_case(self.tag,"cannot find item to delete in "+cur_path)
            set_cannot_continue()

            
        #
        # STEP 3: delete
        #
        if can_continue():
            try:
                click_textview_by_text(ori_name, searchFlag=TEXT_MATCHES,clickType=LONG_CLICK)
                click_textview_by_desc('Delete')
                click_button_by_text('OK')
            except:
                log_test_case(self.tag, "'Delete' wrong:" + cur_path +'/'+ ori_name)
                set_cannot_continue()
            
        #
        # STEP 4: confirm whether delete is successfully
        #
        if can_continue():
            goto_dir(cur_path)
            if not search_text(ori_name):
                case_flag = True
      
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "delete item in file_explorer is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
