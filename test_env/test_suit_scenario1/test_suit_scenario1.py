'''
   A class extends TestSuitBase for scenario1.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
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

CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}

class test_suit_scenario1(TestSuitBase):
    '''
    test_suit_scenario1 is a class for scenario1 suit.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    def test_suit_init_robotium(self):
        '''
        init robotium.kill settings process.
        '''
        kill_by_name("com.android.settings")
        return True