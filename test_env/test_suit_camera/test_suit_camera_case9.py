from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    lqiang@cienet.com.cn
#function:
#    switch to the background camera , and take a picture
############################################

class test_suit_camera_case9(TestCaseBase):
    def test_case_main(self,case_results):
        sleep(2)
        camera.switch_2_background_camera()
        if not camera.take_picture():
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take picture failed')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take picture failed', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'success', logging_wrapper.SEVERITY_HIGH)
