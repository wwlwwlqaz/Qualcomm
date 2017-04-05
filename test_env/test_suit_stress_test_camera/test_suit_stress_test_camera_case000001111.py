'''
@author: c_caijie
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.mms.Mms import *
from wx.lib.agw.peakmeter import InRange
from warnings import catch_warnings



class test_suit_stress_test_camera_case000001111(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch camera;
    Step2:Switch flash light to Auto, and take a picture;
    Step3: switch flash light to On, and take a picture;
    Step4: switch flash light to Off, and take a picture;
    Step5: repeat Step2 to Step5 for 100 time;    
    Verification: 
    ER2: picture have no exception;
    ER3: picture have no exception;
    ER4: picture have no exception;
    ER5: picture have no exception;    
    '''
    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG, testresult, success_flag, i, success_time, auto_flag, on_flag, off_flag
        # case_flag = False
        testresult = []
        success_time = 0
        iterationNum = 3
        total_count = 0
        pass_count = 0
        TAG = "Dev-ci cases: Camera "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """
        while total_count < iterationNum:
            case_flag = False
            try:
                case_flag = camera.case_1()
                print case_flag
            except Exception:
                print 'baocuole'
            finally:
                total_count +=1
                if case_flag:
                    pass_count+=1
                    print 'zhixinchenggongle di %s ci' % pass_count
                    
                    
        print 'result:'
        print pass_count        
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "", SEVERITY_HIGH)
        
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        
        
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : end')
        if can_continue() and case_flag == True:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tfail')
        save_fail_log()
            
