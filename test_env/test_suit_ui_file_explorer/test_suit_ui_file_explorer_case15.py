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


class test_suit_ui_file_explorer_case15(TestCaseBase):
    tag = 'ui_file_explorer_case15'
    
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: open wifi and add email account for sharing by email
        #
        start_activity("com.android.settings", ".Settings")
        settings.whether_open_mobile_data(False)
        settings.enable_wifi(SC.PUBLIC_WIFI_NAME, SC.PUBLIC_WIFI_PASSWORD_SEQUENCE)
        launcher.launch_from_launcher('email')
        email.add_email_account_8916(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_EMAIL_EMAIL_PASSWORD_SEQUENCE)
        
        #
        # STEP 2: choose item to share
        #
        #work_dir_list = ('Music','Video','Image','APK')
        work_dir_list = ('Music',)
        flag = True
        for work_dir in work_dir_list:
            
            # check email account
            launcher.launch_from_launcher('email')
            if not email.is_mail_login():
                email.mail_login(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_EMAIL_EMAIL_PASSWORD_SEQUENCE)
            
            goto_dir(work_dir,'Category')
            #a = get_view_text_by_id(VIEW_TEXT_VIEW,'text')
            click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
            
            #
            # STEP 3: share
            #
            try:
                email_subject = share_by_email()
            except:
                flag = False
                log_test_case(self.tag, "dir "+work_dir+" FAIL to share item by email")
            
            # check if item has been received
            if not subject_received_by_email(email_subject):
                flag = False
                take_screenshot()
                log_test_framework(self.tag, "share_by_email() failed in work_dir %s"%work_dir)
                
        
        if flag:
            case_flag = True

      
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "share item in FileExplorer by email is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

