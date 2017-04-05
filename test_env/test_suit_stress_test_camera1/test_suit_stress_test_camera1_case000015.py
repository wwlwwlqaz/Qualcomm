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



class test_suit_stress_test_camera1_case000015(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch Camera;
    Step2:go to scene mode, and traverse every scene to take picture for 50 time 
    Verification: 
    ER2:No crash   
    '''
    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG, testresult, success_flag, i, success_time1, success_time2, success_time3, success_time4, success_time5, success_time6, success_time7, success_time8, success_time9, success_time10, success_time11, success_time12, ubifocus_flag, optizoom_flag, portrait_flag, landscape_flag, sports_flag, flowers_flag, backlight_flag, candlelight_flag, sunset_flag, night_flag, beach_flag, snow_flag
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
        iterationNum = 50
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
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)            
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
        Flowers mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)             
            if wait_for_fun(lambda:search_text("Flowers"), True, 5):
                click_textview_by_text("Flowers")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")                 
                for i in range(iterationNum):
                    print_log_line('Flowers mode iteration %d'%(i+1))
                    flowers_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Flowers mode and take picture pass")
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
                    flowers_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Flowers success:%d fail:%d iteration:%d'%(success_time6,fail_time6,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult6)        
        '''
        Backlight mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)
            if wait_for_fun(lambda:search_text("Backlight"), True, 5):
                click_textview_by_text("Backlight")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")                 
                for i in range(iterationNum):
                    print_log_line('Backlight mode iteration %d'%(i+1))
                    backlight_flag = False
                    success_flag = False                    
                    camera.take_picture()
                    if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                        log_test_framework("step2:", "go to Backlight mode and take picture pass")
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
                    backlight_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Backlight success:%d fail:%d iteration:%d'%(success_time7,fail_time7,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult7)        
        '''
        Candlelight mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)
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
                    candlelight_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Candlelight success:%d fail:%d iteration:%d'%(success_time8,fail_time8,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult8)          
        '''
        Sunset mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)
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
                    sunset_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Sunset success:%d fail:%d iteration:%d'%(success_time9,fail_time9,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult9) 
        '''
        Night mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)
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
                    night_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Night success:%d fail:%d iteration:%d'%(success_time10,fail_time10,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult10) 
        '''
        Beach mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2) 
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
                    beach_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Beach success:%d fail:%d iteration:%d'%(success_time11,fail_time11,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult11) 
        '''
        Snow mode
        '''
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher")
            sleep(2)            
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)
            drag_by_param(10, 90, 10, 0, 10)
            sleep(2)                        
            if wait_for_fun(lambda:search_text("Snow", isVerticalList=0), True, 5):
                click_textview_by_text("Snow")
                if wait_for_fun(lambda:search_text("OK"), True, 5):
                    click_button_by_text("OK")                 
                for i in range(iterationNum):
                    print_log_line('Snow mode iteration %d'%(i+1))
                    snow_flag = False
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
                    snow_flag = True
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Snow success:%d fail:%d iteration:%d'%(success_time12,fail_time12,iterationNum))
                print_log(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], testresult12) 
               
        case_flag = ubifocus_flag and optizoom_flag and portrait_flag and landscape_flag and sports_flag and flowers_flag and backlight_flag and candlelight_flag and sunset_flag and night_flag and beach_flag and snow_flag                                       
        
        start_activity('org.codeaurora.snapcam','com.android.camera.CameraLauncher')                      
        if wait_for_fun(lambda:search_view_by_id('scene_mode_switcher'), True, 8):
            click_imageview_by_id("scene_mode_switcher") 
            if wait_for_fun(lambda:search_text("Automatic"), True, 5):
                click_textview_by_text("Automatic")
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
            
