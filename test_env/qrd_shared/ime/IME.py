#coding=utf-8
'''
   shared library of ime module.

   This class will provide input method to all of mudules that need input content by ime.
   For the ime keyboard is just an whole image that uiautomator cann't capture the key in it, so we only can click the coordinate of keys
   to complete the input.

   1.Developer can directly call those api to complete inputing content by ime.Such as:

     from qrd_shared.case import *
     ime.IME_input_english(1, 'abc')
     ime.IME_input_number(1, '12345', 'n')
     ime.IME_input(1, 'ceshi','c')

   2.Developer can modify api or add some new api here. Before it, please make sure have been
     familiar with the structure.Modify existed api,please notice it won't affect others caller.

     If you want to add an new input method or have a new resolution DUT, and the coordinate of keys are changed.
     You should add an new key map in qrd_shared\ime\methods.When you add, please reference to existing google pinyin key map.


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
import qrd_shared.ime.methods.predefine_input_seq as INPUT_SEQ
from qrd_shared.case import *
from platform_check import get_platform_info
from utility_wrapper import *

osInfo = get_platform_info()
if osInfo == 'Linux-Phone':
    wait_time = 0
elif osInfo == 'Linux-PC' or osInfo == 'Windows':
    wait_time = 0

class IME(Base):
    def __init__(self):
        '''
        init function.

        @see: L{Base <Base>}
        '''
        self.mode_name = "ime"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))

    def set_default_input_method(self, input_method_name):
        '''
        set default input method

        @type input_method_name: string
        @param input_method_name: ime method name. Make sure firstly define variables in multi-language and use it.

        '''
        sleep(1)
        start_activity('com.android.settings','.Settings')
        scroll_up()
        click_textview_by_text(self.get_value("language_and_ime"))
        #scroll_up()
        #whether select the input method
        disable_watcher_anr_fc()
        
        InvokeFuncByCurRunTarget(self,"qrd_shared.ime","qrd_shared_ime","click_default")
        enable_watcher_anr_fc()
        if search_text(input_method_name,1,0) == False:
            method_selected = False
            goback()
            click_textview_by_text(input_method_name)
            click_textview_by_text(self.get_value("default"))
            click_textview_by_text(input_method_name)
        else:
            click_textview_by_text(input_method_name)
        goback()

    def close_auto_capitalization_google_pinyin(self):
        '''
        close auto capitalization function in goolge pinyin method

        '''
        start_activity('com.android.browser','.BrowserActivity')
        sleep(1)
        click_textview_by_id("url")

        key_map = self.get_key_map(1)
        swtich_key = key_map.get("ch_en")
        long_click(swtich_key[0],swtich_key[1])

        InvokeFuncByCurRunTarget(self,"qrd_shared.ime","qrd_shared_ime","googleime")


    def set_google_pinyin_default_input_en(self):
        '''
        set first ui as English character ui when default input method is google pinyin method.

        '''
        start_activity('com.android.browser','.BrowserActivity')

        click_menuitem_by_text(self.get_value("Find_on_page"))
        self.IME_input(1,"a.","e","p")
        sleep(2)

        key_map = self.get_key_map(1)
        if not search_text("a.",1,0):
            swtich_key = key_map.get("ch_en")
            click(swtich_key[0],swtich_key[1])

        for i in range(0,4):
            send_key(KEY_DEL)

        goback()
        goback()
        goback()
        InvokeFuncByCurRunTarget(self,"qrd_shared.ime","qrd_shared_ime","out")


    #input content
    #ime_type 1 == google_pinyin
    #language c == Chinese  e == English
    #input_type f == full input p == part input input b = part input then press back key
    def IME_input(self, ime_type, content_seq, lanauage='e', input_type="f"):
        '''
        Input content, include English, Chinese, number or special character and so on.

        @type ime_type: string
        @param ime_type: input method type, 1: google pinyin.
        @type content_seq: string
        @param content_seq: sequence of input content.
                            It can use variables both in common.py and in predefine_input_seq.py (test_env\qrd_shared\ime\methods\predefine_input_seq.py).
                            This is a sequence of input characters by order. The input character mapping table is key_map_***_***.py(test_env\qrd_shared\ime\methods\google_pinyin\key_map_***_***.py).
                            Each key in keyboard has the corresponding value in the mapping table.
        @type lanauage: string
        @param lanauage:  it can be English or Chinese. When content contains Chinese, the value is “c”, otherwise is “e”. “e” is the default value.
        @type input_type: string
        @param input_type:  f is full input and p is part, b is part input then press back key. f is the default value.
        '''
        key_map = {}

        #get selected ime's key map
        key_map = self.get_key_map(ime_type)

        #if language is Chinese, switch to Chinese
        if lanauage == 'c':
            sleep(wait_time)
            swtich_key = key_map.get("ch_en")
            click(swtich_key[0],swtich_key[1])
            #provide 1 second change the input method layout
            sleep(0.2)

        #tap the character
        self.tap_content(key_map,content_seq)

        #if language is Chinese, after input, switch to English back
        if lanauage == 'c':
            #switch to English
            sleep(wait_time)
            click(swtich_key[0],swtich_key[1])
            #provide 1 second change the input method layout
            sleep(0.2)

        #input type
        if input_type == "f":
            sleep(wait_time)
            next_key = key_map.get("next")
            click(next_key[0],next_key[1])
        elif input_type == "b":
            sleep(wait_time)
            goback()

    #input only number
    #parameter:
    #    ime_type 1 == google_pinyin
    #    content_number
    #    keyboard_type c == character keyboard  n == number keyboard c-n == character-number keyboard
    #input_type f == full input p == part input input b = part input then press back key
    def IME_input_number(self, ime_type, content_number, keyboard_type, input_type="f"):
        '''
        Input only number

        @type ime_type: string
        @param ime_type: input method type, 1: google pinyin.
        @type content_number: string
        @param content_number: input content. just only number. such as “11234”.
        @type keyboard_type: string
        @param keyboard_type:   there are three types of keyboard when input.
                                c is the character keyboard with character UI.
                                c-n is the character keyboard with number UI.
                                n is the number keyboard.
        @type input_type: string
        @param input_type:  f is full input and p is part, b is part input then press back key. f is the default value.
        '''
        key_map = {}

        #get selected ime's key map
        key_map = self.get_key_map(ime_type)

        #character keyboard key map
        c_1 = key_map.get("1")
        c_2 = key_map.get("2")
        c_3 = key_map.get("3")
        c_4 = key_map.get("4")
        c_5 = key_map.get("5")
        c_6 = key_map.get("6")
        c_7 = key_map.get("7")
        c_8 = key_map.get("8")
        c_9 = key_map.get("9")
        c_0 = key_map.get("0")
        c_bspace = key_map.get(" ")
        c_full_stop = key_map.get(".")
        c_dash = key_map.get("sign_7")
        c_next = key_map.get("next")

        #number keyboard key map
        n_1 = key_map.get("num_1")
        n_2 = key_map.get("num_2")
        n_3 = key_map.get("num_3")
        n_4 = key_map.get("num_4")
        n_5 = key_map.get("num_5")
        n_6 = key_map.get("num_6")
        n_7 = key_map.get("num_7")
        n_8 = key_map.get("num_8")
        n_9 = key_map.get("num_9")
        n_0 = key_map.get("num_0")
        n_bspace = key_map.get("num_bracket")
        n_dash = key_map.get("num_dash")
        n_full_stop = key_map.get("num_full_stop")
        n_next = key_map.get("num_next")

        #character keyboard
        if keyboard_type.find('c') != -1 :

            #switch to character-number keyboard
            if keyboard_type == 'c':
                sleep(wait_time)
                click(key_map.get("num_sign")[0],key_map.get("num_sign")[1])

            #tap the character
            for i in range(0,len(str(content_number))):
                sleep(wait_time)

                key = {
                '1': lambda: c_1,
                '2': lambda: c_2,
                '3': lambda: c_3,
                '4': lambda: c_4,
                '5': lambda: c_5,
                '6': lambda: c_6,
                '7': lambda: c_7,
                '8': lambda: c_8,
                '9': lambda: c_9,
                '0': lambda: c_0,
                ' ': lambda: c_bspace,
                '.': lambda: c_full_stop,
                '-': lambda: c_dash,
                }[content_number[i]]()

                click(key[0],key[1])

            #switch back to character-english keyboard
            if keyboard_type == 'c':
                sleep(wait_time)
                click(key_map.get("num_sign")[0],key_map.get("num_sign")[1])

            #input type
            if input_type == "f":
                sleep(wait_time)
                click(c_next[0],c_next[1])

        elif keyboard_type == "n":

            #tap the character
            for i in range(0,len(str(content_number))):
                sleep(wait_time)

                key = {
                '1': lambda: n_1,
                '2': lambda: n_2,
                '3': lambda: n_3,
                '4': lambda: n_4,
                '5': lambda: n_5,
                '6': lambda: n_6,
                '7': lambda: n_7,
                '8': lambda: n_8,
                '9': lambda: n_9,
                '0': lambda: n_0,
                ' ': lambda: n_bspace,
                '.': lambda: n_full_stop,
                '-': lambda: n_dash,
                }[content_number[i]]()

                click(key[0],key[1])

            #input type
            if input_type == "f":
                sleep(wait_time)
                click(n_next[0],n_next[1])
            elif input_type == "b":
                sleep(wait_time)
                goback()


    #input only english -- support lower and upper case
    #ime_type 1 == google_pinyin_800*480
    #content_english
    #input_type f == full input p == part input input b = part input then press back key
    def IME_input_english(self, ime_type, content_english, input_type="f"):
        '''
        Input only English, both lower case and upper case.

        @type ime_type: string
        @param ime_type: input method type, 1: google pinyin.
        @type content_english: string
        @param content_english:  input content. just only English, support lower and upper case, such as “aaBB”, ”aa”, ”BB”.
        @type input_type: string
        @param input_type:  f is full input and p is part, b is part input then press back key. f is the default value.
        '''
        key_map = {}

        #get selected ime's key map
        key_map = self.get_key_map(ime_type)

        #switch lower-upper key
        switch_low_upper_key = key_map['caps'];

        #content_english type.
        #1. all lower case.
        #2. all upper case.
        #3. First character upper case,others lower case
        #4. some lower case, some upper case
        if content_english.islower() == True:

            #tap the content
            self.tap_content(key_map,content_english)

        elif content_english.isupper() == True:

            #switch to upper case
            sleep(wait_time)
            click(switch_low_upper_key[0],switch_low_upper_key[1])

            #tap the content
            content_english = content_english.lower()
            self.tap_content(key_map,content_english)

            #back to lower
            sleep(wait_time)
            click(switch_low_upper_key[0],switch_low_upper_key[1])

        elif content_english.istitle() == True:

            for i in range(0,len(content_english)):

                if i==0:
                    #switch to upper case
                    sleep(wait_time)
                    click(switch_low_upper_key[0],switch_low_upper_key[1])
                    key = content_english[i].lower()

                sleep(wait_time)
                if i != 0:
                    key = content_english[i]

                x = key_map.get(key)[0]
                y = key_map.get(key)[1]
                click(x,y)

                if i==0:
                    #back to lower
                    sleep(wait_time)
                    click(switch_low_upper_key[0],switch_low_upper_key[1])
        else:
            before_upper_flag = False
            for i in range(0,len(content_english)):

                #upper case or character
                if content_english[i].islower() != True :

                    #switch to upper case
                    if before_upper_flag == False:
                        sleep(wait_time)
                        click(switch_low_upper_key[0],switch_low_upper_key[1])
                        before_upper_flag = True
                        sleep(0.1)

                    #click key
                    sleep(wait_time)
                    key = content_english[i].lower()
                    x = key_map.get(key)[0]
                    y = key_map.get(key)[1]
                    click(x,y)

                    #whether the next charater is lower or the end
                    if i+1 == len(content_english):
                        #back to lower case
                        sleep(wait_time)
                        click(switch_low_upper_key[0],switch_low_upper_key[1])
                        before_upper_flag = False
                        sleep(0.1)
                    elif content_english[i+1].islower() == True:
                        #back to lower case
                        sleep(wait_time)
                        click(switch_low_upper_key[0],switch_low_upper_key[1])
                        before_upper_flag = False
                        sleep(0.1)

                #lower case
                else:

                    #click key
                    sleep(wait_time)
                    key = content_english[i]
                    x = key_map.get(key)[0]
                    y = key_map.get(key)[1]
                    click(x,y)

        #input type
        if input_type == "f":
            sleep(wait_time)
            click(key_map.get("next")[0],key_map.get("next")[1])
        elif input_type == "b":
            sleep(wait_time)
            goback()

     #tap the character
    def tap_content(self, key_map,content):
        '''
        tap the character
        '''
        for i in range(0,len(content)):
            sleep(wait_time)
            key = content[i]
            x = key_map.get(key)[0]
            y = key_map.get(key)[1]
            click(x,y)

    #get used key map
    #ime_type 1 == google_pinyin
    def get_key_map(self, ime_type):
        '''
        get existed key map
        '''
        key_map = {}
        display_width = getDisplayWidth()
        display_height = getDisplayHeight()
        ime_name = ""
        #get selected ime's key map
        if ime_type == 1:
            ime_name = "google_pinyin"
        folder = "qrd_shared.ime.methods." + ime_name;
        path = folder +".key_map_" + display_width + "_" + display_height
        ime_key_map = __import__(path, fromlist=[folder])
        key_map = ime_key_map.__getattribute__("key_map")
        return key_map
