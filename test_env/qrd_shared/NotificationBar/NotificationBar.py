'''
    share others NotificationBar two api:

    1.check the notificationBar find somethings api,
    drag down the notificationBar, check the text keywords.if find,click it.

    2.register handler api,
    register handler for special, drag down the notificationBar, check the text title or packagename,if find it,return handler.

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @note:
    this is demo to how to use the register_NotificationBar_Event/ DragDownAndProcess
    def_demo_register(self):
    fun = lambda:search_view_by_id("btn_done")
    title = 'USB'
    notificationBar.register_NotificationBar_Event('package_name.android.mms', title , fun)
    ...
    ...
    ...
    def_get_handler_register(title):
    action = notificationBar.check_register_event(title)

    @bug:
    @warning:
    @attention:
    @todo: if system notification bar event is able to get in future the callback function should be call auto.

'''

from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
import time

class NotificationBar(Base):

    def __init__(self):
        """
        This function init share notificationbar api class.
        @return:  none
        """

        self.mode_name = "notificationBar"
        self.tag = 'qrd_share_notification_bar'
        Base.__init__(self, self.mode_name)
        self.debug_print('notification_bar init:%f' % (time.time()))
        #self.register_event_total
        self.register_event = []

    def drag_down(self):
        """
        This function drag down the notification bar.
        @return:  none
        """
        drag_by_param(50, 0, 50, 90, 10)

    def check_email(self):
        """
        if found the gmail.click gmail text
        @return:  none
        """

        self.drag_down()
        gmailcom = self.get_value("gmail")
        if search_text(gmailcom):
            click_textview_by_text(gmailcom)
            sleep(5)
        else:
            goback()

    def check_miss_call(self):
        """
        if found missed call , click it.
        @return:  none
        """

        self.drag_down()
        missedcall = self.get_value("MissedCall")
        if search_text(missedcall):
            click_textview_by_text(missedcall)
            sleep(3)
        else:
            goback()

    def clear_all(self):
        """
        clear all the notification Bar
        @return:  none
        """

        self.drag_down()
        '''
        if search_view_by_id('clear_all_button'):
            click_imageview_by_id('clear_all_button')
        '''
        # modified by huitingn for AndroidL
        if search_view_by_id(self.get_value('clear_all_button')):
            click_imageview_by_id(self.get_value('clear_all_button'))
        else:
            self.debug_print('notification_bar no clear all,go back')
            goback()
        sleep(1)

    def enter_setting(self):
        """
        from notification bar enter setting activity.
        @return:  none
        """

        self.drag_down()
        click_imageview_by_id('settings_button')

    def new_message(self):
        """
        check whether new message,if yes, open it
        @return:  none
        """

        self.drag_down()
        newmessage = self.get_value('NewMessage')
        if search_text(newmessage):
            click_textview_by_text(newmessage)
            sleep(3)
        else:
            goback()




    def register_NotificationBar_Event(self, package_name, title, action):
        """
        This function register action fun for special title.when title is show in notificationBar,the registered action fun would be gotten.
        in fact register process is very simple:
        1. (package_name, title, action) three element make a  dict.
        2. save the dict.

        @type  title: string
        @param title: for find the action. search keyword,for example: 'USB','New email'...
        @type  package_name: string
        @param package_name: for find the action. search keyword,for special if title not enough pick up the action.
        @type  action: string
            if callback function, the debug veiw show address string.
        @param action: generally it is callback function.
        @return:  none
        """

        assert_type_string(package_name)
        assert_type_string(title)
        assert_type_string(action)
        obj = { 'p': package_name, 't': title , 'a': action }
        self.register_event.append(obj)

    def check_register_event(self, title):
        """
        This function return the registered action fun when title is show in notificationBar by checking the saved dict .
        @type  title: string
        @param title: for find the action. search keyword,for example: 'USB','New email'...
        @return:  registered action before.
        generally it is callback function.
        """

        self.drag_down()
        if search_text(title) :
            for x in self.register_event :
                #if (search_view_by_desc(x.package_name) and search_text(x.t)):
                if (title == x['t']):
                    self.debug_print('notification_ find event')
                    log_test_case("register", 'find ')
                    return x['a']
        self.debug_print('notification_ not found event')
        return
    
    def airplane_mode(self,switch='off'):
        """
        Turn on or turn off the airplane mode.
        author:huitingn@qualcomm.com
        
        @type switch: string
        @param switch: 'off' or 'on'
        """
        self.drag_down()
        mode = get_view_text_by_id(VIEW_TEXT_VIEW,'subs_label',isScrollable=0)
        if (switch=='off' and is_view_enabled_by_text(VIEW_TEXT_VIEW,'Airplane Mode',isScrollable=0) ) \
        or (switch=='on' and not is_view_enabled_by_text(VIEW_TEXT_VIEW,'Airplane Mode',isScrollable=0) ):
            scroll_down()
            click_textview_by_text('Airplane mode')
            goback()
            
        goback()
    
    
        
