'''
    shard library of weibo module

    This module used to provide functions for weibo,such as: login to weibo, share with weibo.
    We integrate such functions here ,all cases can use it freely.

    1.How to use it in case:

     >>> from qrd_shared.weibo.Weibo import Weibo
     >>> weibo = Weibo()
     >>> weibo.share_with_weibo()

    More shared functions of weibo can be added here,any modification
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
import time

class Weibo(Base):
    '''
    Weibo will provide common weibo related functions for all
    cases ,such as login to weibo, share with weibo and so on.
    '''
    def __init__(self):
        self.mode_name = "weibo"
        Base.__init__(self,self.mode_name)
        self.ime = IME()
        self.debug_print( 'Base init:%f' %(time.time()))

    #input: be sure the weibo app have started, but not sure where it is or whether it have logined ?
    #output: return true or false .
    def is_login(self):
        '''
        judge current whether it has logined.
        if the current activity is not in the switch user activity, we will think it has logined.

        @return: True, if it has logined,otherwise , False
        '''
        activityName = get_activity_name()
        if activityName == 'com.sina.weibo.SwitchUser':
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
        #focus on the login input box
        click_textview_by_id('etLoginUsername', 1, 0)
        self.ime.IME_input(1,SC.PRIVATE_WEIBO_ACCOUNT_SEQUENCE)

        drag_by_param(90,10,95,15,1)
        #focus in the password input box
        click_textview_by_id('etPwd', 1, 0)
        sleep(1)
        self.ime.IME_input(1,SC.PRIVATE_WEIBO_PASSWORD_SEQUENCE)
        click_button_by_id('bnLogin')
        loginActivity = "com.sina.weibo.SwitchUser"
        #wait the login activity disapper
        waitActivity = lambda:get_activity_name() == loginActivity
        return wait_for_fun(waitActivity, False, 15)

    #input: make sure the weibo app is running.
    #output: if the surrent page is in Navigater, it will drag to enter the home page .otherwise, will do nothing.
    def skip_navigator(self):
        '''
        skip the navigator.
        '''
        activityName = get_activity_name()
        if activityName == 'com.sina.weibo.NavigateViewPageActivity':
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            if search_view_by_id('iv_skip_btn'):
                click_imageview_by_id('iv_skip_btn')

            #cancel to share to friends
            if search_view_by_id('ivNavigater_selection'):
                click_imageview_by_id('ivNavigater_selection')
            #begin weibo
            if search_view_by_id('ivNavigater_clickable'):
                click_imageview_by_id('ivNavigater_clickable')
                sleep(4)

    #input: viewing a picture
    #output:back to the camera app
    def share_with_weibo(self,message):
        '''
        share with weibo.
        @note: Be sure it is in the viewing picture interface

        @type message:string
        @param message:the message want to share with weibo
        '''
        shareWithWeibo = self.get_value('share_to_weibo')

        if search_view_by_desc(self.get_value('default_share_to_weibo')):
            click_view_by_container_id('default_activity_button','android.widget.ImageView',0)
        else:
            click_imageview_by_desc(self.get_value('share_object'))
            #click the text sell all
            if wait_for_fun(lambda:search_text(self.get_value('see_all'), searchFlag=TEXT_CONTAINS), True, 3):
                click_textview_by_text(self.get_value('see_all'))
            if search_text(shareWithWeibo):
                click_textview_by_text(shareWithWeibo)
            else:
                log_test_case(self.mode_name, 'Can not find the weibo')
                return False
        sleep(1)
        waitActivity = lambda:get_activity_name().startswith("com.sina.weibo")
        if not wait_for_fun(waitActivity, True, 20):
            return False
        if not self.is_login():
            self.login()
        sleep(2)
        return self.share_with_weibo_inner(message)

    #input: in the post page
    #output:cose the post page
    def share_with_weibo_inner(self,message):
        '''
        share with weibo.
        @note: Be sure it is in the write message interface

        @type message:string
        @param message:the message want to share with weibo
        '''
        waitBlog = lambda:search_view_by_id("et_mblog")
        if not wait_for_fun(waitBlog, True, 10):
            start_activity("com.sina.weibo", ".EditActivity")
        #enter the message
        click_textview_by_id('et_mblog', 1, 0)
        sleep(1)
        self.ime.IME_input(1,message,'c')
        sleep(1)
        #click the delete position button(textView)
        #click_textview_by_text(self.get_value('send'))
        click_textview_by_id("titleSave")

        waitActivity = lambda:get_activity_name() == "com.sina.weibo.EditActivity"
        if not wait_for_fun(waitActivity, False, 20):
            # if the editActivity is still alive , close it
            loopTimes = 0
            while loopTimes < 5:
                if search_text(self.get_value('same_draf_tip'), 1, 0):
                    click_button_by_text(self.get_value('cancel'))
                    break
                else:
                    goback()
                loopTimes = loopTimes + 1
            log_test_case(self.mode_name, 'Cancel post the weibo status')
            return False
        return True