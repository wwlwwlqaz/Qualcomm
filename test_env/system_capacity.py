'''
    Query property or Set property.

    This is the class to provide some common functions:
    get_property/set_property

   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see:
   @note:
   @attention:
   @bug:
   @warning:

'''
import os
from logging_wrapper import log_test_framework
from platform_check import get_platform_info

global osInfo
osInfo = get_platform_info()
LOG_TAG = 'system_capacity'

class SystemCapacity:
    '''
    This class provide the common functions: get_property/set_property
    '''

    def __init__(self):
        log_test_framework(LOG_TAG, "init: ")

    def set_property(self, prop_key, prop_value):
        '''
        set the property value.

        @type prop_key:string
        @param prop_key:property key.
        @type prop_value:string
        @param prop_value:property value.
        '''
        try:
            os.system('setprop ' + prop_key + ' ' + prop_value)
        except IOError, msg:
            log_test_framework(LOG_TAG, "IO error: " + msg.strerror)

def get_property(prop_key):
        '''
        get property by the key.

        @type prop_key:string
        @param prop_key: property key.
        @return: the query property value.
        '''
        if(osInfo == 'Linux-Phone'):
            result = str(os.popen('getprop ' + prop_key).read())
        elif(osInfo == 'Linux-PC' or osInfo == 'Windows'):
            result = str(os.popen('adb shell ' +'getprop ' + prop_key).read())
        return result