import fs_wrapper
from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    user H263 encoder to take a 10s video
#steps:
#    open the background camera
#    change to the video mode
#    set the H263 encoder
#    take a 10s video
############################################


class test_suit_camera_case6(TestCaseBase):
    def test_case_main(self,case_results):
        sleep(2)
        #check the sdcard .no sdcard, no continue
        local_assert(True,is_external_storage_enable())
        if not can_continue():
            return

        #switch to background camera.
        camera.switch_2_background_camera()

        #switch to video mode
        camera.switch_2_video_mode()

        #open the second level settings
        click_imageview_by_id('second_level_indicator')
        #click the other settings
        click_imageview_by_id('other_setting_indicator')
        #search H264 text
        MAX_COUNT = 5
        count = 0
        while search_text('H263', 1, 0) == False and count < MAX_COUNT:
            count = count + 1
            #click to search the H263
            if search_text('H264',1,0):
                click_textview_by_desc(camera.get_value('increase_video_size'))
            else:
                click_textview_by_desc(camera.get_value('decrease_video_size'))

        if count >= MAX_COUNT:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'can not find the H263 label')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'can not find the H263 label', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
            return
        #close the other settings,back to the first level
        click_imageview_by_id('back_to_first_level')

        #begin to take video
        if not camera.take_video(10):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take video failed')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take video failed', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
            return
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, '', logging_wrapper.SEVERITY_HIGH)
