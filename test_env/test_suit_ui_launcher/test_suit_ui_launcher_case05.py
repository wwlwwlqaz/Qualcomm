from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#     Launcher Stress-add widget
#precondition:
#     have enough empty screens
############################################
from test_suit_ui_launcher import *

class test_suit_ui_launcher_case05(TestCaseBase):
    tag = 'ui_launcher_case05'
    def test_case_main(self,case_results):
        #call("test_suit_camera", "test_suit_camera_case9")
        case_flag = False
        
        #check_list = ('Cell Broadcast','LED flashlight')
        check_list = ('Digital clock',)
        for widget in check_list:
            flag = True    
            
            #
            # STEP1: find or make an empty home screen
            #
            send_key(KEY_HOME)
            
            #
            # STEP2: long press widget to send it to home
            #
            #launcher.launch_from_launcher('widgets')
            click_textview_by_desc('Apps',isScrollable=0)
            click_textview_by_text('Apps')
            click_textview_by_text('Widgets')
            try:
                click_textview_by_text(widget, isVerticalList=0,clickType=LONG_CLICK)
            except:
                flag = False
                log_test_case(self.tag,"cannot find widgets: "+ widget)
                continue
            
            #
            # STEP3: check text: name & current_activity
            #
            #send_key(KEY_HOME)
            func = lambda:search_view_by_id(WIDGET_LIST[widget][SEARCH_BY_ID])
            if not wait_for_fun(func,True,3):
                log_test_case(self.tag,"add widgets: " + widget+' Failure')
                flag = False
            func = lambda:search_view_by_desc('Apps')
            if not wait_for_fun(func,True,2):
                flag = False
                log_test_case(self.tag,"after add widgets: " + widget+", cannot find the 'app'")
                
        if flag:
            case_flag = True
      
        
        log_test_case(self.tag, 'case_flag = '+str(case_flag))
        exit_cur_case(self.tag)    
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "some widgets are failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
