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



class test_suit_stress_test_camera_case000015(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch Camera;
    Step2:go to scene mode, and traverse every scene to take picture for 100 time 
    Verification: 
    ER2:No crash   
    '''
    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG, testresult, success_flag, i, success_time1, success_time2, success_time3, success_time4, success_time5, success_time6, success_time7, success_time8, success_time9, success_time10, success_time11, success_time12, success_time13, success_time14, success_time15, success_time16, ubifocus_flag, optizoom_flag, portrait_flag, landscape_flag, sports_flag, candlelight_flag, sunset_flag, night_flag, beach_flag, snow_flag, bestpicture_flag, chromaflash_flag, blurbuster_flag, sharpphoto_flag, trackingfocus_flag, panorama_flag, promode_flag
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
        testresult10 = []
        testresult11 = []
        testresult12 = []
        testresult13 = []
        testresult14 = []
        testresult15 = []
        testresult16 = [] 
        testresult17 = []       
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
        success_time10 = 0
        fail_time10 = 0
        success_time11 = 0
        fail_time11 = 0
        success_time12 = 0
        fail_time12 = 0
        success_time13 = 0
        fail_time13 = 0
        success_time14 = 0
        fail_time14 = 0
        success_time15 = 0
        fail_time15 = 0
        success_time16 = 0
        fail_time16 = 0 
        success_time17 = 0
        fail_time17 = 0       
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
        UbiFocus mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("UbiFocus"), True, 5):
                click_textview_by_text("UbiFocus")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")                
                for i in range(iterationNum):
                    print_log_line('UbiFocus mode iteration %d'%(i+1))
                    ubifocus_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to UbiFocus mode and take picture pass")
                        success_flag = True
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
                if success_time1 == iterationNum:
                    ubifocus_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'UbiFocus success:%d fail:%d iteration:%d'%(success_time1,fail_time1,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult1)            
        '''
        OptiZoom mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("OptiZoom"), True, 5):
                click_textview_by_text("OptiZoom")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('OptiZoom mode iteration %d'%(i+1))
                    optizoom_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to OptiZoom mode and take picture pass")
                        success_flag = True
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
                if success_time2 == iterationNum:
                    optizoom_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'OptiZoom success:%d fail:%d iteration:%d'%(success_time2,fail_time2,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult2)        
        '''
        Portrait mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Portrait"), True, 5):
                click_textview_by_text("Portrait")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Portrait mode iteration %d'%(i+1))
                    portrait_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Portrait mode and take picture pass")
                        success_flag = True
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
                if success_time3 == iterationNum:
                    portrait_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Portrait success:%d fail:%d iteration:%d'%(success_time3,fail_time3,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult3)        
        '''
        Landscape mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Landscape"), True, 5):
                click_textview_by_text("Landscape")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Landscape mode iteration %d'%(i+1))
                    landscape_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Landscape mode and take picture pass")
                        success_flag = True
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
                if success_time4 == iterationNum:
                    landscape_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Landscape success:%d fail:%d iteration:%d'%(success_time4,fail_time4,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult4)        
        '''
        Sports mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Sports"), True, 5):
                click_textview_by_text("Sports")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Sports mode iteration %d'%(i+1))
                    sports_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Sports mode and take picture pass")
                        success_flag = True
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
                if success_time5 == iterationNum:
                    sports_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Sports success:%d fail:%d iteration:%d'%(success_time5,fail_time5,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult5)        
        '''
        Candlelight mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Candlelight"), True, 5):
                click_textview_by_text("Candlelight")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Candlelight mode iteration %d'%(i+1))
                    candlelight_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Candlelight mode and take picture pass")
                        success_flag = True
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
                if success_time6 == iterationNum:
                    candlelight_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Candlelight success:%d fail:%d iteration:%d'%(success_time6,fail_time6,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult6)        
        '''
        Sunset mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Sunset"), True, 5):
                click_textview_by_text("Sunset")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Sunset mode iteration %d'%(i+1))
                    sunset_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Sunset mode and take picture pass")
                        success_flag = True
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
                if success_time7 == iterationNum:
                    sunset_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Sunset success:%d fail:%d iteration:%d'%(success_time7,fail_time7,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult7)        
        '''
        Night mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Night"), True, 5):
                click_textview_by_text("Night")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Night mode iteration %d'%(i+1))
                    night_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Night mode and take picture pass")
                        success_flag = True
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
                if success_time8 == iterationNum:
                    night_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Night success:%d fail:%d iteration:%d'%(success_time8,fail_time8,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult8)          
        '''
        Beach mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Beach"), True, 5):
                click_textview_by_text("Beach")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Beach mode iteration %d'%(i+1))
                    beach_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Beach mode and take picture pass")
                        success_flag = True
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
                if success_time9 == iterationNum:
                    beach_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Beach success:%d fail:%d iteration:%d'%(success_time9,fail_time9,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult9) 
        '''
        Snow mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("Snow"), True, 5):
                click_textview_by_text("Snow")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Snow mode iteration %d'%(i+1))
                    snow_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Snow mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult10.append('%d.Pass'%(i+1))
                        success_time10=success_time10+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult10.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time10=fail_time10+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time10 == iterationNum:
                    snow_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Snow success:%d fail:%d iteration:%d'%(success_time10,fail_time10,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult10) 
        '''
        BestPicture mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_text("BestPicture"), True, 5):
                click_textview_by_text("BestPicture")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('BestPicture mode iteration %d'%(i+1))
                    bestpicture_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    sleep(15)
                    click(1380, 88)
#                     if wait_for_fun(lambda:search_view_by_id("bestpicture_done"), True, 5) or is_view_enabled_by_id(VIEW_TEXT_VIEW, "bestpicture_done"):
#                         click_textview_by_id("bestpicture_done")                       
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to BestPicture mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult11.append('%d.Pass'%(i+1))
                        success_time11=success_time11+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult11.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time11=fail_time11+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time11 == iterationNum:
                    bestpicture_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'BestPicture success:%d fail:%d iteration:%d'%(success_time11,fail_time11,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult11) 
        '''
        ChromaFlash mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")            
            if wait_for_fun(lambda:search_text("ChromaFlash", isVerticalList=0), True, 5):
                click_textview_by_text("ChromaFlash")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('ChromaFlash mode iteration %d'%(i+1))
                    chromaflash_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to ChromaFlash mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult12.append('%d.Pass'%(i+1))
                        success_time12=success_time12+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult12.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time12=fail_time12+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time12 == iterationNum:
                    chromaflash_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ChromaFlash success:%d fail:%d iteration:%d'%(success_time12,fail_time12,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult12) 
        '''
        BlurBuster mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")            
            if wait_for_fun(lambda:search_text("BlurBuster", isVerticalList=0), True, 5):
                click_textview_by_text("BlurBuster")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('BlurBuster mode iteration %d'%(i+1))
                    blurbuster_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to BlurBuster mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult13.append('%d.Pass'%(i+1))
                        success_time13=success_time13+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult13.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time13=fail_time13+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time13 == iterationNum:
                    blurbuster_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'BlurBuster success:%d fail:%d iteration:%d'%(success_time13,fail_time13,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult13)
        '''
        SharpPhoto mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")            
            if wait_for_fun(lambda:search_text("SharpPhoto", isVerticalList=0), True, 5):
                click_textview_by_text("SharpPhoto")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('SharpPhoto mode iteration %d'%(i+1))
                    sharpphoto_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to SharpPhoto mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult14.append('%d.Pass'%(i+1))
                        success_time14=success_time14+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult14.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time14=fail_time14+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time14 == iterationNum:
                    sharpphoto_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'SharpPhoto success:%d fail:%d iteration:%d'%(success_time14,fail_time14,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult14)
        '''
        TrackingFocus mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")            
            if wait_for_fun(lambda:search_text("TrackingFocus", isVerticalList=0), True, 5):
                click_textview_by_text("TrackingFocus")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('TrackingFocus mode iteration %d'%(i+1))
                    trackingfocus_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to TrackingFocus mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult15.append('%d.Pass'%(i+1))
                        success_time15=success_time15+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult15.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time15=fail_time15+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time15 == iterationNum:
                    trackingfocus_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'TrackingFocus success:%d fail:%d iteration:%d'%(success_time15,fail_time15,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult15)
        '''
        Panorama mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")            
            if wait_for_fun(lambda:search_text("Panorama", isVerticalList=0), True, 5):
                click_textview_by_text("Panorama")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('Panorama mode iteration %d'%(i+1))
                    panorama_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        click_imageview_by_id("shutter_button")
                        log_test_framework("step2:", "go to Panorama mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult16.append('%d.Pass'%(i+1))
                        success_time16=success_time16+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult16.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time16=fail_time16+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time16 == iterationNum:
                    panorama_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Panorama success:%d fail:%d iteration:%d'%(success_time16,fail_time16,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult16)
                if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
                    click_imageview_by_id("scene_mode_switcher")
                    sleep(5) 
        '''
        ProMode mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")            
            if wait_for_fun(lambda:search_text("ProMode", isVerticalList=0), True, 5):
                click_textview_by_text("ProMode")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")
                for i in range(iterationNum):
                    print_log_line('ProMode mode iteration %d'%(i+1))
                    promode_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        click_imageview_by_id("shutter_button")
                        log_test_framework("step2:", "go to ProMode mode and take picture pass")
                        success_flag = True
                    if success_flag == True:
                        testresult17.append('%d.Pass'%(i+1))
                        success_time17=success_time17+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Pass'%(i+1))
                    else:
                        testresult17.append('%d.Fail'%(i+1))
                        take_screenshot()
                        fail_time17=fail_time17+1
                        print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Fail'%(i+1))
                        if search_text("Close app", searchFlag=TEXT_CONTAINS):
                            print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%d.Popup Close app'%(i+1))
                            click_button_by_text("Close app", searchFlag=TEXT_CONTAINS)
                            sleep(2)
                        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                       
                if success_time17 == iterationNum:
                    promode_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ProMode success:%d fail:%d iteration:%d'%(success_time17,fail_time17,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult17)
               
        case_flag = ubifocus_flag and optizoom_flag and portrait_flag and landscape_flag and sports_flag and candlelight_flag and sunset_flag and night_flag and beach_flag and snow_flag and bestpicture_flag and chromaflash_flag and blurbuster_flag and sharpphoto_flag and trackingfocus_flag and panorama_flag                                       
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                      
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 5):
            click_imageview_by_id("scene_mode_switcher")
            if wait_for_fun(lambda:search_view_by_id('setting_button'), True, 5):
                click_imageview_by_id("setting_button")
                if wait_for_fun(lambda:search_text("Restore defaults", searchFlag=TEXT_CONTAINS), True, 8):
                    click_textview_by_text("Restore defaults")
                    if wait_for_fun(lambda:search_text("OK", searchFlag=TEXT_CONTAINS), True, 5):
                        click_textview_by_text("OK")
                        sleep(2)                
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
            
