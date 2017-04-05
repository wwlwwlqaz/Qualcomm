from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#     Launcher Stress-slide 5 screen & add widget
#precondition:
#     have enough space in every screen
############################################
from test_suit_ui_launcher import *
import sys

class test_suit_ui_launcher_case11(TestCaseBase):
    tag = 'ui_launcher_case11'
    
    def goto_homescreen_by_index(self,index = 3):
        send_key(KEY_HOME)
        for i in range(2):  # drag to the 1st homescreen
            drag_by_param(10,50,90,50,2)
        for i in range(index):# drag to the index
            drag_by_param(90,50,10,50,2)
    
    def test_case_main(self,case_results):
        case_flag = False
        
        check_list = ('Data monitor','LED flashlight','Data monitor')
        #
        #drag to the most left screen
        #
        self.goto_homescreen_by_index(0)
        
        flag = True
        for widget in check_list:
            #
            # STEP1: long press widget to send it to home
            #
            click_textview_by_desc('Apps',isScrollable=0)
            click_textview_by_desc('Apps',isScrollable=0) # have to add this click, in case cannot find 'Widgets' 1st page
            click_textview_by_desc('Widgets',isVerticalList=0)
            try:
                click_textview_by_text(widget, isVerticalList=0,clickType=LONG_CLICK)
            except:
                flag = False
                log_test_case(self.tag,"cannot find widgets"+str(check_list.index(widget))+": "+ widget)
                # move to next right screen 
                self.goto_homescreen_by_index(check_list.index(widget)+1)
                continue
            #
            # STEP2: check text: name & current_activity
            #
            func = lambda:search_view_by_id(WIDGET_LIST[widget][SEARCH_BY_ID])
            if not wait_for_fun(func,True,3):
                flag = False
                log_test_case(self.tag,"add widgets"+str(check_list.index(widget)) + ': ' + widget+' failure')
                self.goto_homescreen_by_index(check_list.index(widget)+1)
                continue

            #
            # STEP3: move to next right screen 
            #
            drag_by_param(90,50,10,50,2)
            sleep(3)
        
        if True == flag:
            case_flag = True
        #
        # STEP 4: exit
        #
        exit_cur_case(self.tag)
        
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))    
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "some widgets are failed or cannot drag screen", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
