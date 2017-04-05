#coding=utf-8
'''
   Write an new email and send


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{TestCaseBase <TestCaseBase>}
   @note:
   @attention:
   @bug:
   @warning:



'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    Write an new email and send
#precondition:
#    login email
#steps:
#    receive emails
#    write an new email and send
############################################

class test_suit_email_case5(TestCaseBase):
    '''
    test_suit_email_case5 is a class for gmail case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    def test_case_main(self, case_results):
        return InvokeFuncByCurRunTarget(self,"test_suit_email","test_suit_email_case5_adaptive","email5")