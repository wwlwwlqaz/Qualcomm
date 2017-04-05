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
#    share item in FileExplorer by bluetooth 
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


class test_suit_ui_file_explorer_case14(TestCaseBase):
    tag = 'ui_file_explorer_case14'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        notificationBar.airplane_mode('off')
        launcher.launch_from_launcher('settings')
        settings.bluetooth('on')
        if settings.bluetooth_pair() is False:
            take_screenshot()
            log_test_case(self.tag,"bluetooth cannot pair")
            set_cannot_continue()
            
            
        if can_continue():
            #work_dir_list = ('Music','Video','Image','APK')
            work_dir_list = ('Music',)
            flag = True
            for work_dir in work_dir_list:
                
                try:
                    #goto_dir(work_dir,'Category')
                    ##a = get_view_text_by_id(VIEW_TEXT_VIEW,'text')
                    #click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
                    flag = share_by_bluetooth()
                    if not flag:
                        take_screenshot()
                        log_test_framework(self.tag, "share_by_bluetooth() failed in work_dir %s"%work_dir)
                except:
                    flag = False
                    take_screenshot()
                    log_test_case(self.tag, "dir "+work_dir+" FAIL to share item by bluetooth")
            
            if flag:
                case_flag = True

      
        #
        # STEP 5: exit
        #
        disable_bluetooth()
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "share item by bluetooth is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

        