'''
   Base class of all suit.

   This module defines the life cycle of test suit .
   and makes the suit subclass just need to care about little things

   1.test_suit_run() function is the suit entry.
   In this function , it will call test_suit_init() to init some information about this suit.
   then, test_suit_main() function will be called, and subclasses just need to override it,and do itself things.
   last, test_suit_end() function will be called, and save some log.

   2.If you want to add some common function for all the test suits ,
   you can add them here.

   @author: U{c_lqiang<c_lqiang@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{test_case_base<test_case_base>}
   @note:
   @attention:
   @bug:
   @warning:



'''
from utility_wrapper import *
import fs_wrapper
from logging_wrapper import set_cur_suit_name,log_test_framework,qsst_log_suit_init,\
    qsst_log_suit_end, print_report_line
from case_utility import START_RUN,END,insert_waypoint
from test_case_base import TestCaseBase

class TestSuitBase(object):
    """The base class for test suit"""
    def __init__(self, name, suit_info, runner='robotium', enabled=True):
        self.name = name
        self.suit_info = suit_info
        self.runner = runner
        self.enabled = enabled
        self.test_cases = []
        self.relative_suits = []
        
    def addCase(self, case):
        '''
        add case to this suit

        @type case: L{TestCaseBase<TestCaseBase>}
        @param case: which case need to added
        '''
        self.test_cases.append(case)

    def test_suit_run(self, suit_results):
        '''
        the entry of the suit.through this method to control the suit life cycle.

        @type suit_results: array
        @param suit_results: the case result array.
        '''
        if self.test_suit_init(suit_results):
            self.test_suit_main(suit_results)
            self.test_suit_end(suit_results)
            return True
        else:
            log_test_framework(self.name, "suit init fail")
            self.test_suit_end(suit_results)
            return False
    
    def test_suit_init(self, suit_results):
        '''
        init the test suit . such as: save the current suit name; init the report logging; launcher this application;
        set the L{current_case_continue_flag<current_case_continue_flag>} to True;
        '''
        set_cur_suit_name(self.name)
        log_test_framework(self.name, "suit init...")
        qsst_log_suit_init()
        set_can_continue()
        suit_config_map=fs_wrapper.get_test_suit_config(self.name)
        global suit_description
        suit_description = suit_config_map.get(fs_wrapper.SUIT_DESCRIPTION)
        if suit_description == None:
            suit_description = ''

        import settings.common as SC
        #if auto insert case waypoint.
        if SC.PRIVATE_TRACKING_AUTO_INSERT_CASE_WAYPOINT:
            if int(SC.PUBLIC_RUNNING_REPEAT_NUMBER) == 1:
                insert_waypoint(START_RUN + self.name, suit_description)
            else:
                insert_waypoint(START_RUN + '(' + str(TestCaseBase.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ') ' + self.name, suit_description)
        return True

    def test_suit_end(self, suit_results):
        '''
        end the test suit . save some loggoing
        '''
        import settings.common as SC
        #if auto insert case waypoint.
        if SC.PRIVATE_TRACKING_AUTO_INSERT_CASE_WAYPOINT:
            if int(SC.PUBLIC_RUNNING_REPEAT_NUMBER) == 1:
                insert_waypoint(END + self.name, suit_description)
            else:
                insert_waypoint(END + '(' + str(TestCaseBase.cycle_index) +'/' + str(SC.PUBLIC_RUNNING_REPEAT_NUMBER) + ') ' + self.name, suit_description)

        log_test_framework(self.name, "suit end")
        qsst_log_suit_end()
            
    def  test_suit_main(self, suit_results):
        '''
        the subclass need to override this function to do itself things

        @type suit_results: array
        @param suit_results: the case result array.
        '''
        case_results = []
        #run case one by one
        for case in self.test_cases:
            case.test_case_run(case_results)

        #report case results
        if not fs_wrapper.run_init_settings:
            count = len(case_results)
            success = 0
            for result in case_results:
                if result[1]:
                    success += 1
            print_report_line("Total:" +str(success) + '/' + str(count),)
    
    def __str__(self):
        ret = '[Suit][Name: %s, SuitInfo: %s, SuitRunner: %s, enabled: %d]\n' % (self.name, str(self.suit_info),
                                                                                self.runner, self.enabled)
        ret += '\tCase Number: %d\n' % len(self.test_cases)
        for case in self.test_cases:
            ret += '\t%s\n' % str(case)
        ret += '[Suit End]'
        return ret
            
    @staticmethod 
    def createInstance(class_name, *args, **kwargs): 
        '''
        give the class name and the args to create a test suit instance

        @type class_name: string
        @param class_name: class name of this suit
        @type args: reference
        @param args: arguments the suit needs
        '''
        (module_name, class_name) = class_name.rsplit('.', 1) 
        module_meta = __import__(module_name, globals(), locals(), [class_name]) 
        class_meta = getattr(module_meta, class_name) 
        o = class_meta(*args, **kwargs)
        return o

class SuitInfo(object):
    """The class for suit info"""
    def __init__(self, name, pkg_name, socket_name, wait_time, target_pkg=None, target_activity=None):
        self.name = name
        self.pkg_name = pkg_name
        self.socket_name = socket_name
        self.wait_time = int(wait_time)
        self.target_pkg = target_pkg
        self.target_activity = target_activity
        
    def __str__(self):
        return ('[SuitInfo][Name: %s, pkg_name: %s, socket_name: %s, wait_time: %d, target_pkg: %s, target_activity: %s]'
                    % (self.name, self.pkg_name, self.socket_name, self.wait_time, self.target_pkg, self.target_activity))
