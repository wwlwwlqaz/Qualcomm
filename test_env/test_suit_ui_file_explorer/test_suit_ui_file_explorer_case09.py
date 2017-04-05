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
#    move items cross storage
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

class test_suit_ui_file_explorer_case09(TestCaseBase):
    tag = 'ui_file_explorer_case09'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        if not is_external_storage_enable():
            log_test_case(self.tag, "no sd card, cannot start case")
            set_cannot_continue()
        
        #
        # STEP 1: goto work_dir in FileExplorer
        #
        if can_continue():
            work_dir = '/Phone storage/DCIM/Camera'
            number = preprocess(self.tag,work_dir,floor=3)
            goto_dir(work_dir,'Folder')

        
        
        #
        # STEP 2: choose items to copy
        #
        if can_continue():
            try:
                (index_list,num1) = random_index_list_in_folder(work_dir,'.jpg')
                log_test_case(self.tag,"num1=%s want to copy %s photos"%(str(num1),str(len(index_list)+1)))
                
                first_name = get_view_text_by_id(VIEW_TEXT_VIEW,'text')
                click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
                
                name_list = []
                for i in range(len(index_list)):
                    click_textview_by_index(index_list[i])
                    name_list.append(get_view_text_by_index(VIEW_TEXT_VIEW,index_list[i]))
                
                name_list.insert(0, first_name)
                click_textview_by_desc('Move',isScrollable=0)
            except:
                take_screenshot()
                cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
                log_test_case(self.tag, "during COPY: something wrong, maybe no item in " + cur_path)
                set_cannot_continue()
        
        #
        # STEP 3: goto destination
        #        
        if can_continue():
            destination = '/SD card'
            goto_dir(destination,'Folder',go_from_home_screen=False)

            
        #
        # STEP 4: copy items to destination
        #
        if can_continue():
            try:
                click_button_by_text('Paste',waitForView=1)
            except:
                take_screenshot()
                cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
                log_test_case(self.tag, "during COPY: no 'Paste' in " + cur_path)
                set_cannot_continue()
            
        # check    
        if can_continue():
            goto_dir(destination,'Folder',go_from_home_screen=True)
            cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
            
            flag = True
            for i in range(len(name_list)):
                if search_text('%s'%name_list[i],searchFlag=TEXT_MATCHES_REGEX):
                    try:scroll_to_top()
                    except:pass
                    continue
                else:
                    flag = False
                    break
            
            if flag is True:
                case_flag = True
            else:
                log_test_case(self.tag, "failed copy %s "%name_list[i] +'in '+ cur_path)

      
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "move items cross folder is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
