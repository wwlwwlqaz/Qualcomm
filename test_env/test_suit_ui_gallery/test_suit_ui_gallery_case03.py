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
#    take a picture in gallery
############################################
import os,re,subprocess,shlex
from test_suit_ui_gallery import *
import test_suit_ui_file_explorer.test_suit_ui_file_explorer as suit_FE


class test_suit_ui_gallery_case03(TestCaseBase):
    tag = 'ui_gallery_case03'
    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: before operation, record the photo number
        #
        work_dir = '/sdcard/DCIM/Camera'
        filetype = '.jpg'
        num1 = suit_FE.num_of_filetype_in_folder(work_dir,filetype)
        log_test_case(self.tag, "num1 = "+str(num1))
        
        #
        # STEP 2: take photo in gallery
        #
        take_photo_in_gallery(self.tag)
                
        #
        # STEP 3:after operation, record the photo number
        #
        if can_continue():
            # have to wait for operation completing, about 3 seconds
            sleep(5)
            # caculate the .jpg number
            num2 = suit_FE.num_of_filetype_in_folder(work_dir,filetype)
            log_test_case(self.tag, "num2 = "+str(num2))
        
        #
        # STEP 4: check if number increase
        #
        if can_continue():
            if num2>num1 :
                case_flag = True
        
        #
        #  STEP 5: exit
        #
        exit_cur_case(self.tag)


        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "take photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))