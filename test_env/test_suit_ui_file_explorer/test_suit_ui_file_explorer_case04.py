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
#    delete items in FileExplorer
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

class test_suit_ui_file_explorer_case04(TestCaseBase):
    tag = 'ui_file_explorer_case04'
    
    
    def test_case_main(self, case_results):
        case_flag = False
        
        
        #run_monkey_in_camera()
        
        #
        # STEP 1: goto work_dir in FileExplorer
        #
        work_dir = '/Phone storage/DCIM/Camera'
        preprocess(self.tag,work_dir,floor=3)
        goto_dir(work_dir,'Folder')
        
        
        #
        # STEP 2: choose an item to delete
        #
        try:
            (index_list,num1) = random_index_list_in_folder(work_dir,'.jpg')
            log_test_case(self.tag,"num1=%s want to delete %s photos"%(str(num1),str(len(index_list)+1)))
            #click_view_by_container_id('list','android.widget.TextView',0)
            click_textview_by_id('text',waitForView=1, clickType=LONG_CLICK)
            first_name = get_view_text_by_id(VIEW_TEXT_VIEW,'text')
            #click_view_by_container_id('list','android.widget.TextView',2)
            name_list = []
            for i in range(len(index_list)):
                click_textview_by_index(index_list[i])
                name_list.append(get_view_text_by_index(VIEW_TEXT_VIEW,index_list[i]))
            
            name_list.insert(0, first_name)
        except:
            #cur_path = get_view_text_by_id(VIEW_TEXT_VIEW,'tv_path',isVerticalList=1)
            cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
            log_test_case(self.tag, "before DELETE: no 2'*.jpg' file to delete in folder:" + cur_path)
            set_cannot_continue()
            
        #
        # STEP 3: delete
        #
        if can_continue():
            try:
                click_textview_by_desc('Delete',isScrollable=0)
                click_button_by_text('OK')
            except:
                cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
                log_test_case(self.tag, "no 'Delete' button in path:" + cur_path)
                set_cannot_continue()
                
                
        #
        # STEP 4: confirm whether delete is successfully
        #
        if can_continue():
            goto_dir(work_dir,'Folder')
            string = '|'.join(name_list)
            func = lambda:search_text('%s'%(string),searchFlag=TEXT_MATCHES_REGEX)
            num2 = num_of_filetype_in_folder(work_dir,'.jpg')
            log_test_case(self.tag,"num2=%s"%str(num2))
            if wait_for_fun(func,False,5) and (num2==(num1-len(index_list)-1)):
                case_flag = True
            else:
                cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
                log_test_case(self.tag, "after DELETE: file '%s' still exists in %s"%(string,cur_path))
      
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "delete items is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
