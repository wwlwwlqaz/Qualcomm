#coding=utf-8
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



class test_suit_stress_test_camera_case000023(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch Camera;
    Step2:take snapshot;
    Step3: tap thumbnail, and edit the snapshot;
    Step4:tap different effect to repeat for  slide 100 time, such as: None/Punch/Vintage/B/W and so;
    Step5: save the picture;
    Verification: 
    ER5:save successfully and no exception.   
    '''
    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG, testresult, success_flag, i, success_time, Punch_flag, Vintage_flag, BW_flag, Bleach_flag, Instant_flag, Latte_flag, Blue_flag, Litho_flag, XProcess_flag
        case_flag = False
        testresult1 = []
        testresult2 = []
        testresult3 = []
        testresult4 = []
        testresult5 = []
        testresult6 = []
        testresult7 = []
        testresult8 = []
        testresult9 = []       
        success_time1 = 0
        fail_time1 = 0
        success_time2 = 0
        fail_time2 = 0
        success_time3 = 0
        fail_time3 = 0
        success_time4 = 0
        fail_time4 = 0
        success_time5 = 0
        fail_time5 = 0
        success_time6 = 0
        fail_time6 = 0
        success_time7 = 0
        fail_time7 = 0
        success_time8 = 0
        fail_time8 = 0
        success_time9 = 0
        fail_time9 = 0
        iterationNum = 100
        TAG = "Dev-ci cases: Camera "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """
        if search_text("Close app", searchFlag=TEXT_CONTAINS):
            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
            sleep(2) 
                        
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 10):
            click_button_by_id('permission_allow_button')
        if wait_for_fun(lambda:search_text('OK'), True, 5):            
            click_textview_by_text('OK')
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
            log_test_framework("step1:", "Launch Camera pass")            
#             if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 5):
#                 click_imageview_by_id("scene_mode_switcher")
#             if wait_for_fun(lambda:search_view_by_id('setting_button'), True, 5):
#                 click_imageview_by_id("setting_button")
#                 if wait_for_fun(lambda:search_text("Storage"), True, 8):
#                     click_textview_by_text("Storage")
#                     if wait_for_fun(lambda:search_text("SD Card"), True, 8):
#                         click_textview_by_text("SD Card")            
#                 send_key(KEY_BACK)
#                 sleep(2)                           
        '''
        Punch effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Punch effect iteration %d'%(i+1))
                    Punch_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        sleep(3)
                        if wait_for_fun(lambda:search_view_by_desc("Punch"), True, 5):
                            click(445, 2021)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                sleep(3)
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Punch effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult1.append('%d.Pass'%(i+1))
                        success_time1=success_time1+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult1.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time1=fail_time1+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time1 == iterationNum:
                    Punch_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Punch effect success:%d fail:%d iteration:%d'%(success_time1,fail_time1,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult1)
                send_key(KEY_BACK)
                sleep(2)            
        '''
        Vintage effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Punch effect iteration %d'%(i+1))
                    Vintage_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("Vintage"), True, 5):
                            click(699, 2026)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Vintage effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult2.append('%d.Pass'%(i+1))
                        success_time2=success_time2+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult2.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time2=fail_time2+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time2 == iterationNum:
                    Vintage_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Vintage effect success:%d fail:%d iteration:%d'%(success_time2,fail_time2,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult2)
                send_key(KEY_BACK)
                sleep(2) 
        '''
        B/W effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('B/W effect iteration %d'%(i+1))
                    BW_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("B/W"), True, 5):
                            click(998, 2016)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "B/W effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult3.append('%d.Pass'%(i+1))
                        success_time3=success_time3+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult3.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time3=fail_time3+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time3 == iterationNum:
                    BW_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'B/W effect success:%d fail:%d iteration:%d'%(success_time3,fail_time3,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult3)
                send_key(KEY_BACK)
                sleep(2) 
        '''
        Bleach effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Bleach effect iteration %d'%(i+1))
                    Bleach_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("Bleach"), True, 5):
                            click(1292, 2016)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Bleach effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult4.append('%d.Pass'%(i+1))
                        success_time4=success_time4+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult4.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time4=fail_time4+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time4 == iterationNum:
                    Bleach_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Bleach effect success:%d fail:%d iteration:%d'%(success_time4,fail_time4,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult4)
                send_key(KEY_BACK)
                sleep(2)               
        '''
        Instant effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Instant effect iteration %d'%(i+1))
                    Instant_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("None"), True, 5):
                            drag_by_param(95, 88, 0, 88, 10)
                            sleep(2)
                        if wait_for_fun(lambda:search_view_by_desc("Instant"), True, 5):
                            click(151, 2031)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Instant effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult5.append('%d.Pass'%(i+1))
                        success_time5=success_time5+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult5.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time5=fail_time5+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time5 == iterationNum:
                    Instant_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Instant effect success:%d fail:%d iteration:%d'%(success_time5,fail_time5,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult5)
                send_key(KEY_BACK)
                sleep(2) 
        '''
        Latte effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Latte effect iteration %d'%(i+1))
                    Latte_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("None"), True, 5):
                            drag_by_param(95, 88, 0, 88, 10)
                            sleep(2)
                        if wait_for_fun(lambda:search_view_by_desc("Latte"), True, 5):
                            click(416, 2006)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Latte effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult6.append('%d.Pass'%(i+1))
                        success_time6=success_time6+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult6.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time6=fail_time6+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time6 == iterationNum:
                    Latte_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Latte effect success:%d fail:%d iteration:%d'%(success_time6,fail_time6,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult6)
                send_key(KEY_BACK)
                sleep(2)
        '''
        Blue effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Blue effect iteration %d'%(i+1))
                    Blue_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("None"), True, 5):
                            drag_by_param(95, 88, 0, 88, 10)
                            sleep(2)
                            click(704, 2001)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Blue effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult7.append('%d.Pass'%(i+1))
                        success_time7=success_time7+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult7.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time7=fail_time7+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time7 == iterationNum:
                    Blue_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Blue effect success:%d fail:%d iteration:%d'%(success_time7,fail_time7,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult7)
                send_key(KEY_BACK)
                sleep(2)
        '''
        Litho effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('Litho effect iteration %d'%(i+1))
                    Litho_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("None"), True, 5):
                            drag_by_param(95, 88, 0, 88, 10)
                            sleep(2)
                        if wait_for_fun(lambda:search_view_by_desc("Litho"), True, 5):
                            click(998, 2046)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "Litho effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult8.append('%d.Pass'%(i+1))
                        success_time8=success_time8+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult8.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time8=fail_time8+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time8 == iterationNum:
                    Litho_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Litho effect success:%d fail:%d iteration:%d'%(success_time8,fail_time8,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult8)
                send_key(KEY_BACK)
                sleep(2)
        '''
        XProcess effect
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        camera.take_picture()
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 8):
            log_test_framework("step2:", "take snapshot pass")
            if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                click_imageview_by_id("preview_thumb")
                for i in range(iterationNum):
                    print_log_line('XProcess effect iteration %d'%(i+1))
                    XProcess_flag = False
                    success_flag = False                  
                    if wait_for_fun(lambda:search_view_by_id("photopage_bottom_control_edit"), True, 5):
                        click_imageview_by_id("photopage_bottom_control_edit")
                        if wait_for_fun(lambda:search_view_by_desc("None"), True, 5):
                            drag_by_param(95, 88, 0, 88, 10)
                            sleep(2)
                        if wait_for_fun(lambda:search_view_by_desc("X Process"), True, 5):
                            click(1272, 2026)
                            if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                                click_textview_by_id("filtershow_done")
                                if search_text("Close app", searchFlag=TEXT_CONTAINS)==False:
                                    log_test_framework("step3:", "XProcess effect pass")
                                    success_flag = True
                                    sleep(10)
                                    click(709, 1037)
                    if success_flag == True:
                        testresult9.append('%d.Pass'%(i+1))
                        success_time9=success_time9+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult9.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time9=fail_time9+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
                        if wait_for_fun(lambda:search_view_by_id('preview_thumb'), True, 5):
                            click_imageview_by_id("preview_thumb")                                          
                if success_time9 == iterationNum:
                    XProcess_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'XProcess effect success:%d fail:%d iteration:%d'%(success_time9,fail_time9,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult9)
                send_key(KEY_BACK)
                sleep(2)
        case_flag = Punch_flag and Vintage_flag and BW_flag and Bleach_flag and Instant_flag and Latte_flag and Blue_flag and Litho_flag and XProcess_flag        
        if search_text("isn't responding", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs ANR")            
            take_screenshot()
            if search_text("Close app", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                sleep(2)
            if search_text("Close", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close")
                sleep(2)            
        elif search_text("Unfortunately", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs crash")
            take_screenshot()
            if search_text("OK", searchFlag=TEXT_CONTAINS):
                click_button_by_text("OK")
                sleep(2)
            if search_text("Close", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close")
                sleep(2)            
        elif search_text("stopped", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Popup has stopped")
            take_screenshot()
            if search_text("Close", searchFlag=TEXT_CONTAINS):
                click_button_by_text("Close")
                sleep(2)            
            if search_text("OK", searchFlag=TEXT_CONTAINS):
                click_button_by_text("OK")
                sleep(2)       
        elif search_text("Close app", searchFlag=TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Popup Close app error")
            take_screenshot()            
            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
            sleep(2)        
        send_key(KEY_BACK)
        sleep(1)
        send_key(KEY_BACK)
        sleep(1)
        send_key(KEY_HOME)
        sleep(1)                
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
            
