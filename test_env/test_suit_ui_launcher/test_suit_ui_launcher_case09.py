from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#     Launcher Stress-check SIM state
############################################
from test_suit_ui_launcher import *


class test_suit_ui_launcher_case09(TestCaseBase):
    tag = 'ui_launcher_case09'
    def test_case_main(self,case_results):
        case_flag = True
        
        #
        # STEP 1: launch to SIM information
        #
        start_activity('com.android.settings','.Settings')
        click_textview_by_text('About phone')
        click_textview_by_text('Status')
        # list what information you want to know
        info_list = ['My phone number','Network','Signal strength','Mobile network type','Service state',\
                     'Roaming','IMEI','IMEI SV','Mobile network state',\
                     ]
        
        #
        # STEP 2: read SIM information
        #
        flag = True
        sim_info = "\n"
        for info in info_list:
            if search_text(info):pass   # scroll screen to right position
            t = get_view_text_by_index(VIEW_TEXT_VIEW,SIM_INFO_INDEX[info])
            
            #
            # STEP 3: can information be read? or confirm does it fit expect state
            #
            #if t != SIM_REFER_INDEX[info]: case_flag = False
            if not t:
                flag = False
                log_test_case(self.tag,"cannot read info:" + info)
            
            sim_info = sim_info + info + ":\n" + t + "\n"
        #sim_info = get_text('SIM')
        log_test_case(self.tag,"\nsim_information : " + sim_info)
        
        # get_serial_number() == '1408638269.49_0.968113686586'
        # get_sim_card_state(SLOT_ONE) == 'no available sim card'
        # get_sim_card_vendor(SLOT_ONE) == 'unknown or locked or error'
        # get_sim_card_rssi(SLOT_ONE) == 'great'
        # get_networktype(SLOT_ONE) == 'UNKNOWN'


        
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
            qsst_log_case_status(STATUS_FAILED, "check SIM state is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        