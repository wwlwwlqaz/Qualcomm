import fs_wrapper
from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    use the background camera to take a 3M pixels picture
#precondition:
#    there is a mounted sdcard
#steps:
#    open the background camera
#    set the 3M picture size
#    take a picture
############################################


class test_suit_camera_case4(TestCaseBase):
    def test_case_main(self,case_results):
        sleep(2)
        #check the sdcard .no sdcard, no continue
        local_assert(True,is_external_storage_enable())
        if not can_continue():
            return

        #switch to background camera.
        camera.switch_2_background_camera()

        #open the second level settings
        click_imageview_by_id('second_level_indicator')
        #click the other settings imageview to set picture size

        click_view_by_container_id('second_level_indicator_bar','android.widget.ImageView','2')
#        index = 5
#        if getRuntimeEnv() != ROBOTIUM:
#            index = 2
#        if search_view_by_id('onscreen_flash_indicator'):
#            index = index +1
#        if search_view_by_id('onscreen_white_balance_indicator'):
#            index = index +1
#        if search_view_by_id('onscreen_exposure_indicator'):
#            index = index +1
#        if search_view_by_id('onscreen_scene_indicator'):
#            index = index +1
#        if search_view_by_id('onscreen_gps_indicator'):
#            index = index +1
#        if search_view_by_id('onscreen_focus_indicator'):
#            index = index +1
#        click_imageview_by_index(index)

        #search 3M pixels text
        MAX_COUNT = 15
        count = 0
        while search_text(camera.get_value('3m_pixels'),1,0) == False and count < MAX_COUNT:
            count = count + 1
            if search_text(camera.get_value('5m_pixels'),1,0):
                click_textview_by_desc(camera.get_value('decrease_picture_size'))
            else:
                click_textview_by_desc(camera.get_value('increase_picture_size'))

        if count >= MAX_COUNT:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'can not find the 5M pixels label')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'can not find the 5M pixels label', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
            return

        #close the other settings,back to the first level
        click_imageview_by_id('back_to_first_level')

        #click the shutter button
        if not camera.take_picture():
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take picture failed')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take picture failed', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
            return
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, '', logging_wrapper.SEVERITY_HIGH)
