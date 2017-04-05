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
#    share item in FileExplorer by email
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
from test_suit_ui_message.test_suit_ui_message import *


class test_suit_ui_file_explorer_case16(TestCaseBase):
    tag = 'ui_file_explorer_case16'
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: need a SIM to share item by MMS
        #
        if 'no available sim card' == get_sim_card_state(SLOT_ONE):
            set_cannot_continue()
            log_test_case(self.tag, "get_sim_card_state(SLOT_ONE):" + 'no available sim card')
            log_test_case(self.tag, "no SIM, case failed and skipped")
        
        #
        # STEP 2: choose item to share
        #
        if can_continue():
            #work_dir_list = ('Music','Video','Image','APK')
            work_dir_list = ('Music',)
            flag = True
            for work_dir in work_dir_list:
                try:
                    launcher.launch_from_launcher('mms')
                    num1 = message_num_in_thread(SC.PUBLIC_SLOT1_PHONE_NUMBER)
                    
                    #
                    # STEP 3: share
                    #
                    goto_dir(work_dir,'Category')
                    #a = get_view_text_by_id(VIEW_TEXT_VIEW,'text')
                    click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
                    share_by_mms(SC.PUBLIC_SLOT1_PHONE_NUMBER_SEQUENCE)
                    
                    launcher.launch_from_launcher('mms')
                    num2 = message_num_in_thread(SC.PUBLIC_SLOT1_PHONE_NUMBER)
                    
                    if not (num2>num1):
                        flag = False
                        take_screenshot()
                        log_test_framework(self.tag, "share_by_mms() failed in work_dir %s"%work_dir)
                except:
                    flag = False
                    log_test_case(self.tag, "dir "+work_dir+" FAIL to share item by MMS")
            
            if flag:
                case_flag = True
    
          
            #
            # STEP 4: exit
            #
            exit_cur_case(self.tag)
                
            
            log_test_case(self.tag, "case_flag = "+str(case_flag))  
            if case_flag:
                qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
            else:
                qsst_log_case_status(STATUS_FAILED, "share item in FileExplorer by mms is failed", SEVERITY_HIGH)
            case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

   
    