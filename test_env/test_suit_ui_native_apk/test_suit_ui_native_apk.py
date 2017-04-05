# coding: utf-8
'''
   A class extends TestSuitBase for checking native apk


   @author: huitingn@qti.qualcomm.com
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{TestSuitBase <TestSuitBase>}
   @note:
   @attention:
   @bug:
   @warning:


'''
from utility_wrapper import *
import fs_wrapper
from test_suit_base import TestSuitBase
from case_utility import *
import datetime,shlex


CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}

CLOCK_PLATE = {'HOUR':{},'MINUTE':{},'A_P':{}
                  }

CLOCK_PLATE['HOUR']['12'] = (238,318)
CLOCK_PLATE['HOUR']['1'] = (307,337)
CLOCK_PLATE['HOUR']['2'] = (354,386)
CLOCK_PLATE['HOUR']['3'] = (372,453)
CLOCK_PLATE['HOUR']['4'] = (355,520)
CLOCK_PLATE['HOUR']['5'] = (307,571)
CLOCK_PLATE['HOUR']['6'] = (238,590)
CLOCK_PLATE['HOUR']['7'] = (172,571)
CLOCK_PLATE['HOUR']['8'] = (122,520)
CLOCK_PLATE['HOUR']['9'] = (105,453)
CLOCK_PLATE['HOUR']['10'] = (124,384)
CLOCK_PLATE['HOUR']['11'] = (170,337)

CLOCK_PLATE['MINUTE']['00'] = (238,318)
CLOCK_PLATE['MINUTE']['05'] = (307,337)
CLOCK_PLATE['MINUTE']['10'] = (354,386)
CLOCK_PLATE['MINUTE']['15'] = (372,453)
CLOCK_PLATE['MINUTE']['20'] = (355,520)
CLOCK_PLATE['MINUTE']['25'] = (307,571)
CLOCK_PLATE['MINUTE']['30'] = (238,590)
CLOCK_PLATE['MINUTE']['35'] = (172,571)
CLOCK_PLATE['MINUTE']['40'] = (122,520)
CLOCK_PLATE['MINUTE']['45'] = (105,453)
CLOCK_PLATE['MINUTE']['50'] = (124,384)
CLOCK_PLATE['MINUTE']['55'] = (170,337)

CLOCK_PLATE['A_P']['AM'] = (106,618)
CLOCK_PLATE['A_P']['PM'] = (376,618)
CLOCK_PLATE['A_P']['am'] = (106,618)
CLOCK_PLATE['A_P']['pm'] = (376,618)

CLOCK_PLATE['DONE'] = (378,721)


COUNTDOWN = {'1':0,'2':1,'3':2,'4':3,'5':4,\
             '6':5,'7':6,'8':7,'9':8}

TIMER_BUTTON = {}
TIMER_BUTTON['1'] = ('first','android.widget.Button',0)
TIMER_BUTTON['2'] = ('first','android.widget.Button',1)
TIMER_BUTTON['3'] = ('first','android.widget.Button',2)
TIMER_BUTTON['4'] = ('second','android.widget.Button',0)
TIMER_BUTTON['5'] = ('second','android.widget.Button',1)
TIMER_BUTTON['6'] = ('second','android.widget.Button',2)
TIMER_BUTTON['7'] = ('third','android.widget.Button',0)
TIMER_BUTTON['8'] = ('third','android.widget.Button',1)
TIMER_BUTTON['9'] = ('third','android.widget.Button',2)
TIMER_BUTTON['0'] = ('forth','android.widget.Button',1)

class test_suit_ui_native_apk(TestSuitBase):
    '''
    test_suit_ui_nhtApp is a class for checking native apk.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    
    pass


def exit_cur_case(case_tag):
    '''
    goback to homescreen. exit current case.
    
    @type case_tag: string
    @param case_tag:the calling case'TAG
    
    '''
    global current_case_continue_flag
    current_case_continue_flag = True
    
    func = lambda:(search_view_by_desc('Apps') or goback())
    if not wait_for_fun(func,True,5):
        send_key(KEY_HOME)
        #log_test_framework(case_tag, "exit is wrong, may influence the next case")


def cur_time_in_mobilephone():
    TAG='cur_time_in_mobilephone()'
    log_test_framework(TAG,"start")
    
    start_activity('com.android.settings','.Settings')
    click_textview_by_text('Date & time')
    
    # don't use 24-hour format

    if get_view_text_by_index(VIEW_COMPOUNDBUTTON, 2)=='ON': 
        click_button_by_index(2)
    # automatic date & time
    if get_view_text_by_index(VIEW_COMPOUNDBUTTON, 0)=='OFF': 
        click_button_by_index(0)
        
            
    curTime = get_view_text_by_index(VIEW_TEXT_VIEW,11)
    log_test_framework(TAG, "curTime is : " + curTime)
    
    
    curTime = curTime.decode("utf-8")
    convTime = datetime.datetime.strptime(curTime,'%I:%M %p')
    (hour,minute,a_p) = shlex.split(convTime.strftime('%I %M %p'))
    log_test_framework(TAG, " hour: " + hour + " minute: " + minute + " a_p: " + a_p)
    
    
    log_test_framework(TAG,"end")
    return (hour,minute,a_p,curTime)




def pre_check():
    pass

