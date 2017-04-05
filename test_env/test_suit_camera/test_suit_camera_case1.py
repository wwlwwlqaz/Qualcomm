import fs_wrapper
from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    use the foreground camera to take a VGA picture
#precondition:
#    there is a mounted sdcard
#steps:
#    open the foreground camera
#    set the VGA picture size
#    take a picture
############################################

class test_suit_camera_case1(TestCaseBase):
    def test_case_main(self,case_results):
        sleep(3)
        #check the sdcard .no sdcard, no continue
        local_assert(True,is_external_storage_enable())
        if not can_continue():
            return
        #switch to foreground camera.
        camera.switch_2_foreground_camera()

        #open the second level settings
        click_imageview_by_id('second_level_indicator')
        #click the other settings imageview to set picture size
        click_view_by_container_id('second_level_indicator_bar','android.widget.ImageView','2')

        #search VGA text
        MAX_COUNT = 5
        count = 0
        while search_text('VGA',searchFlag=TEXT_MATCHES) ==False and count < MAX_COUNT:
            count = count + 1
            click_textview_by_desc(camera.get_value('increase_picture_size'))

        if count >= MAX_COUNT:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'can not find the VGA label')
            set_cannot_continue()
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'can not find the VGA label', logging_wrapper.SEVERITY_HIGH)
            return

        #close the other settings,back to the first level
        click_imageview_by_id('back_to_first_level')

        #click the shutter button
        if not camera.take_picture():
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take picture failed')
            set_cannot_continue()
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take picture failed', logging_wrapper.SEVERITY_HIGH)
            return
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'take picture success', logging_wrapper.SEVERITY_HIGH)
