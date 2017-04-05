'''
    shard library of camera module

    This module used to provide functions for camera,such as: switch the camera between background and foreground;
    take picture, take video and so on .We integrate such functions here ,all cases can use it freely.

    1.How to use it in case:

     >>> from qrd_shared.camera.Camera import Camera
     >>> camera = Camera()
     >>> camera.switch_2_video_mode()

    More shared functions of camera can be added here,any modification
    here must guarantee the api not change since it may be used by cases not in your scope.


    @author: U{c_lqiang<c_lqiang@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @note:
    @attention:
    @bug:
    @warning:


'''
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
import time
from _ctypes_test import func
class Camera(Base):
    '''
    Camera will provide common camera related functions for all
    cases ,such as switch camera between background and foreground, take picture, take video and so on.
    '''

    def __init__(self):
        self.mode_name = "camera"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))

    #input: the camera is running.
    #output: switch to the camera mode
    def switch_2_camera_mode(self):
        '''
        swtich to the camera mode.
        '''
        #switch to video mode
        click_imageview_by_id('mode_1')
        #select the video mode
        click_imageview_by_id('mode_camera') #mode_video, mode_panorama, mode_camera
        sleep(3)

    #input: the camera is running.
    #output: switch to the video mode
    def switch_2_video_mode(self):
        '''
        switch to the video mode.
        '''
        #switch to video mode
        click_imageview_by_id('mode_0')
        #select the video mode
        click_imageview_by_id('mode_video') #mode_video, mode_panorama, mode_camera
        sleep(3)

    #input: the camera is running.
    #output: switch to the panorama mode
    def switch_2_panorama_mode(self):
        '''
        switch to the panorama mode.
        '''
        #switch to video mode
        click_imageview_by_id('mode_2')
        #select the video mode
        click_imageview_by_id('mode_panorama') #mode_video, mode_panorama, mode_camera
        sleep(3)

    #input: the camera is running.
    #output: switch to the background camera
    def switch_2_background_camera(self):
        '''
        switch to the background camera.
        '''
        #switch to the camera mode
        self.switch_2_camera_mode()
        #if the flash icon is not exist, it means need to click the switch button
        if not self.is_background_camera():
            click_imageview_by_id('camera_picker')
        sleep(1)

    #input: the camera is running.
    #output: switch to the foreground camera
    def switch_2_foreground_camera(self):
        '''
        switch to the foreground camera.
        '''
        #switch to the camera mode
        self.switch_2_camera_mode()
        #if the flash icon is exist, it means need to click the switch button
        if self.is_background_camera() == True:
            click_imageview_by_id('camera_picker')
        sleep(1)

    #input: the camera is running.
    #output: check the camera whether it is background camera or foreground camera
    def is_background_camera(self):
        '''
        check whether it is on background camera
        '''
        #open the second level settings
        click_imageview_by_id('second_level_indicator')

        result = search_view_by_desc(self.get_value('flash_mode'))
        click_imageview_by_id('back_to_first_level')
        sleep(1)
        return result

    #input: the camera is running.
    #output: take a picture
    def take_picture(self):#c_caijie
        '''
        take a picture.

        @note: How to check whether it is success?
        we just to check the count of the picture in /storage/sdcard0/DCIM/camera.
        if the count is greater than before take picture, it is success.

        @return: True, if take picture success, otherwise, return False
        '''
        osInfo = get_platform_info()
        if(osInfo == 'Linux-Phone'):
            beforePictures = os.listdir(os.sep+'sdcard'+os.sep+'DCIM'+os.sep+'Camera'+os.sep)
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
            click_imageview_by_id('shutter_button')
            sleep(4)

        if(osInfo == 'Linux-Phone'):
            afterPictures = os.listdir(os.sep+'sdcard'+os.sep+'DCIM'+os.sep+'Camera'+os.sep)
            if(len(afterPictures) > len(beforePictures)):
                return True            
            else:
                return False
        else:
            return True

    #input: the camera is running.
    #output: take a video
    #params: @second the time nof the video
    def take_video(self,sleeptime):
        '''
        take a video of custom time.

        @type second:int
        @param second:second time of video
        '''
        osInfo = get_platform_info()
        if(osInfo == 'Linux-Phone'):
            beforeFiles = os.listdir(os.sep+'sdcard'+os.sep+'DCIM'+os.sep+'Camera'+os.sep)
        if wait_for_fun(lambda:search_view_by_id('video_button'), True, 5):
            click_imageview_by_id('video_button')
        if wait_for_fun(lambda:search_view_by_id('recording_time'), True, 5):
            sleep(sleeptime)
        if wait_for_fun(lambda:search_view_by_id('video_button'), True, 5):
            click_imageview_by_id('video_button')
            sleep(4)
        if(osInfo == 'Linux-Phone'):
            afterFiles = os.listdir(os.sep+'sdcard'+os.sep+'DCIM'+os.sep+'Camera'+os.sep)
            if(len(afterFiles) > len(beforeFiles)):
                return True
            else:
                return False
        else:
            return True

    def take_video_camera1(self,sleeptime):
        '''
        take a video of custom time.

        @type second:int
        @param second:second time of video
        '''
        osInfo = get_platform_info()
        if(osInfo == 'Linux-Phone'):
            beforeFiles = os.listdir(os.sep+'sdcard'+os.sep+'DCIM'+os.sep+'Camera'+os.sep)
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
            click_imageview_by_id('shutter_button')
            if wait_for_fun(lambda:search_view_by_id('recording_time'), True, 5):
                sleep(sleeptime)
                if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
                    click_imageview_by_id('shutter_button')
            sleep(4)
        if(osInfo == 'Linux-Phone'):
            afterFiles = os.listdir(os.sep+'sdcard'+os.sep+'DCIM'+os.sep+'Camera'+os.sep)
            if(len(afterFiles) > len(beforeFiles)):
                return True
            else:
                return False
        else:
            return True

    #input: the camera is not running(or not in the foreground).
    #output: take a picture
    def take_picture_alone(self):
        '''
        take a picture along. it means, no need the camera application is opening.
        and we will start the camera application, and take a picture
        '''
        start_activity('com.android.gallery3d','com.android.camera.Camera')
        sleep(2)
        result = self.take_picture()
        goback()
        return result

    #input: the camera is not running(or not in the foreground).
    #output: take a video
    #params: @second the time nof the video
    def take_video_alone(self,second):
        '''
        take a video along. it means, no need the camera application is opening.
        and we will start the camera application, and take a video of custom second time.

        @type second:int
        @param second:second time of video
        '''
        start_activity('com.android.gallery3d','com.android.camera.Camera')
        sleep(2)
        self.switch_2_video_mode()
        result = self.take_video(second)
        goback()
        return result

    #get a picture by camera,for example,add a picture as attach file in mms.
    def get_picture_by_camera(self):
        '''
        using the camera to take a picture and return to the next application.

        @note: if need to choose one of the camera ,
        we will choose the fist camera , and click the "Only once".
        so , we don`t change the default camera.
        '''
        if search_text('Remember photo locations',searchFlag=TEXT_CONTAINS):
            log_test_case( self.mode_name, 'it indicated that we are first time to use camera module')
            click_button_by_text('No thanks')
        '''
        if search_text(self.get_value("action_using")):
            click_textview_by_id("text1")
            click_button_by_id("button_once")
        '''
        sleep(2)
        click_button_by_id("shutter_button")
        if wait_for_fun(lambda:search_view_by_id("btn_done"), True, 10):
            click_button_by_id("btn_done")
            return True
        return False

    def remember_photo_locations(self, remember):
        '''
        whether remember photo locations, this prompt dialog will popup when camera app launch at the first time.

        @type remember: boolean
        @param remember: whether remember photo locations. default is not remrember.
        '''
        fun1 = lambda:search_text(self.get_value("remember_photo_locations"))
        if wait_for_fun(fun1, True,  5):
            click_textview_by_text(self.get_value("yes")) if remember else click_textview_by_text(self.get_value("no_thanks"))
        else:
            pass
    def take_panorama_picture(self):#c_caijie
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 5):
            click_imageview_by_id('camera_switcher')
        if wait_for_fun(lambda:search_view_by_desc("Switch to panorama"), True, 5):
            click_imageview_by_desc('Switch to panorama')
            if wait_for_fun(lambda:search_view_by_id("shutter_button"), True, 5):
                click_button_by_id('shutter_button')
                if wait_for_fun(lambda:search_view_by_id("shutter_button"), True, 5):
                    sleep(2)
                    click_button_by_id('shutter_button')
