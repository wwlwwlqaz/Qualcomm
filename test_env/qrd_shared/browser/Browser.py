'''
   shared library of browser module.

   This class will provide operations api for browser application.

   1.Developer can directly call those api to perform some operation.Such as:

     from qrd_shared.case import *
     case_flag = browser.access_browser(SC.PRIVATE_BROWSER_ADDRESS_URL, SC.PRIVATE_BROWSER_WEB_TITLE, SC.PRIVATE_BROWSER_WAIT_TIME)

   2.Developer can modify api or add some new api here. Before it, please make sure have been
     familiar with the structure.Modify existed api,please notice it won't affect others caller.


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see:
   @note:
   @attention:
   @bug:
   @warning:



'''

from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
import time
from qrd_shared.ime.IME import IME
from qrd_shared.case import *
from qrd_shared.phone.Phone import Phone

class Browser(Base):
    '''
    Browser is a class for operating Browser application.

    @see: L{Base <Base>}
    '''
    def __init__(self):
        '''
        init function.

        @see: L{Base <Base>}
        '''
        self.mode_name = "browser"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))

    #check whether access url successfully
    #url_address: url address
    #check_value: when need check whether access successfully, this is the check value
    #wait_time: when check access , the wait time
    #is_checked: whether check to access successfully
    def access_browser(self, url_address, check_value, wait_time, is_checked=True):
        '''
        check whether access url successfully

        @type url_address: string
        @param url_address: url address.
        @type check_value: string
        @param check_value: when need check whether access successfully, this is the check value.
        @type wait_time: number
        @param wait_time: when check access , the wait time.
        @type is_checked: boolean
        @param is_checked: whether check to access successfully.
        @return: True: access successful; False: no.
        '''
        search_result = False
        ime = IME()

        if is_checked == True:
            #clear the browser cache
            self.clear_cache()
        #click_imageview_by_id('tab_switcher')
        #addressing config web address
        #entertext_edittext_by_id('url', url_address)
        sleep(1)
        click_textview_by_id('url', clickType=LONG_CLICK)    #this can
        #send_key(KEY_DEL)
        #modified by c_yazli
        sleep(1)
        click_button_by_id('clear',isVerticalList=0, isScrollable=1)
        #entertext_edittext_by_index(0, url_address)
        entertext_edittext_on_focused(url_address)
        send_key(KEY_ENTER)
        '''click_textview_by_id("url")
        send_key(KEY_DEL)
        #input address url
        ime.IME_input(1,url_address)'''

        #make sure whether access successful
        if is_checked == True:
            scroll_down()
            wait_fun = lambda: search_view_by_id("favicon")
            wait_result = wait_for_fun(wait_fun,True,wait_time)

            if wait_result == True:

                start_time = int(time.time())
                while int(time.time()) - start_time < int(wait_time):
                    click_button_by_id("favicon")
                    if search_text(unicode(check_value),searchFlag=TEXT_CONTAINS):
                        search_result =  True
                        break
                    elif search_text(self.get_value("webpage_not_available")):
                        search_result =  False
                        break
                    else:
                        sleep(1)
                    goback()
            else:
                search_result =  False
        else:
            if search_text(url_address):
                search_result =  True
            else:
                search_result =  False

        return search_result

    def clear_cache(self):
        '''
        clear the browser cache

        '''
        #clear the browser cache
        sleep(1)
        #click_menuitem_by_text(self.get_value("menu_preferences"))
        click_button_by_id('more_browser_settings')
        sleep(1)
        click_textview_by_text('Settings',isScrollable=1)
        sleep(1)
        click_textview_by_text(self.get_value("pref_privacy_security_title"))
        sleep(1)
        click_textview_by_text(self.get_value("pref_privacy_clear_cache"))
        sleep(1)
        click_textview_by_text(self.get_value("pref_privacy_clear_cache_data"))

        if search_text(self.get_value("dialog_ok_button")):
            click_button_by_text(self.get_value("dialog_ok_button"))

        goback()
        goback()
        goback()
        goback()
        # add by huitingn
        if is_view_enabled_by_text(VIEW_TEXT_VIEW,'Version') and is_view_enabled_by_text(VIEW_TEXT_VIEW,'General'):
            click_imageview_by_desc('Navigate up')

    #check google account automatic signing
    #check connection problem
    def pre_check(self):
        '''
        check google account automatic signing and connection problem when could happen after launcher browser.

        '''
        sleep(1)

        #check google account automatic signing
        if search_text(self.get_value("google_account_auto_connection"),1,0) == True:
            goback()

        #check connection problem
        if search_text(self.get_value("Connection_problem"),1,0) == True:
            goback()
            
    
    def close_other_tabs(self,left=1):
        sleep(1)
    
        windowNum = get_view_text_by_id(VIEW_TEXT_VIEW, 'tab_switcher_text')
        windowNum = int(windowNum)
    
        if windowNum>left:
            click_imageview_by_id('tab_switcher')
            for i in range(windowNum-left):
                click_imageview_by_id('closetab')
                if left>0:click_imageview_by_id('tab_view') # now should be just 1 window in browser  
                
    def exit_browser(self):#c_caijie
        send_key(KEY_BACK)
        sleep(2)
        send_key(KEY_BACK)
        sleep(3)
        if search_text('QUIT'):
            click_textview_by_text('QUIT')
            sleep(5)
        send_key(KEY_HOME)
        sleep(2)

    def browser_baidu(self):#c_caijie
        phone = Phone()
        start_activity("com.android.browser", "com.android.browser.BrowserActivity")
        sleep(10)
        phone.permission_allow()
        start_activity("com.android.browser", "org.chromium.chrome.browser.ChromeTabsbedActivity")
        sleep(30)
        phone.permission_allow()
        if search_text('Accept & continue'):
            click_textview_by_text('Accept & continue')
            sleep(5)                
        if search_view_by_id('url'):
            click_textview_by_id('url')
            sleep(5)
            send_key(KEY_DEL)
            entertext_edittext_by_id('url','http://www.baidu.com')
            sleep(10)
            send_key(KEY_ENTER)
            sleep(60)
        if search_view_by_id('url_bar'):
            click_textview_by_id('url_bar')
            sleep(5)
            send_key(KEY_DEL)
            entertext_edittext_by_id('url_bar','http://www.baidu.com')
            sleep(10)
            send_key(KEY_ENTER)
            sleep(60)            