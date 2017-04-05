'''
   shared library of phone module.

   This class will provide operations api for phone application.

   1.Developer can directly call those api to perform some operation.Such as:

     from qrd_shared.case import *
     phoneOn = phone.phone_call('10086', "", 0)

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
from qrd_shared.settings.Settings import Settings
import time
from lib2to3.fixer_util import Number

class Phone(Base):

    PREDEFINED_NUMBERS = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

    '''
    Phone is a class for operating Phone application.

    @see: L{Base <Base>}
    '''

    def __init__(self):
        '''
        init function.

        @see: L{Base <Base>}
        '''
        self.mode_name = "phone"
        Base.__init__(self, self.mode_name)
        self.settings = Settings()
        self.debug_print('Base init:%f' % (time.time()))
        
    def go_home(self):
        for i in range(10):
            flag1 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Speed Dial', isScrollable=0, searchFlag=TEXT_MATCHES)
            flag2 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Recents', isScrollable=0, searchFlag=TEXT_MATCHES)
            flag3 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Contacts', isScrollable=0, searchFlag=TEXT_MATCHES)
            
        
            '''try:scroll_to_bottom()
            except:pass'''
            
            if flag1 & flag2 & flag3 is True: return True
            else: goback()
            sleep(1)
        
        return False

    # MO by one slot
    # parameter:
    #    phoneNumber: the whole call phone number
    #    smartNumber: part phone number to match contacts
    #    slot: 0--slot1, 1--slot2 2-- default slot can use for emergency call
    # Return:
    #    True: get through.
    #    False: no
    def phone_call(self, phoneNumber, smartNumber, slot, call_duration):
        '''
        MO by one slot

        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        @type smartNumber: string
        @param smartNumber: part phone number to match contacts.
        @type slot: number
        @param slot: 0--slot1, 1--slot2 2-- default slot can use for emergency call.
        @return: True: get through; False: no.
        '''
        # dial
        if smartNumber != "":
            self.smart_dial(smartNumber, phoneNumber)
        else:
            self.dial(phoneNumber)

        callmark = ""
        if slot == 0:
            callmark = "callmark1"
        elif slot == 1:
            callmark = "callmark2"
        elif slot != 2:
            return False

        sleep(3)
        if slot == 0:
            if search_text("Call with"):
                take_screenshot()
                click_textview_by_index(1)

#            click_textview_by_text("SUB 01")
            # click_in_list_by_index(1)
        # ##search_view_by_id("call_action_sub_icon2") and 
        elif slot == 1:
            if search_text("Call with"):
                take_screenshot()
                click_textview_by_index(2)
#            click_textview_by_text("SUB 02")
#            click_in_list_by_index(2)
        else:
            sleep(1)
            if slot != 2 and search_view_by_id(callmark):
                click_button_by_id(callmark)
            sleep(1)
            click_button_by_id(callmark)
        if search_text(self.get_value("network_not_available")):
            return False
        # whether get through.
        take_screenshot()
        sleep(call_duration)
        func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'elapsedTime')))
        if wait_for_fun(func, True, 10):
            elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
            
        if search_view_by_id("floating_end_call_action_button") and (cmp(elapsedTime, '00:00')) :
            click_button_by_id("floating_end_call_action_button")
            return True
        
        else:
            return False

    # remove guide info when enter phone app for the first time
    def remove_gudie_info(self):
        '''
        remove guide info when enter phone app for the first time

        '''
        if search_view_by_id("clingText") == True:
            click_button_by_text(self.get_value("ok"), 1, 0)

    # data call switch to always ask
    # parameter:
    #    card_id,1-slot1,2-slot2,0-always ask
    def set_data_call(self, card_id):
        '''
        data call switch to always ask

        @type card_id: number
        @param card_id: 1-slot1,2-slot2,0-always ask.
        '''
        sleep(1)
        # remove guide info when enter first time
        self.remove_gudie_info()

        start_activity('com.android.settings', '.Settings')
        self.settings.set_default_voice(card_id)
        goback()
        
    def call_back_from_history(self):
        '''
        call back from history
        '''
        click_imageview_by_desc('More options')
        click_textview_by_text('Call History')
        click_textview_by_text('All')
        click_textview_by_id('filter_sub_spinner')
        sleep(1)
        click_textview_by_text('ALL SIMS')
        if search_text('10086') :
            click_textview_by_text('10086')
            click_textview_by_text('Call Back')
        elif search_text('12117'):
            click_textview_by_text('12117')
            click_textview_by_text('Call Back')
        else:
            #click_textview_by_index(0)
            click_textview_by_id('name')
            click_textview_by_text('Call Back')
        sleep(float(SC.PRIVATE_PHONE_CALL_TIME))
        func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'elapsedTime')))
        if wait_for_fun(func, True, 10):
            elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
        if search_view_by_id("floating_end_call_action_button") and (cmp(elapsedTime, '00:00')) :
            click_button_by_id("floating_end_call_action_button")
            return True
        else:
            return False

    # used for API
    def smart_dial(self, smartNumber, phoneNumber):
        '''
        inner used.
        According to input phone number to match contacts,then dial.

        @type smartNumber: string
        @param smartNumber: part phone number to match contacts.
        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        '''
        click_imageview_by_id("deleteButton", 1, 0, 0, LONG_CLICK)
        for i in range(0, len(smartNumber)):
            click_imageview_by_id(str(self.PREDEFINED_NUMBERS[smartNumber[i]]))
        click_view_by_container_id('filterbutton', 'android.widget.TextView', 0)
        sleep(1)
        click_textview_by_text(phoneNumber)
        click_imageview_by_id("dialButton")

    # used for API
    def dial(self, phoneNumber):
        '''
        inner used.
        Firstly, delete existed phone number.
        Then input number and dial

        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        '''
        if search_view_by_id("deleteButton"):
            click_imageview_by_id("deleteButton", 1, 0, 0, LONG_CLICK)
        sleep(10)
        call_number_str = [s for s in phoneNumber ]
        for phoneNumber in call_number_str:
            if phoneNumber == "1":
                click_imageview_by_id("dialpad_key_voicemail")
            else:
                click_imageview_by_id(str(self.PREDEFINED_NUMBERS[phoneNumber]))
        sleep(1)
        if search_view_by_id("dialButton"):
            click_imageview_by_id("dialButton")
        else:
            click_button_by_id("floating_action_button")

    def input_dial_number(self, phoneNumber):#c_caijie
        '''
        inner used.
        Firstly, delete existed phone number.
        Then input number 

        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        '''
        if search_view_by_id("deleteButton"):
            click_imageview_by_id("deleteButton", 1, 0, 0, LONG_CLICK)
        sleep(10)
        call_number_str = [s for s in phoneNumber ]
        for phoneNumber in call_number_str:
            if phoneNumber == "1":
                click_imageview_by_id("dialpad_key_voicemail")
            else:
                click_imageview_by_id(str(self.PREDEFINED_NUMBERS[phoneNumber]))
        sleep(1)

            
     # used for API
    def speed_dial(self, speed_dail_number,Number):
        '''
        inner used.
        According to input phone number to match contacts,then dial.

        @type smartNumber: string
        @param smartNumber: part phone number to match contacts.
        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        '''
        click_imageview_by_id('dialtacts_options_menu_button')
        click_textview_by_text('Settings')
        click_textview_by_text('Call settings')
        click_textview_by_text('Speed dial settings',isScrollable=1)
        sleep(1)
        take_screenshot()
        click_textview_by_text(Number)
        if search_text("Input Number"):
            log_test_framework("weixiang--> :", "number 2 have not been added speed dail")
            entertext_edittext_on_focused(speed_dail_number)
            click_button_by_id('btn_complete')
            if search_text(speed_dail_number):
                log_test_framework("weixiang--> :", "number 2 added speed dail successfully" )
                return True
            else:
                log_test_framework("weixiang--> :", "number 2  added speed dail failed")
                take_screenshot()
                return False
        elif (not search_text("Key unassigned")) and (search_text("Delete")):
            log_test_framework("weixiang--> :", "number 2 added speed dail before, need delete it firstly")
            click_textview_by_text('Delete')
            click_textview_by_text(Number)
            if search_text("Input Number"):
                log_test_framework("weixiang--> :", "number 2 have not been added speed dail")
                entertext_edittext_on_focused(speed_dail_number)
                click_button_by_id('btn_complete')
                if search_text(speed_dail_number):
                    log_test_framework("weixiang--> :", "number 2 added speed dail successfully" )
                    return True
                else:
                    log_test_framework("weixiang--> :", "number 2  added speed dail failed")
                    take_screenshot()
                    return False
                
    # used for API
    def clear_call_log(self):
        '''
        inner used.
        Firstly, delete existed phone number.
        Then input number and dial

        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        '''
        
        sleep(1)
        click_imageview_by_id('dialtacts_options_menu_button')
        sleep(1)
        click_textview_by_text('Call History')
        sleep(1)
        click_textview_by_text('All')
        sleep(1)
        click_textview_by_id('filter_sub_spinner')
        sleep(1)
        click_textview_by_text('ALL SIMS')
        if search_text("Your call log is empty"):
            log_test_framework("weixiang--> :", "No call Log" )
            return True
        else:
            send_key(KEY_MENU)
            click_textview_by_text('Clear call log')
            sleep(1)
            click_imageview_by_desc('More options')
            delstr = 'All'
            if search_text(delstr):
                click_textview_by_text(delstr)
                if is_view_enabled_by_id(VIEW_TEXT_VIEW, 'done', isScrollable=0):
                    click_textview_by_desc('done')
                else:
                    log_test_framework("weixiang--> :", "No call Log" )
                    return True
                sleep(2)
                # if wait_for_fun(lambda:search_text('will be deleted'), True, 10):
                if search_text('Sure to delete the call logs ', searchFlag=TEXT_CONTAINS):
                    # click_textview_by_text('OK')
                    click_button_by_text('OK')
                    return True
                else:
                    return False
        
    def permission_allow(self):#c_caijie
        if search_text("NEXT", isScrollable=0, searchFlag=TEXT_CONTAINS):
            click_textview_by_text("NEXT",isScrollable=0)
            sleep(4)
        for i in range(8):
            if search_view_by_id('permission_allow_button'):
                click_button_by_id('permission_allow_button',isScrollable=0)
                sleep(5)


    def del_all_calllog(self):#c_caijie
        click_button_by_id('dialtacts_options_menu_button')
        sleep(3)
        click_textview_by_text('Call History')
        sleep(3)
        click_imageview_by_desc("More options")
        sleep(3)
        click_textview_by_text('Clear call history')
        sleep(3)
        click_checkbox_by_id('select_all_check')
        sleep(3)
        click_textview_by_id('btn_ok')
        sleep(3)
        click_button_by_text('OK')
        sleep(10) 
                           