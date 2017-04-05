# coding=utf-8
'''
   provide some interface of settings application.

   This class will provide operations api of settings application.

   1.Developer can directly call those api to perform some operation.

   2.Developer can add some new api.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{Base <Base>}
   @note:
   @attention:
   @bug:
   @warning:



'''
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.ime.IME import IME
from logging_wrapper import log_test_framework
import time
from qrd_shared.email.Email import Email



class Settings(Base):
    '''
    Settings is a class for operating Settings application.

    @see: L{Base <Base>}
    '''
    global TAG , count 
    '''@var count: count login,init value is 0
       @var TAG: "tag of Settings"
       @attention: modify by min.sheng,change TAG to global
    '''
    count = 0
    TAG = "Settings"
   
    
    def __init__(self):
        '''
        init method.
        '''
        self.mode_name = "settings"
        Base.__init__(self, self.mode_name)
        self.ime = IME()
        self.email = Email()
        self.debug_print('Settings init:%f' % (time.time()))

    def close_lockscreen(self):#c_caijie
        '''
        set screen lock as None.
        set screen sleep as Never.
        '''
#         drag_by_param(0, 50, 90, 50, 10)
#         sleep(2)
#         click_textview_by_text("Display")
#         sleep(2)
#         click_textview_by_text("Sleep")
#         sleep(2)
#         click_textview_by_text("30 minutes")
#         sleep(2)
#         drag_by_param(0, 50, 90, 50, 10)
#         sleep(2)
#         if search_text("Security"):
#             click_textview_by_text("Security")
#             sleep(2)
#             click_textview_by_text("Screen lock")
#             time.sleep(2)
#             click_textview_by_text("None")
#             time.sleep(2)
#         send_key(KEY_BACK)
        
        '''
        @attention: min.sheng
        @see: send_key(KEY_BACK)
        '''
        time.sleep(1)
        scroll_up()
        click_textview_by_text(self.get_value("security"))
        time.sleep(1)
        click_textview_by_text(self.get_value("screen_lock"))
        time.sleep(1)
        click_textview_by_text(self.get_value("none"))
        time.sleep(1)
        '''
        @attention: min.sheng
        @see: send_key(KEY_BACK)
        '''
        send_key(KEY_BACK)
        #click_imageview_by_index(0)

        time.sleep(1)
        scroll_up()
        #click_textview_by_text(self.get_value("display"))
        click_textview_by_text(self.get_value("display"))
        #if is_checkbox_checked_by_index(0):
        #    click_checkbox_by_index(0)
        click_textview_by_text(self.get_value("sleep"))
        time.sleep(1)
        '''
        @attention: no select "never" for M, so change to 30 minutes
        @author: min.sheng
        '''
        click_textview_by_text(self.get_value("30 minutes"))
        #click_textview_by_text(self.get_value("never"))
        time.sleep(1)
        click_imageview_by_index(0)
		
		#c_wwan
        send_key(KEY_BACK)
        if wait_for_fun(lambda:search_text("Data usage", searchFlag=TEXT_CONTAINS), True, 5):
            click_textview_by_text("Data usage")
            time.sleep(1)
            if wait_for_fun(lambda:search_text('OFF', searchFlag=TEXT_MATCHES), True, 5):
                click_button_by_id("switch_widget")
                time.sleep(1)
            else:
                pass
        send_key(KEY_BACK)
        send_key(KEY_HOME)
        time.sleep(1)		
		
    def select_language(self, lan):
        '''
        set system language.

        @type lan:string
        @param lan:: language name
        '''
        click_textview_by_index(19)
        click_textview_by_index(1)
        sleep(1)
        click_textview_by_text(lan)
        sleep(2)
        click_imageview_by_index(0)

    def enable_wifi(self, wifi_name, wifi_pwd):
        '''
        enable wifi.

        @type wifi_name: string
        @param wifi_name: wifi name
        @type wifi_pwd: tuple
        @param wifi_pwd: wifi password
        @return: whether enable wifi success
        '''
        if search_text('Wi‑Fi', searchFlag=TEXT_CONTAINS):
            click_textview_by_text('Wi‑Fi')
        else:click_textview_by_text('WLAN')
        #To see available networks
        if search_text(self.get_value("see_available_networks"), searchFlag=TEXT_CONTAINS):
            click_button_by_index(0)
            sleep(10)
        sleep(5)
        # scroll_down()
        if not search_text(wifi_name):
            click_imageview_by_index(0)
            '''
                @attention: add a log message by min.sheng
            '''
            log_test_framework(TAG, "not find the wifiname:%s"%wifi_name)
            return False
        click_textview_by_text(wifi_name)
        flag_wifi = 0
        if not wifi_pwd == "":
            if search_view_by_id("password"):
                click_checkbox_by_id('show_password')
                # entertext_edittext_by_index(0, wifi_pwd)
                click_textview_by_id("password")
                '''
                    @attention: modify by min.sheng 
                    @see: entertext_edittext_by_id('password', wifi_pwd)
                '''
                entertext_edittext_by_id('password', wifi_pwd)
                #self.ime.IME_input(1, wifi_pwd)
                # self.ime.IME_input(wifi_pwd)
                # IME.IME_input(1, wifi_pwd)
                click_button_by_text(self.get_value("connect"))
            elif search_text(self.get_value("connected")):
                flag_wifi = 1
                goback()
            elif search_text(self.get_value("forget")) and search_text(self.get_value("connect")):
                '''
                    @attention: modify by min.sheng, forget the passward and reconnect
                '''
                click_button_by_text(self.get_value("forget"))
                click_textview_by_text(wifi_name)
                click_checkbox_by_id('show_password')
                click_textview_by_id("password")
                entertext_edittext_by_id('password', wifi_pwd)
                click_button_by_text(self.get_value("connect"))
                ###click_button_by_text(self.get_value("connect"))
            else:
                log_test_framework(self.TAG, "something wrong after click wifi name.")
                goback()
                click_imageview_by_index(0)
                return False
        else:
            if search_text(self.get_value("forget")):
                goback()
        if flag_wifi == 1:
            click_imageview_by_index(0)
            return True
        sleep(10)
        click_textview_by_text(wifi_name)
        if search_text(self.get_value("connected")):
            goback()
            click_imageview_by_index(0)
            return True
        else:
            goback()
            click_imageview_by_index(0)
            return False

    def disable_wifi(self):
        '''
        disable wifi.
        '''
        click_textview_by_text(self.get_value("wifi"))
        if not search_text(self.get_value("see_available_networks"), searchFlag=TEXT_CONTAINS):
            click_button_by_index(0)
        click_imageview_by_index(0)

    def add_google_account(self, user_name, user_pwd):
        '''
        add google account.

        @type user_name: string
        @param user_name: google account name
        @type user_pwd: tuple
        @param user_pwd: google account password
        @return: whether add google account success
        '''
        click_textview_by_text(self.get_value("add_account"))
        click_textview_by_text("Google")
        click_button_by_id("next_button")
        # entertext_edittext_by_id("username_edit", user_name)
        click_textview_by_id("username_edit")
        self.ime.IME_input(1, user_name)
        # entertext_edittext_by_id("password_edit", user_pwd)
        click_textview_by_id("password_edit")
        self.ime.IME_input(1, user_pwd)
        if search_text(self.get_value("keep_me_up"), searchFlag=TEXT_CONTAINS):
            click_button_by_id("button1")
        if search_text(self.get_value("account_exsits"), searchFlag=TEXT_CONTAINS):
            log_test_framework(self.TAG, "Account already exists.")
            click_button_by_id("next_button")
            start_activity("com.android.settings", ".Settings")
            return True
        # click_button_by_id("next_button")
        if not self.re_sign_in():
            log_test_framework(self.TAG, "Couldn't sign in.")
            return False
        if search_text(self.get_value("entertainment"), searchFlag=TEXT_CONTAINS):
            click_button_by_id("skip_button")
        click_button_by_id("done_button")
        return True

    def re_sign_in(self):
        '''
        if could not sign in,sign in continuous for 3 times

        @return: whether sign in success
        '''
        flag = True
        global count
        while(flag):
            if not search_text(self.get_value("signing_in"), searchFlag=TEXT_CONTAINS):
                flag = False
        if search_text(self.get_value("could_not_sign_in"), searchFlag=TEXT_CONTAINS):
            click_button_by_id("next_button")
            click_textview_by_text(self.get_value("next"))
            count += 1
            if count == 3:
                count = 0
                return False
            self.re_sign_in()
        else:
            count = 0
            return True

    def whether_open_gps(self, open):
        '''
        open or close gps.

        @type open: boolean
        @param open: true-open gps,false-close gps
        '''
        click_textview_by_text(self.get_value("location_access"))
        if open:
            if not is_compoundbutton_checked_by_index(0):
                click_button_by_index(0)
                fun = lambda:search_view_by_id("button2")
                if wait_for_fun(fun, True, 2):
                    click_button_by_id("button2")
            else:
                if not is_checkbox_checked_by_index(0):
                    click_checkbox_by_index(0)
        else:
            if is_compoundbutton_checked_by_index(0):
                if is_checkbox_checked_by_index(0):
                    click_checkbox_by_index(0)
        click_imageview_by_index(0)

    def whether_open_mobile_data(self, open):
        '''
        open or close mobile data.

        @type open: boolean
        @param open: true-open mobile data,false-close mobile data
        '''
        if open:
            if not is_compoundbutton_checked_by_index(1):
                click_button_by_index(1)
        else:
            if is_compoundbutton_checked_by_index(1):
                click_button_by_index(1)

    def set_default_voice(self, card_id):
        '''
        set default voice.

        @type card_id: string
        @param card_id: default voice card id, 1-slot1, 2-slot2, 0-always ask
        '''
        if search_text("SIM cards"):
            click_textview_by_text("SIM cards")
            sleep(2)
        if search_text("Calls"):
            click_textview_by_text("Calls")
            sleep(1)
        if card_id == 0:
            sleep(1)
            click_in_list_by_index(0)
        elif card_id == 1:
            sleep(1)
            click_in_list_by_index(1)
        elif card_id == 2:
            sleep(1)
            click_in_list_by_index(2)
        else:
            log_test_framework(self.TAG, "card_id:" + card_id + "is error.")
        sleep(3)
        # click_imageview_by_index(0)
        #click_imageview_by_desc("Navigate up")

    def set_default_data(self, card_id):
        '''
        set default data.

        @type card_id: string
        @param card_id: default data card id, 1-slot1, 2-slot2, 0-always ask
        '''
        if search_text("SIM cards"):
            click_textview_by_text("SIM cards")
        else:
            return()
        sleep(1)
        if search_text("Mobile data"):
            click_textview_by_text("Mobile data")
        if search_text("Cellular data"):
            click_textview_by_text("Cellular data")
        if card_id == 0:
            return()
        elif card_id == 1:
            click_in_list_by_index(0)
        elif card_id == 2:
            click_in_list_by_index(1)
        else:
            log_test_framework(self.TAG, "card_id:" + card_id + "is error.")
        #click_imageview_by_index(0)
        sleep(5)

    def set_default_sms(self, card_id):#c_caijie
        '''
        set default sms.

        @type card_id: string
        @param card_id: default sms card id, 1-slot1, 2-slot2, 0-always ask
        '''
        if search_text("SIM cards"):
            click_textview_by_text("SIM cards")
            sleep(2)
        if search_text("SMS messages", searchFlag=TEXT_CONTAINS):            
            click_textview_by_text("SMS messages")
            sleep(2)
        if card_id == 0:
            click_in_list_by_index(0)
        elif card_id == 1:
            click_in_list_by_index(1)
        elif card_id == 2:
            click_in_list_by_index(2)
        else:
            log_test_framework(self.TAG, "card_id:" + card_id + "is error.")
        #click_imageview_by_index(0)
        sleep(5)

    def is_wifi_connected(self, wifi_name):
        '''
        get wifi status whether wifi is connected.

        @type wifi_name: string
        @param wifi_name: wifi name
        @return: true-if wifi_name have connected, false-if wifi_name haven't connected
        '''
        click_textview_by_text(self.get_value("wifi"))
        if search_text(self.get_value("see_available_networks"), searchFlag=TEXT_CONTAINS):
            return False
        click_textview_by_text(wifi_name)
        if not search_text(self.get_value("connected")):
            return False
        return True

    def access_to_my_location(self, access):
        '''
        whether access to my location in Location access

        @type access: boolean
        @param access: true- on,false-off
        '''
        click_textview_by_text(self.get_value("location_access"))
        if access:
            if not is_compoundbutton_checked_by_index(0):
                click_button_by_index(0)
                for i in range(0, 2):
                    fun = lambda:search_view_by_id("button1")
                    if wait_for_fun(fun, True, 2):
                        click_button_by_id("button1")
            else:
                click_button_by_index(0)
                click_button_by_index(0)
                for i in range(0, 2):
                    fun = lambda:search_view_by_id("button1")
                    if wait_for_fun(fun, True, 2):
                        click_button_by_id("button1")
        else:
            if is_compoundbutton_checked_by_index(0):
                click_button_by_index(0)
        click_imageview_by_index(0)
    
    
    def bluetooth(self, switch='on'):
        '''
        Trun on or turn off the bluetooth.
        author:huitingn@qualcomm.com

        @type switch: string
        @param switch: wifi name
        '''
        click_textview_by_text(self.get_value('bluetooth'))
        if (switch == 'on' or switch == 'enable'):
            if get_view_text_by_id(VIEW_TEXT_VIEW, 'switch_text', isScrollable=0) == 'Off':
                click_textview_by_text('Off')
                sleep(5)
        elif (switch == 'off' or switch == 'disable'):
            if get_view_text_by_id(VIEW_TEXT_VIEW, 'switch_text', isScrollable=0) == 'On':
                click_textview_by_text('On', isScrollable=0)
        else:raise ValueError(r"switch should be 'on','off' or 'enable','disable'")
        
        
    def bluetooth_pair(self):
        '''
        pair a bluetooth device.
        author:huitingn@qualcomm.com
        
        @return: True-success False-fail
        '''
        tag = r'qrd_shared/Settings/bluetooth_pair()'
        flag = False
        # pair with another device
        if not search_text('Paired devices', isScrollable=0, searchFlag=TEXT_MATCHES):
            reciver = get_view_text_by_index(VIEW_TEXT_VIEW, 5)
            # reciver = get_view_text_by_index(VIEW_TEXT_VIEW, 6)
            click_textview_by_text(reciver)
            func = lambda:search_text('Bluetooth pairing request', isScrollable=0)  # # also in slave:start #should open bt before
            if wait_for_fun(func, True, 5):
                click_button_by_text('Pair')  # # also in slave:end
                func = lambda:search_text('Paired devices', isScrollable=0, searchFlag=TEXT_MATCHES)
                if wait_for_fun(func, True, 30):
                    flag = True
                else:
                    log_test_framework(tag, "cannot pair device")
                    if search_text("Couldn't pair with", isScrollable=0):
                        click_button_by_text('OK')
        else:
            # click_imageview_by_id('icon',isScrollable=0) 
            flag = True
        
        return flag
    
    def check_carrier_sim(self,slotId):
        '''
        check the carrier of sim
        @author: min.sheng
        @type param:  slotId: string
        @param slotId: SIM1:sim1; SIM2:sim2
        '''
        start_activity('com.android.settings','.Settings')
        click_textview_by_text("SIM cards")
        sleep(2)
        click_textview_by_text(slotId)   
        sleep(2)
        carrier_result = get_view_text_by_id(VIEW_TEXT_VIEW, "carrier")
        return carrier_result
    
    def modify_sim_name(self,slotId,operation,name):
        '''
        get the name of simcard
        @author: min.sheng
        @type param:  slotId: string
        @param slotId: SIM1:sim1; SIM2:sim2
        @type operation: string
        @param operation: get:get the name   set:set the name
        @type name:string 
        @param name:  the name you want set
        '''
        start_activity('com.android.settings','.Settings')
        click_textview_by_text("SIM cards")
        sleep(2)
        click_textview_by_text(slotId)   
        sleep(2)
        if operation=="get":
            sim_name = get_view_text_by_id(VIEW_EDIT_TEXT, "sim_name")
            return sim_name
        elif operation=="set":
            entertext_edittext_by_id("sim_name", name)
            #click ok
            click_button_by_id("button1")
            
    def kill_allpid(self):
        '''
        kill current all pid
        @author: min.sheng
        '''
        send_key(KEY_HOME)
        sleep(2)
        start_activity("com.android.systemui", "com.android.systemui.recents.RecentsActivity")
        if search_text("Your recent screens appear here"):
            return
        while not search_view_by_desc("Apps"):
            if is_view_enabled_by_id(VIEW_IMAGE_VIEW, "dismiss_task"):
                log_test_framework(TAG, "found the dismiss_task")  
                click_imageview_by_id("dismiss_task",1,0)
                sleep(3)
            else:
                log_test_framework(TAG, "clear pid finished")
                return
            
    def check_after_resetphone(self):
        '''
        check some feature after reset the phone 
        @author: min.sheng
        '''
        if search_text("Close"):
            click_button_by_text("Close")
            sleep(1)
        if search_text("OK"):
            click_button_by_text("OK")
            sleep(1)
        send_key(KEY_HOME)
        sleep(1)
