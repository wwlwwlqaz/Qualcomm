'''
   background test loader for qsst python framework

   This module used to provide utilities for loading the suits or cases from the qsst framework,
   such as: load background test suit and so on

   If you want to add some common function to load background suit or case,
   you can also added them here.

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

import fs_wrapper
from background_case_pool.bg_test_suit_base import BgTestSuitBase
from background_case_pool.bg_test_case_base import BgTestCaseBase
from logging_wrapper import log_test_framework

TAG = 'BgTestLoader'
BACKGROUND_CASE_POOL = 'background_case_pool'

class BgTestLoader(object):
    ''' load background case or suit'''
    def __init__(self):
        pass

    def addTestCase(self, bg_test_suit, caseConfigMap, className, suitName, caseName):
        '''
        add the case to the suit

        @type bg_test_suit: L{BgTestSuitBase<BgTestSuitBase>}
        @param bg_test_suit: suit you want to operation
        @type caseConfigMap: array
        @param caseConfigMap: the configuration map of the case which is adding to the suit
        '''
        test_case = BgTestCaseBase.createInstance(className, caseName, suitName)
        test_case.case_config_map = caseConfigMap
        log_test_framework(test_case.name, "background case added")
        bg_test_suit.addCase(test_case)

    def getCaseList(self, base_path):
        '''
        load the test cases from the path

        @type base_path: string
        @param base_path: the path of the case
        @return: return all the cases which can found under this path
        '''
        all_case_name_list = []
        suit_name_list = fs_wrapper.get_suit_name_list(base_path)
        for suit_name in suit_name_list:
            suit_config_map = fs_wrapper.get_test_suit_config(suit_name, True)
            if suit_config_map.get(fs_wrapper.SUIT_ENABLE_ATTR) == '1':
                cases = fs_wrapper.get_all_cases_py_module_name(suit_name, True)
                for case in cases:
                    case_config_map = fs_wrapper.get_test_case_config(case[1], suit_name, True)
                    if case_config_map.get(fs_wrapper.CASE_ENABLE_ATTR) == '1':
                        all_case_name_list.append((suit_name + fs_wrapper.DOT_TAG + case[1], case[1]))
        return all_case_name_list

    def loadBgTestSuit(self,base_path):
        suit_name = "test_suit_background"
        test_suit = BgTestSuitBase(suit_name, "This is a background suit.")
        log_test_framework(TAG, "suit_name:"+suit_name)
        log_test_framework(TAG, "base_path:"+base_path)
        case_list = self.getCaseList(base_path)
        for case in case_list:
            log_test_framework(TAG,  "add background case:"+case[1])
            case_suit_name = case[0][:case[0].index('.')]
            case_config_map = fs_wrapper.get_test_case_config(case[1], case_suit_name, True)
            self.addTestCase(test_suit, case_config_map, case[0] + fs_wrapper.DOT_TAG + case[1], case_suit_name, case[1])
        return test_suit

