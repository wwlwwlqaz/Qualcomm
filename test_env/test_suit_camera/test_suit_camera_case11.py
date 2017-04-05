from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    lqiang@cienet.com.cn
#function:
#    switch to the background camera , and take a video
############################################

class test_suit_camera_case11(TestCaseBase):
    def test_case_main(self,case_results):
        sleep(2)
        camera.switch_2_background_camera()
        camera.switch_2_video_mode()
        if not camera.take_video(10):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take video failed')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take video failed', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, '', logging_wrapper.SEVERITY_HIGH)