#         click_textview_by_desc(self.get_value('Apps list'))
#         if search_text("OK"):
#             click_button_by_text("OK")
#         send_key(KEY_HOME)
        
    def airplane_mode(self):#c_caijie
        start_activity('com.android.settings','com.android.settings.Settings')
        sleep(5)
        click_textview_by_text('More')
        sleep(3)
        click_textview_by_text('Airplane mode')
        sleep(5)
        if search_text("OK",searchFlag=TEXT_CONTAINS):
            click_button_by_id('button1')
            sleep(3)
    def cellular_networks(self):#c_caijie
        start_activity('com.android.settings','com.android.settings.Settings')
        sleep(5)
        click_textview_by_text('More')
        sleep(3)
        click_textview_by_text('Cellular networks')
        sleep(3)
        click_textview_by_text('Data roaming')
        sleep(3)      
        
        
    def set_language_to_simplified_chinese(self):#c_caijie
        click_textview_by_text("Languages & input")
        sleep(2)
        click_textview_by_text("English (United States)")
        sleep(2)
        if search_text("Add a language"):
            click_textview_by_text("Add a language")
            sleep(2)
            click_textview_by_text("简体中文（中国）")
            sleep(5)
            drag_by_param(50, 15, 0, 0, 10)
            sleep(2)  
    
    def set_language_from_chinese_to_english_us(self):#c_caijie
        click_textview_by_text("语言和输入法")
        sleep(2)
        click_textview_by_text("中文 (简体)")
        sleep(2)
        click_textview_by_text("English (United States)")
        sleep(2)
        if search_text("确定"):
            click_button_by_text("确定")
            sleep(2)                         
        
    def change_font_size_to_large(self):
        click_textview_by_text("Display")
        sleep(2)
        click_textview_by_text("Font size")
        sleep(2)
        click_button_by_index(2)
        sleep(3)

    def change_font_size_to_default(self):
        click_textview_by_text("Display")
        sleep(2)
        click_textview_by_text("Font size")
        sleep(2)
        click_button_by_index(1)
        sleep(3)   
        
    def set_wallpaper(self):
        click_textview_by_text("Display")
        sleep(2)
        click_textview_by_text("Wallpaper")
        sleep(2)
        click_textview_by_text("Snapdragon Gallery")
        sleep(2)
        click(290,539)
        sleep(2)
        click(187,392)
        sleep(2)    
        if wait_for_fun(lambda:search_view_by_id("set_wallpaper_button"), True, 5):
            click_button_by_id("set_wallpaper_button")
            if wait_for_fun(lambda:search_text("Home screen"), True, 5):
                click_textview_by_text("Home screen")     
    
    def SIM_status(self):
        click_textview_by_text("About phone")
        if wait_for_fun(lambda:search_text("Status"), True, 3):
            click_textview_by_text("Status")
            if wait_for_fun(lambda:search_text("SIM status"), True, 3):
                click_textview_by_text("SIM status") 
                
    def data_usage(self):
        click_textview_by_text("Apps")
        if wait_for_fun(lambda:search_text("Settings"), True, 3):
            click_textview_by_text("Settings")
            if wait_for_fun(lambda:search_text("Data usage"), True, 3):
                click_textview_by_text("Data usage")  
    
    def tethering_hotspot(self):
        click_textview_by_text("More")
        if wait_for_fun(lambda:search_text("Tethering & hotspot"), True, 3):
            click_textview_by_text("Tethering & hotspot")   
    
    def check_APN(self):
        click_textview_by_text("More")
        if wait_for_fun(lambda:search_text("Cellular networks"), True, 3):
            click_textview_by_text("Cellular networks")
            if wait_for_fun(lambda:search_text("Access Point Names"), True, 3):
                click_textview_by_text("Access Point Names") 
                
    def check_location(self):
        click_textview_by_text("Location")
        if wait_for_fun(lambda:search_view_by_desc("More options"), True, 3):
            click_imageview_by_desc("More options")
            if wait_for_fun(lambda:search_text("Scanning"), True, 3):
                click_textview_by_text("Scanning")
                        
    def add_calendar_event(self):
        click_imageview_by_desc("More options")
        if wait_for_fun(lambda:search_text("New event"), True, 3):
            click_textview_by_text("New event")
            if wait_for_fun(lambda:search_text("Add account"), True, 5):
                click_button_by_text("Add account")
                if wait_for_fun(lambda:search_view_by_id("account_email"), True, 5):
                    Email().add_eamil_account()
                    sleep(5)
                    start_activity('com.android.calendar','com.android.calendar.AllInOneActivity')
                    if wait_for_fun(lambda:search_view_by_desc("More options"), True, 5):
                        click_imageview_by_desc("More options")
                        if wait_for_fun(lambda:search_text("New event"), True, 3):
                            click_textview_by_text("New event")
                            if wait_for_fun(lambda:search_view_by_id("title"), True, 3):
                                entertext_edittext_by_id('title','event')
                                sleep(5)
                                click_textview_by_index(1)
                                #click_textview_by_text("DONE") 
    
    def enable_usb_debugging(self):
        click_textview_by_text("About phone")
        sleep(2)
        for i in range(6):
            click_textview_by_text("Build number")
        send_key(KEY_BACK)
        if wait_for_fun(lambda:search_text("Developer options"), True, 3):
            click_textview_by_text("Developer options")
            sleep(2)
            click_textview_by_text("USB debugging") 
            
    def check_cellular_networks(self):
        click_textview_by_text("More")
        if wait_for_fun(lambda:search_text("Cellular networks"), True, 3):
            click_textview_by_text("Cellular networks") 
            
    def check_cellular_data_limit(self):
        click_textview_by_text("Data usage")
        if wait_for_fun(lambda:search_text("Cellular data usage"), True, 3):
            click_textview_by_text("Cellular data usage")
            if wait_for_fun(lambda:search_view_by_id("filter_settings"), True, 3):
                click_imageview_by_id("filter_settings")
                if wait_for_fun(lambda:search_text("Set data limit"), True, 3):
                    click_textview_by_text("Set data limit")
                    if wait_for_fun(lambda:search_text("OK"), True, 3):
                        click_button_by_text("OK")
                        
    def set_APN_protocol(self):
        click_textview_by_text("More")
        if wait_for_fun(lambda:search_text("Cellular networks"), True, 3):
            click_textview_by_text("Cellular networks")
            if wait_for_fun(lambda:search_text("Access Point Names"), True, 3):
                click_textview_by_text("Access Point Names")
                if wait_for_fun(lambda:search_text("CMNET"), True, 3):
                    click_textview_by_text("CMNET")
                    if wait_for_fun(lambda:search_text("APN protocol"), True, 3):
                        click_textview_by_text("APN protocol")
                        if wait_for_fun(lambda:search_text("IPv4"), True, 3):
                            click_textview_by_text("IPv4") 
    
    def enable_disable_screen_pinning(self):
        click_textview_by_text("Security")
        if wait_for_fun(lambda:search_text("Screen pinning"), True, 5):
            click_textview_by_text("Screen pinning")
            if wait_for_fun(lambda:search_text("Off"), True, 5):
                click_imageview_by_id("switch_widget")
                if wait_for_fun(lambda:search_text("On"), True, 5):
                    #click_imageview_by_id("switch_widget")
                    click_button_by_text("On")                                                                                                                                                                                                                                         