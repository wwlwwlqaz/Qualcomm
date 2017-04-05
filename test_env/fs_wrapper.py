'''
   file level operation wrapper for qsst python framework

   This module will provide operations independent of file level difference.
   It provide api to get suites and cases information as: all suit names,
   module names of suites, module names of cases, suit configurations, case
   configurations and so on.

   1.The api provide by this file is used for qsst python framework, not used
   for cases directly.

   2.This file contains file level operation for suit,case and configurations,
   if you want add more similar to , you can add it here. But before you add ,
   I recommend you understand the architecture of dir, also the prefix and suffix
   of the files.


   @author: U{zhibinw<zhibinw@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{test_loader <test_loader>}
   @see: L{test_case_base<test_case_base>}
   @see: L{test_suit_base<test_suit_base>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import os
from os import path
from xml.dom.minidom import parse
from logging_wrapper import log_test_framework
from test_suit_base import SuitInfo
from exception import AttributeException

TEST_SUIT_TAG = 'test_suit_'
PY_SUFFIX = '.py'
XML_SUFFIX = '.xml'
DOT_TAG = '.'
CASE_TAG = '_case'
PATH_SEPARATOR = '/'

SUIT_ENABLE_ATTR = "enable"
'''no use'''
SUIT_ENTRY_ATTR = "entry"
SUIT_NAME_ATTR = "name"
'''no use'''
SUIT_RUNNER_ATTR = "runner"
'''no use'''
SUIT_SOCKET_ATTR = "socket"
'''no use'''
SUIT_LOGPATH_ATTR = "logpath"
'''no use '''
SUIT_TIMEWAIT_ATTR = "timewait"
SUIT_APP_NAME = 'app_name'
SUIT_DESCRIPTION = 'description'

SUIT_REQUIRED_ATTRS = [SUIT_ENABLE_ATTR, SUIT_NAME_ATTR,SUIT_APP_NAME]
BG_SUIT_REQUIRED_ATTRS = [SUIT_ENABLE_ATTR, SUIT_NAME_ATTR]

SEQUENCE_NUMBER = "sequence_number"

CASE_NAME_ATTR = "name"
CASE_ENTRY_ATTR = "entry"
CASE_ENABLE_ATTR = "enable"
CASE_DEPENDENCY_ATTR = "dependency"
CASE_INTERACTIVE_ATTR = "interactive"

'''no use'''
CASE_RELATIVE_SUIT_LIST_ATTR = "relative_suits"
CASE_APP_NAME = "app_name"
CASE_DESCRIPTION = 'description'
CASE_REFERENCE = "reference"
CASE_DEPEND_CAPACITY = "depend_capacity"
CASE_DISABLE_HOSTLOGGING = "disable_auto_hostlogging"
CASE_AUTO_LOGGING_ENV_CONTEXT_ATTR = "auto_logging_env_context"
CASE_ITEMS_FOR_AUTO_LOGGING_ATTR = "env_context_items_for_auto_logging"
CASE_ENABLE_WATCHER_ANR_AND_FC = "enable_watcher_anr_fc"

CASE_REQUIRED_ATTRS = [CASE_NAME_ATTR, CASE_ENABLE_ATTR]
CASE_RELATIVE_SUIT_LIST_ATTR_SEPARATOR = ", "

SYMBOL_LINE_BREAK = '\n'
SUIT_CONFIG_SYMBOL1 = ': '
SUIT_CONFIG_SYMBOL2 = ', '

SUIT_INFO_TEST_PKG_NAME_INDEX = 0
SUIT_INFO_TEST_SOCKET_INDEX = 1
SUIT_INFO_TEST_TIME_WAIT_INDEX = 2
SUIT_INFO_TARGET_PKG_NAME_INDEX = 3
SUIT_INFO_TARGET_ACTIVITY_NAME_INDEX = 4

ACCESSIBILITY_SOCKET_NAME = 'myuiautomator'
QSSTSERVICE_SOCKET_NAME = 'myqsstservice'

PRECONDITION_SETTINGS_PATH = "settings"
PRECONDITION_SETTINGS_PREFIX = "test_suit_settings"
run_init_settings = False
TAG = 'fs_wrapper'

def get_suit_name_list(search_path):
    '''
    get all suite names from a given path.

    @type search_path: string
    @param search_path: path contains test suits.
    @return: all suite names in the given path.
    '''
    suit_name_list = []
    search_path = path.normpath(search_path)
    if path.exists(search_path):
        if path.isdir(search_path):
            curFileNameList = os.listdir(search_path)
            curFileNameList = sort_suit_list(search_path, curFileNameList)
            for tempFileName in curFileNameList:
                if tempFileName.startswith(TEST_SUIT_TAG) and path.isdir(search_path + PATH_SEPARATOR + tempFileName):
                    suit_name_list.append(tempFileName)
    return suit_name_list

def sort_suit_list(search_path, list):
    is_bg_case = "background_case_pool" in search_path
    list.sort()
    tmp_list = list[:]
    for i in range(0, list.__len__()):
        suit = list[i]
        if TEST_SUIT_TAG in suit and path.isdir(search_path + PATH_SEPARATOR + suit):
            suit_map = get_test_suit_config(suit, is_bg_case)
            sn = suit_map.get(SEQUENCE_NUMBER)
            if sn != None and int(sn) != i:
                tmp_list.remove(suit)
                tmp_list.insert(int(sn), suit)
    return tmp_list

def sort_case_list(list, suit_name, is_bg_case):
    list.sort()
    tmp_list = list[:]
    for i in range(0, list.__len__()):
        case = list[i]
        if case.startswith(suit_name + CASE_TAG) and case.endswith(XML_SUFFIX):
            case_map = get_test_case_config(case[:-4], suit_name, is_bg_case)
            sn = case_map.get(SEQUENCE_NUMBER)
            if sn != None and int(sn) != i:
                tmp_list.remove(case)
                tmp_list.insert(int(sn), case)
    return tmp_list

def get_suit_py_module_name(suit_name):
    '''
    get module name of a suit, usually it will return
    suit_name.suit_name as python module name, format
    is: test_suit_contacts.test_suit_contacts

    @type suit_name:string
    @param suit_name: name of a suit.
    @return: python module name of this suit.
    '''
    suit_name = path.normpath(suit_name)
    if run_init_settings:
        if path.exists(PRECONDITION_SETTINGS_PATH):
            if path.isdir(PRECONDITION_SETTINGS_PATH):
                curFileNameList = os.listdir(PRECONDITION_SETTINGS_PATH)
                for tempFileName in curFileNameList:
                    if tempFileName == (suit_name + PY_SUFFIX):
                        return (PRECONDITION_SETTINGS_PATH + DOT_TAG + suit_name)
    else:
        if path.exists(suit_name):
            if path.isdir(suit_name):
                curFileNameList = os.listdir(suit_name)
                for tempFileName in curFileNameList:
                    if tempFileName == (suit_name + PY_SUFFIX):
                        return (suit_name + DOT_TAG + suit_name)
    return ''

def cmp_case(case1, case2):
    '''
    compare two cases, used for sort cases.
    the case is a tuple,  format is:
    ('test_suit_contacts.test_suit_contacts_case1',test_suit_contacts_case1')
    it will get the last number 1 to compare.

    @type case1: tuple
    @param case1: first case to compare.
    @type case2: tuple
    @param case2: second case to compare.
    @return: difference of the last number.
    '''

    int1 = int(case1[1][case1[1].index(CASE_TAG)+len(CASE_TAG):])
    int2 = int(case2[1][case2[1].index(CASE_TAG)+len(CASE_TAG):])
    return int1-int2

def get_all_cases_py_module_name(suit_name, is_bg_case=False):
    '''
    get all cases' module name as a list in a suit by pass the suit name.
    the cases' module name is in a list of tuple , a  tuple's format is:
    ('test_suit_contacts.test_suit_contacts_case1','test_suit_contacts_case1')

    @type suit_name: string
    @param suit_name: a suit name string.
    @type suit_name: boolean
    @param is_bg_case: whether is background suit.
    @return: a list contains cases names in tuple.
    '''
    cases = []
    suit_name = path.normpath(suit_name)
    if run_init_settings:
        if path.exists(PRECONDITION_SETTINGS_PATH):
            if path.isdir(PRECONDITION_SETTINGS_PATH):
                curFileNameList = os.listdir(PRECONDITION_SETTINGS_PATH)
                for tempFileName in curFileNameList:
                    if tempFileName.startswith(PRECONDITION_SETTINGS_PREFIX + CASE_TAG) and tempFileName.endswith(XML_SUFFIX):
                        cases.append((PRECONDITION_SETTINGS_PATH + DOT_TAG + tempFileName[:-len(XML_SUFFIX)], tempFileName[:-len(XML_SUFFIX)]))
    else:
        if (is_bg_case == True):
            from background_case_pool.bg_test_loader import BACKGROUND_CASE_POOL
            suit_path = BACKGROUND_CASE_POOL + PATH_SEPARATOR + suit_name
        else:
            suit_path = suit_name
        if path.exists(suit_path):
            if path.isdir(suit_path):
                curFileNameList = os.listdir(suit_path)
                curFileNameList = sort_case_list(curFileNameList, suit_name, is_bg_case)
                for tempFileName in curFileNameList:
                    if tempFileName.startswith(suit_name + CASE_TAG) and tempFileName.endswith(XML_SUFFIX):
                        cases.append((suit_name + DOT_TAG + tempFileName[:-len(XML_SUFFIX)], tempFileName[:-len(XML_SUFFIX)]))
#     cases = sorted(cases, cmp=cmp_case)
    return cases

def get_test_suit_config(suit_name,is_bg_suit=False):
    '''
    get a suit's configuration from its xml file(eg:test_suit_contacts.xml),
    and return it as map.

    @type suit_name: string
    @param suit_name: suit name.
    @type is_bg_case: boolean
    @param is_bg_case: whether is background suit.
    @return: map contains the configuration of this suit.
    '''
    result_map = {}
    if (is_bg_suit == True):
        from background_case_pool.bg_test_loader import BACKGROUND_CASE_POOL
        xml_file_name = BACKGROUND_CASE_POOL + PATH_SEPARATOR+ suit_name + PATH_SEPARATOR + suit_name + XML_SUFFIX
    else:
        xml_file_name = suit_name + PATH_SEPARATOR + suit_name + XML_SUFFIX
    if run_init_settings:
        xml_file_name = PRECONDITION_SETTINGS_PATH + PATH_SEPARATOR + suit_name + XML_SUFFIX
    if path.exists(xml_file_name):
        if path.isfile(xml_file_name):
            try:
                xml_file = open(xml_file_name)
            except IOError:
                log_test_framework(TAG, "Open file " + xml_file_name + " error")
                return result_map
            xml_dom = parse(xml_file)
            root = xml_dom.documentElement
            all_attrs = root.attributes.keys()
            for attr in all_attrs:
                result_map[attr] = root.getAttribute(attr)

            if (is_bg_suit == True):
                REQUIRED_ATTRS = BG_SUIT_REQUIRED_ATTRS
            else:
                REQUIRED_ATTRS = SUIT_REQUIRED_ATTRS

            for requiredAtrr in REQUIRED_ATTRS:
                #check the required key , if no the key in the map , return empty
                if not result_map.has_key(requiredAtrr):
                    raise AttributeException('Need '+requiredAtrr+" attribute in "+suit_name)
    return result_map

def get_test_case_config(case_name, suit_name, is_bg_case=False):
    '''
    get a case's configuration from its xml file(eg:test_case_contacts.xml),
    and return it as map.

    @type case_name: string
    @param case_name: case name.
    @type suit_name: string
    @param suit_name: suite name contains this case.
    @type is_bg_case: boolean
    @param is_bg_case: whether is background case.
    @return: map contains the configuration of this case.
    '''
    result_map = {}
    if (is_bg_case == True):
        from background_case_pool.bg_test_loader import BACKGROUND_CASE_POOL
        xml_file_name = BACKGROUND_CASE_POOL + PATH_SEPARATOR+ suit_name + PATH_SEPARATOR + case_name + XML_SUFFIX
    else:
        xml_file_name = suit_name + PATH_SEPARATOR + case_name + XML_SUFFIX

    if run_init_settings:
        xml_file_name = PRECONDITION_SETTINGS_PATH + PATH_SEPARATOR + case_name + XML_SUFFIX
    if path.exists(xml_file_name):
        if path.isfile(xml_file_name):
            try:
                xml_file = open(xml_file_name)
            except IOError:
                log_test_framework(TAG, "Open file " + xml_file_name + " error")
                return result_map
            xml_dom = parse(xml_file)
            root = xml_dom.documentElement
            all_attrs = root.attributes.keys()
            for attr in all_attrs:
                result_map[attr] = root.getAttribute(attr)
            for requiredAtrr in CASE_REQUIRED_ATTRS:
                #check the required key , if no the key in the map , return empty
                if not result_map.has_key(requiredAtrr):
                    raise AttributeException('Need '+requiredAtrr+" attribute in "+case_name)
    return result_map

def parse_suit_list(suit_list_string, result):
    '''
    used by old version for relative suits, DO NOT uset it any more. 
    '''
    if len(suit_list_string) == 0:
        return
    suits = suit_list_string.split(CASE_RELATIVE_SUIT_LIST_ATTR_SEPARATOR)
    for item in suits:
        result.append(item)

def get_all_suit_config(config_filename):
    '''
    used by old version, DO NOT uset it any more.
    '''
    all_suit_config_map = {}
    try:
        config_file = open(config_filename, 'r')
    except IOError:
        log_test_framework(TAG,"Config file: '" + config_filename + "' doesn't exist or can't be opened!")
        return all_suit_config_map
    lines = config_file.readlines()
    for line in lines:
        line = line.strip(SYMBOL_LINE_BREAK)
        if len(line) != 0:
            items = line.split(SUIT_CONFIG_SYMBOL1)
            suit_name = items[0]
            attrs = items[1].split(SUIT_CONFIG_SYMBOL2)
            all_suit_config_map[suit_name] = []
            all_suit_config_map[suit_name].append(attrs[0])
            all_suit_config_map[suit_name].append(attrs[1])
            all_suit_config_map[suit_name].append(attrs[2])
            if len(attrs) == 5:
                all_suit_config_map[suit_name].append(attrs[3])
                all_suit_config_map[suit_name].append(attrs[4])
    return all_suit_config_map

def get_test_config(config_filename):
    '''
    used by old version, DO NOT use it any more.
    '''
    all_suit_config_map = {}
    try:
        config_file = open(config_filename, 'r')
    except IOError:
        log_test_framework(TAG,"Config file: '" + config_filename + "' doesn't exist or can't be opened!")
        return all_suit_config_map
    lines = config_file.readlines()
    for line in lines:
        line = line.strip(SYMBOL_LINE_BREAK)
        if len(line) != 0:
            items = line.split(SUIT_CONFIG_SYMBOL1)
            suit_name = items[0]
            attrs = items[1].split(SUIT_CONFIG_SYMBOL2)
            suit_info = SuitInfo(suit_name, *attrs)
            all_suit_config_map[suit_name] = suit_info
    return all_suit_config_map
