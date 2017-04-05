import fs_wrapper
from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    use the foreground camera to take a 10s video
#precondition:
#    there is a mounted sdcard
#steps:
#    open the foreground camera
#    switch to the video mode
#    take a 10 video
############################################

class test_suit_camera_case2(TestCaseBase):
    def test_case_main(self,case_results):
        sleep(2)
        #check the sdcard .no sdcard, no continue
        local_assert(True,is_external_storage_enable())
        if not can_continue():
            return

        #switch to foreground camera.
        camera.switch_2_foreground_camera()

        #switch to video mode
        camera.switch_2_video_mode()

        #begin to take video
        if not camera.take_video(10):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take video failed')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take video failed', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
            return
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, '', logging_wrapper.SEVERITY_HIGH)
