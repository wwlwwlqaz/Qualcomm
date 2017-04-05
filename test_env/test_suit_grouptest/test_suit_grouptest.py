'''
   A class extends TestSuitBase for baidumap.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
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

CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}

class test_suit_grouptest(TestSuitBase):
    pass




def deleteOldSerialNumber():
    tag = 'deleteOldSerialNumber()'
    currLocation = os.getcwd()
    a = currLocation.split(os.sep)#[0:-1]
    b = os.sep.join(a+['settings',GROUP_SERIAL_NUMBER_FILE_NAME])
    try:os.remove(b)
    except Exception,ex:log_test_framework(tag, 'exception: '+str(ex))


