from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#     Launcher Stress-slide 5 screen
############################################
from test_suit_ui_launcher import *


class test_suit_ui_launcher_case08(TestCaseBase):
    tag = 'ui_launcher_case08'
    
    def test_case_main(self,case_results):
        case_flag = True
        
        send_key(KEY_HOME)
        sleep(3)
        drag_by_param(90,50,10,50,2)
        sleep(3)
        drag_by_param(90,50,10,50,2)
        sleep(3)
        send_key(KEY_HOME)
        sleep(3)
        drag_by_param(10,50,90,50,2)
        sleep(3)
        drag_by_param(10,50,90,50,2)
        sleep(3)
        
        #
        # STEP : exit
        #
        exit_cur_case(self.tag)
        
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))    
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "some widgets are failed or cannot drag screen", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
    