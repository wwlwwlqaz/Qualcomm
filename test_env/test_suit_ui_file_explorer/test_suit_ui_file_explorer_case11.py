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
#    move items cross storage in FileExplorer
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
import os,re,string,subprocess,shlex
from test_suit_ui_file_explorer import *


class test_suit_ui_file_explorer_case11(TestCaseBase):
    tag = 'ui_file_explorer_case11'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: open bluetooth for sharing by bluetooth
        #
        enable_bluetooth()
        if bluetooth_pair():
            #
            # STEP 2: goto work_dir in FileExplorer
            #
            work_dir = 'Video'
            goto_dir(work_dir,'Category')
            
            #
            # STEP 3: choose items to share
            #
            if can_continue():
                try:
                    click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
                    click_view_by_container_id('list','android.widget.TextView',2)
                except:
                    cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
                    log_test_case(self.tag, "before SHARE: something wrong, maybe no item in " + cur_path)
                    set_cannot_continue()
                
                
                if can_continue():
                    try:
                        case_flag = share_by_bluetooth()
                    except:
                        log_test_case(self.tag, "something wrong during share_by_bluetooth()")
      
        #
        # STEP 4: exit
        #
        disable_bluetooth()
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "launch video and share is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
        
        
                