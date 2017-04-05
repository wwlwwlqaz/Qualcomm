from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#     Launcher Stress-check sdcard state
############################################
from test_suit_ui_launcher import *


class test_suit_ui_launcher_case10(TestCaseBase):
    tag = 'ui_launcher_case10'
    def test_case_main(self,case_results):
        #search_text('Downloads')
        case_flag = False
        
        #
        # STEP 1: launch to sdcard information
        #
        start_activity('com.android.settings','.Settings')
        click_textview_by_text('Storage')
        # list what information you want to know
        info_list = ['Total space',\
                     'Available','Apps (app data & media content)','Pictures, videos',\
                     'Audio (music, ringtones, podcasts, etc.)','Downloads','Misc.',\
                     'Cached data',\
                     ]
        #
        # STEP 2: read sdcard information
        #
        flag = True
        sdcard_info = "\n"
        drag_by_param(50, 58, 50, 50, 10)
        
        for info_title in info_list:
            search_text(info_title,searchFlag=TEXT_MATCHES)   # scroll screen to right position
            content = get_view_text_by_index(VIEW_TEXT_VIEW,STORAGE_INFO_INDEX[info_title]+1)
            
            #
            # STEP 3: can information be read? or confirm does it fit expect state
            #
            #if content != STORAG_REFER_INDEX[info_title]: flag = False
            if not content:
                flag = False
                log_test_case(self.tag,"cannot read info:" + info_title)
            sdcard_info = sdcard_info + info_title +":\n" + content + "\n"
        
        log_test_case(self.tag,"\nsdcard_information : " + sdcard_info)
        # is_external_storage_enable() == True

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
            qsst_log_case_status(STATUS_FAILED, "check sdcard state is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        