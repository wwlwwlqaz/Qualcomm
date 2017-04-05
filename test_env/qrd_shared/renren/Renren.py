'''
    shard library of renren module

    This module used to provide functions for renren,such as: login to renren, share with renren.
    We integrate such functions here ,all cases can use it freely.

    1.How to use it in case:

     >>> from qrd_shared.renren.Renren import Renren
     >>> renren = Renren()
     >>> renren.share_with_renren()

    More shared functions of renren can be added here,any modification
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
from qrd_shared.ime.IME import IME
import settings.common as SC
from logging_wrapper import log_test_case
import time

class Renren(Base):
    '''
    Renren will provide common renren related functions for all
    cases ,such as login to renren, share with renren and so on.
    '''
    welcome_activity = 'com.renren.mobile.android.loginfree.WelcomeActivity'
    ''' The class name of the welcome activity '''
    login_activity = 'com.renren.mobile.android.ui.Login'
    ''' The class name of the login activity '''
    welcome_screen = 'com.renren.mobile.android.ui.WelcomeScreen'
    ''' The class name of the welcome screen '''
    def __init__(self):
        self.mode_name = "renren"
        Base.__init__(self,self.mode_name)
        self.ime = IME()
        self.debug_print( 'Base init:%f' %(time.time()))

    #input: be sure the weibo app have started, but not sure where it is or whether it have logined ?
    #output: return true or false .
    def is_login(self):
        '''
        judge current whether it has logined.
        if the current activity is not in the welcome activity , login activity or welcome screen, we will think it has logined.

        @return: True, if it has logined,otherwise , False
        '''
        activityName = get_activity_name()
        if activityName == self.welcome_activity or activityName == self.login_activity or activityName == self.welcome_screen:
            return False
        return True

    #input: the page is in the login page
    #output: just enter the email and password and press the login button,and try to wait for 5 seconds.
    #        if the activity page switched to another page in the 5 seconds, we assume  success
    def login(self):
        '''
        enter the account information and login to the main interface

        @return: True, if it login successfully,otherwise , False
        '''
        activityName = get_activity_name()
        if activityName == self.welcome_activity:
            click_imageview_by_id('welcome_login')
        if activityName == self.welcome_screen:
            click_imageview_by_id('welcome_login')
        #clear the account
        clear_edittext_by_id('account_layout')
        #focus on the login input box
        click_textview_by_id('account_layout', 1, 0)
        sleep(1)
        self.ime.IME_input(1,SC.PRIVATE_RENREN_ACCOUNT_SEQUENCE)
        #focus in the password input box
        #click_textview_by_id('password_edit', 1, 0)
        self.ime.IME_input(1,SC.PRIVATE_RENREN_PASSWORD_SEQUENCE)
        click_button_by_id('login_button')

        #wait the login activity disappear
        waitActivity = lambda:get_activity_name() == self.login_activity
        return wait_for_fun(waitActivity, False, 25)

    #input: make sure the weibo app is running.
    #output: if the surrent page is in Navigater, it will drag to enter the home page .otherwise, will do nothing.
    def skip_navigator(self):
        '''
        skip the navigator.
        '''
        activityName = get_activity_name()
        if activityName == 'com.renren.mobile.android.newfeatures.NewFeatureActivity':
            click_imageview_by_id('new_feature_btn_go')

    #input: viewing a picture
    #output:back to the camera app
    def share_with_renren(self,message):
        '''
        share with renren.
        @note: Be sure it is in the viewing picture interface

        @type message:string
        @param message:the message want to share with renren
        '''
        shareWithRenren = self.get_value('share_to_renren')

        if search_view_by_desc(self.get_value('default_share_to_renren')):
            click_view_by_container_id('default_activity_button','android.widget.ImageView',0)
        else:
            click_imageview_by_desc(self.get_value('share_object'))
            #click the text sell all
            if wait_for_fun(lambda:search_text(self.get_value('see_all'), searchFlag=TEXT_CONTAINS), True, 3):
                click_textview_by_text(self.get_value('see_all'))
            if search_text(shareWithRenren):
                click_textview_by_text(shareWithRenren)
            else:
                log_test_case(self.mode_name, 'Can not find the renren')
                return False
        sleep(1)

        waitActivity = lambda:get_activity_name().startswith("com.renren.mobile.android")
        if not wait_for_fun(waitActivity, True, 5):
            return False

        if not self.is_login():
            self.login()
        sleep(2)
        click_button_by_id('edit_photo_done')
        sleep(2)
        click_button_by_id('edit_photo_done')
        sleep(3)
        return self.share_with_renren_inner(message)

    #input: the ui is in the post page
    #output:close the post page
    def share_with_renren_inner(self,message):
        '''
        share with renren.
        @note: Be sure it is in the write message interface

        @type message:string
        @param message:the message want to share with renren
        '''
        #enter the message
        click_textview_by_id('input_editor', 1, 0)
        sleep(1)
        self.ime.IME_input(1,message,'c', 'b')
        sleep(1)
        #click the delete position button(textView)
        click_button_by_id('flipper_head_action')

        waitActivity = lambda:get_activity_name() == "com.renren.mobile.android.publisher.InputPublisherActivity"
        if not wait_for_fun(waitActivity, False, 25):
            # if the editActivity is still alive , close it
            loopTimes = 0
            while loopTimes < 5:
                if search_text(self.get_value('cancel_post_tip'), 1, 0):
                    click_button_by_text(self.get_value('ok'))
                    break
                else:
                    goback()
                loopTimes = loopTimes + 1
            log_test_case(self.mode_name, 'Cancel post the renren status')
            return False
        return True

    def exit_reren(self):
        '''
        exit the renren application .
        '''
        goback()
        goback()
        loopCount = 0
        while loopCount < 5:
            if search_text(self.get_value("sure_exit"), 1, 0):
                click_button_by_text(self.get_value('ok'))
                return
            loopCount = loopCount +1
            goback()
