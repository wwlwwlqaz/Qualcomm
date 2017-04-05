# -*- coding: utf-8 -*-  
'''

@author: huitingn
@version:

'''
from utility_wrapper import *
import fs_wrapper
from test_suit_base import TestSuitBase
from case_utility import *
import re, datetime, shlex
from qrd_shared.case import *


CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}
BOOL_STK_WIFI_CHECK = False
BOOL_STK_MOBILE_NETWORK_CHECK = False

class test_suit_cmcc_devci_contact(TestSuitBase):
    '''
    test_suit_ui_message is a class for browser suit.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    pass

def format_phone_number(num):
    '''
    format phone number,for example:format "12345678901" to "123 4567 8901"

    @type num: string
    @param num: phone number that need format
    @return: a phone number which have formated
    '''
    s = insert(num, ' ', 3)
    return insert(s, ' ', 8)

def format_phone_number_1(num):
    '''
    format phone number,for example:format "12345678901" to "1 234-567-8901"
    @author: min.sheng
    @type num: string
    @param num: phone number that need format
    @return: a phone number which have formated
    '''
    s1 = insert(num, ' ', 1)
    s2 = insert(s1, '-', 5)
    return insert(s2, '-', 9)

def insert(original, new, pos):
    '''
    insert a new string into a tuple.

    @type original: string
    @param original: original string
    @type new: string
    @param new: a string that need insert.
    @type pos: number
    @param pos: position that need insert.
    @return: a new string.
    '''
    return original[:pos] + new + original[pos:]


def check_string_ok():
    '''
        check string of ok 
        @author: min.sheng
    '''
    if search_text('ok', 1, 0,searchFlag=TEXT_CONTAINS):
            click_button_by_text('ok', 1, 0)
            sleep(2)

