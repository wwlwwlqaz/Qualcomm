'''
   Base class of all background suit.

   This module defines the life cycle of background test suit .
   and makes the suit subclass just need to care about little things

   1.test_suit_run() function is the suit entry.
   In this function , it will call test_suit_init() to init some information about this suit.
   then, test_suit_main() function will be called, and subclasses just need to override it,and do itself things.

   2.If you want to add some common function for all the background test suits ,
   you can add them here.

   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{bg_test_case_base<bg_test_case_base>}
   @note:
   @attention:
   @bug:
   @warning:

'''

from logging_wrapper import log_test_framework

class BgTestSuitBase(object):
    """The base class for test suit"""
    def __init__(self, name, suit_info, enabled=True):
        self.name = name
        self.suit_info = suit_info
        self.enabled = enabled
        self.bg_test_cases = []

    def __str__(self):
        ret = '[Suit][Name: %s, SuitInfo: %s, enabled: %d]\n' % (self.name, str(self.suit_info),self.enabled)
        ret += '\tCase Number: %d\n' % len(self.bg_test_cases)
        for case in self.bg_test_cases:
            ret += '\t%s\n' % str(case)
        ret += '[Suit End]'
        return ret

    def test_suit_run(self):
        '''
        the entry of the background suit.This method to control the suit life cycle.
        '''
        self.test_suit_init()
        self.test_suit_main()

    def test_suit_main(self):
        '''
        the subclass need to override this function to do itself things
        '''
        #run case one by one
        for case in self.bg_test_cases:
            #SubThread will be killed when main Thread close.
            case.setDaemon(True)
            case.start()

    def test_suit_init(self):
        '''
        end the test suit . save some loggoing.
        '''
        log_test_framework(self.name, "suit init....")

    def addCase(self, case):
        '''
        add case to this suit
        @type case: L{BgTestCaseBase<BgTestCaseBase>}
        @param case: which case need to added
        '''
        self.bg_test_cases.append(case)