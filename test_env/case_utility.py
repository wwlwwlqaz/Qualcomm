#coding=utf-8

'''
   case level utility for case writers

   This module will provide api to simulate user operation in DUT,get DUT info,
   status,context and so on.

   1.The api provided by this file is used for cases directly.

   2.If you want to add more similar to, you can add it here.
   Parts of api will communicate with uiautomator which play as a server. The api
   has a similar template.Before you add, recommend refer to existed api.


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{utility_wrapper <utility_wrapper>}
   @see: L{platform_check<platform_check>}
   @see: L{logging_wrapper<logging_wrapper>}
   @note:
   @attention:
   @bug:
   @warning:



'''
from utility_wrapper import *
from platform_check import get_platform_info
from logging_wrapper import *
import time
from subprocess import PIPE, Popen
from platform_check import get_platform_info
import os
import signal
import utility_wrapper
import random
from exception import SocketException,AssertFailedException

_LOG_TAG = 'case_utility'

'''action value used for communicating with uiautomator'''
#ACTION_END = '0'
ACTION_CLICK = '1'
ACTION_GO_BACK = '2'
ACTION_ENTER_TEXT = '3'
ACTION_SCREENSHOT = '4'
ACTION_RESTART_APP = '5'
ACTION_SHUTDOWN_APP ='6'
ACTION_START_APP = '7'
ACTION_DRAG = '8'
ACTION_SEND_KEY = '9'
ACTION_SEARCH_TEXT = '10'
#ACTION_START_ACTIVITY = '11'
ACTION_SEARCH_WEBVIEW_TITLE = '11'
ACTION_GET_BOOLEAN = '12'
ACTION_SET_VALUE = '13'
ACTION_SEARCH_VIEW = '14'
ACTION_CHECK_EXTERNAL_STORAGE = '15'
ACTION_CHECK_SYSTEM_LANGUAGE = '16'
ACTION_GET_ACTIVITY_NAME = '17'
ACTION_GET_VIEW_STATUS = '18'
ACTION_CLICK_BLIND = '19'
ACTION_LONG_CLICK = '20'
ACTION_CLEAR_TEXT = '21'
ACTION_UPDATE_REGISTER = '22'
ACTION_UPDATE_UNREGISTER = '23'
ACTION_DOUBLE_CLICK = '24'
ACTION_ZOOM = '25'
ACTION_GET_DISPLAY_WIDTH = '26'
ACTION_GET_DISPLAY_HEIGHT = '27'
ACTION_SLEEP = '28'
ACTION_WAKEUP = '29'
ACTION_ALARMER_UNREGISTER = '30'
ACTION_SEND_MMS = '31'
ACTION_ENABLE_SCROLL_PROFILING = '32'
ACTION_DISABLE_SCROLL_PROFILING = '33'
ACTION_GET_TEXT = '34'
ACTION_GET_POSTION = '35'
ACTION_GET_SPEED = '36'
ACTION_GET_BATTERY_TEMPERATE = '37'
ACTION_GET_ORIENTATION = '38'
ACTION_GET_AVAILABLE_RAM = '39'
ACTION_GET_AVAILABLE_ROM = '40'
ACTION_GET_WIFI_RSSI = '41'
ACTION_MT_TRIGGER_SERVICE = '43'
ACTION_UPDATE_NOTIFICATION = '44'
ACTION_GET_SIM_CARD_STATE = '45'
ACTION_GET_SIM_CARD_RSSI = '46'
ACTION_CHECK_BLUETOOTH = '47'
ACTION_CHECK_WIFI = '48'
ACTION_GET_VIEW_TEXT = '49'
ACTION_GET_VIEW_ENABLED = '50'
ACTION_GET_NETWORKTYPE = '51'
ACTION_WATCHER_REGISTER = '52'
ACTION_LEFT_DRAG = '53'
ACTION_RIGHT_DRAG = '54'

'''temperate unit'''
#temperate unit
#Celsius
TEMP_UNIT_C = '0'
#Fahrenheit
TEMP_UNIT_F = '1'

'''SIM card'''
#slot1
SLOT_ONE = '0'
#slot2
SLOT_TWO = '1'

'''SIM card state'''
#no SIM card is available in the device
SIM_STATE_ABSENT = 'no available sim card'
#Ready.
SIM_STATE_READY = 'ready'
#SIM Card Deactivated
SIM_STATE_DEACTIVATED = 'deactivated'
#SIM card is unknown or locked or error.
SIM_STATE_UNKNOWN = 'unknown or locked or error'

'''SIM card vendor'''
#SIM card is unknown or locked or error.
SIM_VENDOR_UNKNOW = 'unknown or locked or error'
#no SIM card is available in the device
SIM_VENDOR_ABSENT = 'no available sim card'

''' sim card vendors'''
SIM_VENDOR_CHINA_MOBILE = 'China Mobile'
SIM_VENDOR_CHINA_UNICOM = 'China Unicom'
SIM_VENDOR_CHINA_TELECOM = 'China Telecom'

#sim-card vendors map
VENDOR = {"0":SIM_VENDOR_UNKNOW,
          "1":SIM_VENDOR_ABSENT,
          "46000":SIM_VENDOR_CHINA_MOBILE,
          "46001":SIM_VENDOR_CHINA_UNICOM,
          "46002":SIM_VENDOR_CHINA_MOBILE,
          "46003":SIM_VENDOR_CHINA_TELECOM,
          "46007":SIM_VENDOR_CHINA_MOBILE,
          }
'''RSSI of SIM card '''
#none or unknown signal strength.
SIGNAL_STRENGTH_NONE_OR_UNKNOWN = 'none or unknown'
#poor signal strength.
SIGNAL_STRENGTH_POOR = 'poor'
#moderate signal strength.
SIGNAL_STRENGTH_MODERATE = 'moderate'
#good signal strength.
SIGNAL_STRENGTH_GOOD = 'good'
#great signal strength.
SIGNAL_STRENGTH_GREAT = 'great'

'''view used for action'''
VIEW_MENU_ITEM = '0'
VIEW_TEXT_VIEW = '1'
VIEW_EDIT_TEXT = '2'
VIEW_IMAGE_VIEW = '3'
VIEW_BUTTON = '4'
VIEW_CHECKBOX = '5'
VIEW_LIST = '6'
VIEW_TOGGLEBUTTON = '7'
VIEW_COMPOUNDBUTTON = '8'
VIEW_PROGRESSBAR = '9'

'''type id used for view'''
ID_TYPE_ID = '0'
ID_TYPE_TEXT = '1'
ID_TYPE_INDEX = '2'
ID_TYPE_FOCUSED = '3'
ID_TYPE_DESC = '4'

'''search type'''
#search flag
TEXT_MATCHES = '0'
TEXT_CONTAINS= '1'
TEXT_STARTS_WITH = '2'
TEXT_MATCHES_REGEX = '3'

'''types of scroll screen'''
#specific values
DRAG_UP = '1'
DRAG_DOWN = '2'
DRAG_TO_BOTTOM = '4'
DRAG_TO_TOP = '3'
DRAG_BY_PARAMETER = '0'
ZOOM_DOWN = '5'
ZOOM_UP = '6'

'''values of boolean'''
#for bool
BOOL_TRUE = 'true'
BOOL_FALSE = 'false'

'''keys for send action'''
#for action send key
KEY_RIGHT = '22'
KEY_LEFT = '21'
KEY_UP = '19'
KEY_DOWN = '20'
KEY_ENTER = '66'
KEY_MENU = '82'
KEY_DEL = '67'
KEY_HOME = '3'
KEY_BACK = '4'
KEYCODE_POWER = '26'

'''press type'''
#press type
SHORT_PRESS = '0'
LONG_PRESS = '1'

'''click type'''
#click type
SHORT_CLICK = '0'
LONG_CLICK = '1'

'''view status'''
#view status
VIEW_STATUS_CHECK = '1'
VIEW_STATUS_SELECT = '2'

'''wait time for pause python process'''
WAIT_TIME = 20

'''the name of send value to qsst service'''
SEND_LOG_ROOT = 'LOG_ROOT'
SEND_CYCLE_TIME = 'CYCLE_TIME'
SEND_SUIT_NAME = 'SUIT_NAME'
SEND_CASE_NAME = 'CASE_NAME'
SEND_ITEMS_AUTO_MONITOR_SERVICE_CHANGE = 'ITEMS_AUTO_MONITOR_SERVICE_CHANGE'
SEND_FLAG_AUTO_MONITOR_SERVICE_CHANGE = 'FLAG_AUTO_MONITOR_SERVICE_CHANGE'
SEND_END_CASE = 'END_CASE'
SEND_TEST_ENV_DIR = 'TEST_ENV_DIR'
SEND_TRACKING = 'TRACKING'

#description prefix of tracking
START_RUN = 'Start run '
END = 'End '

#MMS demo attachment.
MMS_DEMO_PLAINTEXT = 'MMSDEMO_PlainText'
MMS_DEMO_PIC60K = 'MMSDEMO_Pic60K'
MMS_DEMO_PIC100K = 'MMSDEMO_Pic100K'
MMS_DEMO_AUDIO100K = 'MMSDEMO_Audio100K'
MMS_DEMO_AUDIO200K = 'MMSDEMO_Audio200K'
MMS_DEMO_AUDIO300K = 'MMSDEMO_Audio300K'
MMS_DEMO_VIDEO200K = 'MMSDEMO_Video200K'
MMS_DEMO_VIDEO300K = 'MMSDEMO_Video300K'


'''constants for group test'''
ACT_AS_HOST_KEY = 'ActAsHost'
SLOT1_PHONE_NUMBER_KEY = 'Slot1PhoneNumber'
SLOT2_PHONE_NUMBER_KEY = 'Slot2PhoneNumber'
GROUP_NAME_KEY = 'GroupName'
DEVICE_NAME_KEY = 'DeviceName'
ROLE_NAME_KEY = 'Role'
STATUS_KEY = 'Status'
TEST_RESULT_KEY = 'Result'
STATUS_INITIALIZED_VALUE = 'Initialized'
STATUS_READY_VALUE = 'Ready'
STATUS_FINISHED_VALUE = 'Finished'
RESULT_SUCCESS_VALUE = 'Success'
RESULT_FAILURE_VALUE = 'Failure'
GOURP_DATABASE_NAME = 'QSST_Group_db'
GOURPS_TABLE_NAME = 'Groups'
GROUP_SERIAL_NUMBER_FILE_NAME = 'SerialNumber'
GROUP_REGISTER_ACTION = 'RegisterGroup_'
ACTIONS_TABLE_NAME = 'Actions'
ACTION_KEY = 'Action'
ACTION_ID_KEY = 'ID'


'''constants for ftp throughput info. '''
#ftp operation
FTP_OP_UPLOAD = 'UPLOAD'
FTP_OP_DOWNLOAD = 'DOWNLOAD'
OP_SUCCEED = 0
OP_FAILED = 1
ftp_invalid_info = {"0": "Ftp init failed",
                 "3": "Upload failed",
                 "4": "Download failed",
                 "5": "File not exist",
                 "6": "Directory not exists",
                 "7":"Invalid operation(download or upload)",
                 }


#if assert failes during one case or not
#can_continue() = True
#click text view
#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
#waitForView: 1 for wait for new Window Change Event, and 0 for just click at once.
@api_log_decorator
def click_textview_by_id(_id, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click textview by id.

    @type _id: string
    @param _id: id of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_textview_by_id(_id, isVerticalList, isScrollable, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_textview_by_text(text, isVerticalList=1, isScrollable=1, searchFlag=TEXT_STARTS_WITH, waitForView=0, clickType=SHORT_CLICK):
    '''
    click textview by text.

    @type text: string
    @param text: text of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type searchFlag: string
    @param searchFlag: matching type, TEXT_MATCHES:text perfect matching; TEXT_CONTAINS:text partial matching;
                       TEXT_STARTS_WITH: matching string the text string starts with; TEXT_MATCHES_REGEX: matching with regex.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(text)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(searchFlag)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_textview_by_text(text, isVerticalList,isScrollable, searchFlag, waitForView,clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_textview_by_desc(desc, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click textview by desc.

    @type desc: string
    @param desc: description of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(desc)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_textview_by_desc(desc,isVerticalList,isScrollable,waitForView,clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_textview_select_by_text(text):
    '''
    check whether exists the textview by the text.

    @type text: string
    @param text: text of textview.
    @return: True:exist, False:not exist.
    '''
    if not can_continue():
        return
    assert_type_string(text)
    try:
        result=get_tls_thrift_client().client_uiautomator.get_textview_select_by_text(text)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_view_text_by_id(view_type, _id, isVerticalList=1, isScrollable=1):
    '''
    get view'text by id
    The view can be textview,edittext,button,checkbox.

    @type view_type: string
    @param view_type: the type of view. can be VIEW_TEXT_VIEW,VIEW_EDIT_TEXT,VIEW_BUTTON,VIEW_CHECKBOX.
    @type _id: string
    @param _id: id of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @return: the text of view
    '''
    if not can_continue():
        return
    assert_type_string(view_type)
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    try:
        result=get_tls_thrift_client().client_uiautomator.get_view_text_by_id(view_type, _id, isVerticalList, isScrollable)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_view_text_by_index(view_type, index):
    '''
    get view'text by index
    The view can be textview,edittext,button,checkbox.

    @type view_type: string
    @param view_type: the type of view. can be VIEW_TEXT_VIEW,VIEW_EDIT_TEXT,VIEW_BUTTON,VIEW_CHECKBOX.
    @type index: number
    @param index: index of textview.
    @return: the text of view
    '''
    if not can_continue():
        return
    assert_type_string(view_type)
    assert_type_int(index)
    try:
        result=get_tls_thrift_client().client_uiautomator.get_view_text_by_index(view_type, index)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def click_textview_by_index(index):
    '''
    click textview by index.

    @type index: number
    @param index: index of textview.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        get_tls_thrift_client().client_uiautomator.click_textview_by_index(index)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def click_in_list_by_index(index, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click list by index. all index should start from 0

    @type index: number
    @param index: index of list.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    #all index should start from 0
    try:
        get_tls_thrift_client().client_uiautomator.click_in_list_by_index(index,isVerticalList, isScrollable, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#click menu item
#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_menuitem_by_text(text, isVerticalList=1, isScrollable=1, searchFlag=TEXT_STARTS_WITH, waitForView=0, clickType=SHORT_CLICK):
    '''
    click menuitem by text.

    @type text: string
    @param text: text of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type searchFlag: string
    @param searchFlag: matching type, TEXT_MATCHES:text perfect matching; TEXT_CONTAINS:text partial matching;
                       TEXT_STARTS_WITH: matching string the text string starts with; TEXT_MATCHES_REGEX: matching with regex.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(text)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(searchFlag)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_menuitem_by_text(text, isVerticalList, isScrollable, searchFlag, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#click image view
@api_log_decorator
def click_imageview_by_index(index):
    '''
    click imageview by index.

    @type index: number
    @param index: index of imageview.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        get_tls_thrift_client().client_uiautomator.click_imageview_by_index(index)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_imageview_by_id(_id, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click imageview by id.

    @type _id: number
    @param _id: id of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_imageview_by_id(_id, isVerticalList, isScrollable, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_imageview_by_desc(desc, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click imageview by description.

    @type desc: description
    @param desc: description of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(desc)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_imageview_by_desc(desc, isVerticalList, isScrollable, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#click button
@api_log_decorator
def click_button_by_index(index):
    '''
    click button by index.

    @type index: number
    @param index: index of button.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        get_tls_thrift_client().client_uiautomator.click_button_by_index(index)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_button_by_id(_id, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click button by id.

    @type _id: id
    @param _id: id of button.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_button_by_id(_id, isVerticalList, isScrollable, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_button_by_text(text, isVerticalList=1, isScrollable=1, searchFlag=TEXT_STARTS_WITH, waitForView=0, clickType=SHORT_CLICK):
    '''
    click button by text.

    @type text: String
    @param text: text of button.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type searchFlag: string
    @param searchFlag: matching type, TEXT_MATCHES:text perfect matching; TEXT_CONTAINS:text partial matching;
                       TEXT_STARTS_WITH: matching string the text string starts with; TEXT_MATCHES_REGEX: matching with regex.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(text)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(searchFlag)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_button_by_text(text, isVerticalList, isScrollable,searchFlag, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def click_checkbox_by_index(index):
    '''
    click checkbox by index.

    @type index: number
    @param index: index of checkbox.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        get_tls_thrift_client().client_uiautomator.click_checkbox_by_index(index)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#isVerticaList: 1 for VerticalList, and 0 for HorizontalList
#isScrollable:  1 for Scrollable, and 0 for disable scroll
@api_log_decorator
def click_checkbox_by_id(_id, isVerticalList=1, isScrollable=1, waitForView=0, clickType=SHORT_CLICK):
    '''
    click checkbox by id.

    @type _id: id
    @param _id: id of checkbox.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type waitForView: number
    @param waitForView: whether wait for new window change event,1:wait for; 0:click at once.
    @type clickType: string
    @param clickType: click type,SHORT_CLICK:Short click; LONG_CLICK:long click.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_int(waitForView)
    assert_type_string(clickType)
    try:
        get_tls_thrift_client().client_uiautomator.click_checkbox_by_id(_id, isVerticalList, isScrollable, waitForView, clickType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#className should be the UI item's class name.
@api_log_decorator
def click_view_by_container_id(_id, className, index):
    '''
    click view by layout id ,the index of the view in layout and UI item's class name when can not directly click the view by its attribute.

    @type _id: id
    @param _id: id of layout.
    @type className: String
    @param className: should be the UI item's class name.
    @type index: number
    @param index: the index of the view in layout.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_string(className)
    assert_type_int(index)
    if not type(index) in [type(0)]:
        index=int(index)
    try:
        get_tls_thrift_client().client_uiautomator.click_view_by_container_id(_id, className, index)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#className should be the UI item's class name.
@api_log_decorator
def click_view_by_container_desc(desc, className, index):
    '''
    click view by layout description ,the index of the view in layout and UI item's class name when the view has no description.

    @type desc: description
    @param desc: description of layout.
    @type className: String
    @param className: should be the UI item's class name.
    @type index: number
    @param index: the index of the view in layout.

    '''
    if not can_continue():
        return
    assert_type_string(desc)
    assert_type_string(className)
    assert_type_int(index)
    try:
        get_tls_thrift_client().client_uiautomator.click_view_by_container_desc(desc, className, index)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def long_click(x, y):
    '''
    long click screen by coordinate point.

    @type x: number
    @param x: x-coordinate point.
    @type y: number
    @param y: y-coordinate point.

    '''
    if not can_continue():
        return
    assert_type_int(x)
    assert_type_int(y)
    try:
        get_tls_thrift_client().client_uiautomator.long_click(x, y)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def double_click(x, y):
    '''
    double click screen by coordinate point.

    @type x: number
    @param x: x-coordinate point.
    @type y: number
    @param y: y-coordinate point.

    '''
    if not can_continue():
        return
    assert_type_int(x)
    assert_type_int(y)
    try:
        get_tls_thrift_client().client_uiautomator.double_click(x, y)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#send key event
@api_log_decorator
def send_key(key, keyType = SHORT_PRESS):
    '''
    send key event.

    @type key: String
    @param key: the defined key event value. Use the KEY_* variables
    @type keyType: String
    @param keyType: press type,SHORT_PRESS:short press; LONG_PRESS:long press.

    '''
    if not can_continue():
        return
    assert_type_string(key)
    try:
        get_tls_thrift_client().client_uiautomator.send_key(key, keyType)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#drag event
@api_log_decorator
def drag_by_param(startX, startY, endX, endY, stepCount):
    '''
    drag screen from one point to another point by some speed.

    @type startX: Number
    @param startX: start x-coordinate postion by percent
    @type startY: Number
    @param startY: start y-coordinate postion by percent
    @type endX: Number
    @param endX: end x-coordinate postion by percent
    @type endY: Number
    @param endY: end y-coordinate postion by percent
    @type stepCount: Number
    @param stepCount: the speed of drag. higher value, lower speed.

    '''
    if not can_continue():
        return
    assert_type_int(startX)
    assert_type_int(startY)
    assert_type_int(endX)
    assert_type_int(endY)
    assert_type_int(stepCount)
    try:
        get_tls_thrift_client().client_uiautomator.drag_by_param(startX, startY, endX, endY, stepCount)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def scroll_up():
    '''
    scroll up screen
    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.scroll_up()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def scroll_down():
    '''
    scroll down screen
    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.scroll_down()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def scroll_to_bottom():
    '''
    scroll screen to bottom
    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.scroll_to_bottom()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def scroll_to_top():
    '''
    scroll screen to top
    '''

    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.scroll_to_top()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#enter edittext
@api_log_decorator
def entertext_edittext_by_id(_id, value, isVerticalList=1, isScrollable=1, isClear=1):
    '''
    Input the text in edittext by id. When need clear firstly, set isClear as 1, otherwise 0.

    @type _id: string
    @param _id: id of edittext.
    @type value: string
    @param value: the enter value.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type isClear: number
    @param isClear: whether clear old value firstly,1:need clear; 0:without clear.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(value)
    try:
        get_tls_thrift_client().client_uiautomator.entertext_edittext_by_id(_id, value, isVerticalList, isScrollable, isClear)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def entertext_edittext_by_index(index, value, isVerticalList=1, isScrollable=1, isClear=1):
    '''
    Input the text in edittext by index. When need clear firstly, set isClear as 1, otherwise 0.

    @type index: number
    @param index: index of edittext.
    @type value: string
    @param value: the enter value.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type isClear: number
    @param isClear: whether clear old value firstly,1:need clear; 0:without clear.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(value)
    try:
        get_tls_thrift_client().client_uiautomator.entertext_edittext_by_index(index, value, isVerticalList, isScrollable, isClear)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def entertext_edittext_on_focused(value, isVerticalList=1, isScrollable=1, isClear=1):
    '''
    Input the text in edittext by edittext value. When need clear firstly, set isClear as 1, otherwise 0.

    @type value: string
    @param value: the editext value.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type isClear: number
    @param isClear: whether clear old value firstly,1:need clear; 0:without clear.

    '''
    if not can_continue():
        return
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(value)
    try:
        get_tls_thrift_client().client_uiautomator.entertext_edittext_on_focused(value, isVerticalList, isScrollable, isClear)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#clear edittext
@api_log_decorator
def clear_edittext_by_id(_id, isVerticalList=1, isScrollable=1):
    '''
    clear edittext value by id.

    @type _id: string
    @param _id: id of editext.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.

    '''
    if not can_continue():
        return
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    try:
        get_tls_thrift_client().client_uiautomator.clear_edittext_by_id(_id, isVerticalList, isScrollable)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def clear_edittext_by_index(index, isVerticalList=1, isScrollable=1):
    '''
    clear edittext value by index.

    @type index: number
    @param index: index of editext.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.

    '''
    if not can_continue():
        return
    assert_type_int(index)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    try:
        get_tls_thrift_client().client_uiautomator.clear_edittext_by_index(index, isVerticalList, isScrollable)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def clear_edittext_on_focused(isVerticalList=1, isScrollable=1):
    '''
    clear the focused edittext.

    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.

    '''
    if not can_continue():
        return
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    try:
        get_tls_thrift_client().client_uiautomator.clear_edittext_on_focused(isVerticalList, isScrollable)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#go back
#className: UI element name. eg: VIEW_PROGRESSBAR, VIEW_CHECKBOX and etc.
#idType: the category which id belongs to. eg: ID_TYPE_ID,ID_TYPE_TEXTS and etc.
@api_log_decorator
def goback(className='', idType='', id=''):
    '''
    go back, that is click the back key.

    @type className: string
    @param className: no use.
    @type idType: string
    @param idType: no use.
    @type id: string
    @param id: no use.

    '''
    send_key( KEY_BACK)
    '''
    if not can_continue():
        return
    assert_type_string(className)
    assert_type_string(idType)
    assert_type_string(id)
    try:
        get_tls_thrift_client().client_uiautomator.goback(className ,idType, id)
    except Thrift.TException, tx:
        deal_remote_exception(tx)
    '''

@api_log_decorator
def shutdown():
    '''
    shut down current app
    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.shutdown()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def sleep(_time):
    '''
    sleep some time

    @type _time:number
    @param _time: the seconds of sleep time

    '''
    if not can_continue():
        return
    time.sleep(_time)

#search text
@api_log_decorator
def search_text(text, isVerticalList=1, isScrollable=1, searchFlag=TEXT_STARTS_WITH):
    '''
    search text.

    @type text: string
    @param text: text of textview.
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type searchFlag: string
    @param searchFlag: matching type, TEXT_MATCHES:text perfect matching; TEXT_CONTAINS:text partial matching;
                       TEXT_STARTS_WITH: matching string the text string starts with; TEXT_MATCHES_REGEX: matching with regex.

    '''
    if not can_continue():
        return False
    assert_type_string(text)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(searchFlag)
    try:
        result=get_tls_thrift_client().client_uiautomator.search_text(text, isVerticalList, isScrollable, searchFlag)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#get textView's text
@api_log_decorator
def get_text(text, isVerticaList=0, isScrollable=0, searchFlag=TEXT_CONTAINS):
    '''
    get textView's text.

    @type text: string
    @param text: text of textview.
    @type isVerticaList: number
    @param isVerticaList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type searchFlag: string
    @param searchFlag: matching type, TEXT_MATCHES:text perfect matching; TEXT_CONTAINS:text partial matching;
                       TEXT_STARTS_WITH: matching string the text string starts with; TEXT_MATCHES_REGEX: matching with regex.

    '''
    if not can_continue():
        return
    assert_type_string(text)
    assert_type_int(isVerticaList)
    assert_type_int(isScrollable)
    assert_type_string(searchFlag)
    try:
        result=get_tls_thrift_client().client_uiautomator.get_text(text, isVerticaList, isScrollable, searchFlag)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)
#search webview title
@api_log_decorator
def search_webview_title(title):
    '''
    search webview title.

    @type title: string
    @param title: title of webview.

    '''
    if not can_continue():
        return False
    assert_type_string(title)
    try:
        result=get_tls_thrift_client().client_uiautomator.search_webview_title(title)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#local function
@api_log_decorator
def local_rm_dir(_dir):
    '''
    remove directory.

    @type _dir: string
    @param _dir: the directory.

    '''
    assert_type_string(_dir)
    os.system('rm -r ' + _dir)

@api_log_decorator
def local_assert(expected, real):
    '''
    set whether continue in case. When expected value is not equal to real value ,then can not continue.

    @type expected: boolean
    @param expected: expected value.
    @type real: boolean
    @param real: real value.

    '''
    if not can_continue():
        return
    if expected != real:
        set_cannot_continue()
        log_test_framework(_LOG_TAG, 'assert fail, real: ' + str(real) + ', expected: ' + str(expected))

@api_log_decorator
def start_activity(package_name, activity_name):
    '''
    manual start activity.

    @type package_name: string
    @param package_name: package name of activity.
    @type activity_name: string
    @param activity_name: activity name.

    '''
    if not can_continue():
        return False
    assert_type_string(package_name)
    assert_type_string(activity_name)
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        os.system("am start " + package_name + "/" + activity_name)
    elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
        os.system("adb shell am start " + package_name + "/" + activity_name)

@api_log_decorator
def reboot_phone():
    '''
    reboot phone.

    '''
    if not can_continue():
        return False
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        os.system("reboot ")
    elif(osInfo == 'Linux-PC' or osInfo == 'Windows'):
        os.system("adb reboot ")

@api_log_decorator
def is_cdma():
    '''
    check whether the network is CMDA or not.

    @return: True: CMDA; False: no.

    '''
    out=os.popen('getprop gsm.operator.numeric').read()
    if out == str("46003\n"):
        return True
    else:
        return False

@api_log_decorator
def is_checkbox_checked_by_text(text):
    '''
    check checkbox whether is checked or not by text.

    @type text: string
    @param text: the text of checkbox

    '''
    if not can_continue():
        return
    assert_type_string(text)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_checkbox_checked_by_text(text)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_checkbox_checked_by_index(index):
    '''
    check checkbox whether is checked or not by index.

    @type index: number
    @param index: the index of checkbox

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_checkbox_checked_by_index(index)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_togglebutton_checked_by_text(text):
    '''
    check togglebutton whether is checked or not by text.

    @type text: string
    @param text: the text of togglebutton

    '''
    if not can_continue():
        return
    assert_type_string(text)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_togglebutton_checked_by_text(text)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_togglebutton_checked_by_index(index):
    '''
    check togglebutton whether is checked or not by index.

    @type index: number
    @param index: the index of togglebutton

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_togglebutton_checked_by_index(index)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_compoundbutton_checked_by_index(index):
    '''
    check compoundbutton whether is checked or not by index.

    @type index: number
    @param index: the index of compoundbutton

    '''
    if not can_continue():
        return
    assert_type_int(index)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_compoundbutton_checked_by_index(index)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_view_enabled_by_id(view_type, _id, isVerticalList=1, isScrollable=1):
    '''
    check view whether is enabled or not by id.
    The view can be textview,edittext,button,checkbox,imageview,togglebutton,compoundbutton.

    @type view_type: string
    @param view_type: the type of view. can be VIEW_TEXT_VIEW,VIEW_EDIT_TEXT,VIEW_BUTTON,VIEW_CHECKBOX,VIEW_IMAGE_VIEW,VIEW_TOGGLEBUTTON,VIEW_COMPOUNDBUTTON.
    @type id: number
    @param id: the id of textview
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    '''
    if not can_continue():
        return
    assert_type_string(view_type)
    assert_type_string(_id)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_view_enabled_by_id(view_type, _id, isVerticalList, isScrollable)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_view_enabled_by_text(view_type, text, isVerticalList=1, isScrollable=1, searchFlag=TEXT_STARTS_WITH):
    '''
    check view whether is enabled or not by text.
    The view can be textview,edittext,button,checkbox,imageview,togglebutton,compoundbutton.

    @type view_type: string
    @param view_type: the type of view. can be VIEW_TEXT_VIEW,VIEW_EDIT_TEXT,VIEW_BUTTON,VIEW_CHECKBOX,VIEW_IMAGE_VIEW,VIEW_TOGGLEBUTTON,VIEW_COMPOUNDBUTTON.
    @type text: string
    @param text: the text of textview
    @type isVerticalList: number
    @param isVerticalList: search direction,1:vertical; 0:horizontal.
    @type isScrollable: number
    @param isScrollable: whether scroll when search textview id,1:scrollable; 0:disable scroll.
    @type searchFlag: string
    @param searchFlag: matching type, TEXT_MATCHES:text perfect matching; TEXT_CONTAINS:text partial matching;
                       TEXT_STARTS_WITH: matching string the text string starts with; TEXT_MATCHES_REGEX: matching with regex.
    '''
    if not can_continue():
        return
    assert_type_string(view_type)
    assert_type_string(text)
    assert_type_int(isVerticalList)
    assert_type_int(isScrollable)
    assert_type_string(searchFlag)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_view_enabled_by_text(view_type, text, isVerticalList, isScrollable, searchFlag)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_view_enabled_by_index(view_type, index):
    '''
    check view whether is enabled or not by index.
    The view can be textview,edittext,button,checkbox,imageview,togglebutton,compoundbutton.

    @type view_type: string
    @param view_type: the type of view. can be VIEW_TEXT_VIEW,VIEW_EDIT_TEXT,VIEW_BUTTON,VIEW_CHECKBOX,VIEW_IMAGE_VIEW,VIEW_TOGGLEBUTTON,VIEW_COMPOUNDBUTTON,VIEW_LIST.
    @type index: number
    @param index: the index of imageview

    '''
    if not can_continue():
        return
    assert_type_string(view_type)
    assert_type_int(index)
    try:
        result=get_tls_thrift_client().client_uiautomator.is_view_enabled_by_index(view_type, index)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def set_progressbar_by_index(index, value):
    '''
    set progressbar by index.

    @type index: number
    @param index: the index of progressbar
    @type value: string
    @param value: the value of progressbar

    '''
    if not can_continue():
        return
    assert_type_int(index)
    assert_type_string(value)
    try:
        get_tls_thrift_client().client_uiautomator.set_progressbar_by_index(index, value)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def search_view_by_id(_id):
    '''
    check whether exists view by id.

    @type _id: string
    @param _id: the id of view
    @return: True: exist; False: no.

    '''
    if not can_continue():
        return False
    assert_type_string(_id)
    try:
        result=get_tls_thrift_client().client_uiautomator.search_view_by_id(_id)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def search_view_by_desc(desc):
    '''
    check whether exists view by description.

    @type desc: string
    @param desc: the description of view
    @return: True: exist; False: no.

    '''
    if not can_continue():
        return False
    assert_type_string(desc)
    try:
        result=get_tls_thrift_client().client_uiautomator.search_view_by_desc(desc)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_external_storage_enable():
    '''
    check whether exists enable external storage.

    @return: True: exist; False: no.

    '''
    if not can_continue():
        return False
    try:
        result=get_tls_thrift_client().client_uiautomator.is_external_storage_enable()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_system_language():
    '''
    get current system language.

    @return: the system language.
    '''

    if not can_continue():
        return ''
    try:
        result=get_tls_thrift_client().client_uiautomator.get_system_language()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)


@api_log_decorator
def get_activity_name():  #获取当前的activity名字
    '''
    get current activity name.

    @return: current activity name.
    '''

    try:
        #result=get_tls_thrift_client().client_uiautomator.get_activity_name()
        #return result
        log_test_framework(_LOG_TAG, 'hard code get activity name')
        return 'com.android.launcher2.Launcher'
    except Thrift.TException, tx:
        deal_remote_exception(tx)
        
@api_log_decorator
def get_activity_name_1():
    '''
    get current activity name.

    @return: current activity name.
    '''

    try:
        result=get_tls_thrift_client().client_uiautomator.get_activity_name()
        log_test_framework(_LOG_TAG, 'hard code get activity name')
        return result
        #return 'com.android.launcher2.Launcher'
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def click(x,y):
    '''
    click screen by coordinate point.

    @type x: number
    @param x: x-coordinate point.
    @type y: number
    @param y: y-coordinate point.

    '''
    if not can_continue():
        return ''
    #cmd = generate_cmd(ACTION_GET_ACTIVITY_NAME, '','', '', [str(x),str(y)])
    #log_test_framework(_LOG_TAG, 'send: ' + cmd)
    run_cmd("input  tap " + str(x) +" " + str(y))
    #log_test_framework(_LOG_TAG, 'receive: 1')
    #log_test_framework(_LOG_TAG, 'ok without result')

@api_log_decorator
def wait_for_fun(fun,flag,timeout,sleeptime=1):
    '''
    It will loop the fun operation until the return value of fun is same with flag or wait time
    reaches the timeout. If fun success , wait_for_fun will return true , else will return false.

    @type fun: string
    @param fun: the fun operation.
    @type flag: boolean
    @param flag: expected flag value.
    @type timeout: number
    @param timeout: time out.
    @type sleeptime: number
    @param sleeptime: the seconds of sleep time.

    '''
    start_time = time.time()
    while int(time.time()) - int(start_time) < int(timeout):
        if fun() == flag:
            log_test_framework(_LOG_TAG,str(fun) + ' expected '+ str(flag))
            return True
        else:
            sleep(sleeptime)
    return False

@api_log_decorator
def run_time_for_fun(fun):
    '''
    get the running time of function.

    usage:
            wait_fun = lambda: something fun name
            e.g  wait_fun = lambda:browser.access_browser(SC.PRIVATE_BROWSER_ADDRESS_URL, SC.PRIVATE_BROWSER_WEB_TITLE, SC.PRIVATE_BROWSER_WAIT_TIME)
            run_time = run_time_for_fun(wait_fun)

    @type fun: string
    @param fun: the fun operation.
    @return: the running time.

    '''
    start_time = time.time()
    fun()
    return int(time.time()) - int(start_time)

#appName: application name.
#className: UI element name. eg: VIEW_PROGRESSBAR, VIEW_CHECKBOX and etc.
#idType: the category which id belongs to. eg: ID_TYPE_ID,ID_TYPE_TEXTS and etc.
#aciton: the type of action which will be performed when condition is matched. only support ACTION_CLICK and ACTION_GO_BACK
@api_log_decorator
def register_update_watcher(appName, className, idType, id, action):
    '''
    register a watcher to deal with suddenly pop up  events in background.

    @type appName: string
    @param appName: application name.
    @type className: string
    @param className: UI element name. eg: VIEW_PROGRESSBAR, VIEW_CHECKBOX and etc.
    @type idType: string
    @param idType: the category which id belongs to. eg: ID_TYPE_ID,ID_TYPE_TEXTS and etc.
    @type id: string
    @param id: the id of the view.
    @type action: string
    @param action: the type of action which will be performed when condition is matched. only support ACTION_CLICK and ACTION_GO_BACK

    '''
    #if not can_continue():
    #    return
    assert_type_string(appName)
    assert_type_string(className)
    assert_type_string(idType)
    assert_type_string(id)
    assert_type_string(action)
    try:
        get_tls_thrift_client().client_uiautomator.register_update_watcher(appName, className, idType, id, action)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def register_condition_action_watcher( packageName_condition,className_condition,idType_condition,id_condition,
    action,className_action,idType_action,id_action ):
    '''
    register a watcher to deal with suddenly interrupt condition.
    The following 4 parameters define the interrupt condition:
        [ packageName_condition,  className_condition, idType_condition, id_condition]
    The others parameters define how to do next after find the interrupt?
        [action,             className_action,    idType_action,    id_action]
    For example: check some special text for interrupt condition,
    and click the ok_button close the interrupt.

    @type packageName_condition: string
    @param packageName_condition: package  name.
    @type className_condition/className_action: string
    @param className_condition/className_action:
        UI element name. eg: VIEW_PROGRESSBAR, VIEW_CHECKBOX and etc.
    @type idType_condition/idType_action: string
    @param idType_condition / idType_action :
        the category which id belongs to. eg: ID_TYPE_ID,ID_TYPE_TEXTS and etc.
    @type id_condition/id_action: string
    @param id_action/id_condition : the id of the view.
    @type action: string
    @param action: the type of action which will be performed when condition is matched.
    current only support ACTION_CLICK,ACTION_GO_BACK and ACTION_LEFT_DRAG /ACTION_RIGHT_DRAG

    '''
    #if not can_continue():
    #    return
    assert_type_string(className_action)
    assert_type_string(idType_action)
    assert_type_string(id_action)
    assert_type_string(action)
    osInfo = get_platform_info()
    #if(osInfo == 'Linux-Phone'):
    if(osInfo == 'Linux-Phone' or osInfo == 'Windows'):
        try:
            log_test_framework(_LOG_TAG, ' WATCHER condition REGISTER className ' + str(className_condition) )
            get_tls_thrift_client().client_uiautomator.register_condition_action_watcher(packageName_condition,className_condition,idType_condition,id_condition,action,className_action,idType_action,id_action )
        except Thrift.TException, tx:
            deal_remote_exception(tx)

#appName: application name.
@api_log_decorator
def unregister_update_watcher(appName):
    '''
    unregister the update watcher.

    @type appName: string
    @param appName: application name.

    '''
    if not can_continue():
        return
    assert_type_string(appName)
    try:
        get_tls_thrift_client().client_uiautomator.unregister_update_watcher(appName)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#mode: should be ZOOM_DOWN/ZOOM_UP
@api_log_decorator
def zoom_by_param(mode, startX1 = -1, startY1 = 1, startX2 = -1, startY2 = -1):
    '''
    zoom down or zoom up screen.

    @type mode: string
    @param mode: the mode of zoom,ZOOM_DOWN/ZOOM_UP
    @type startX1: Number
    @param startX1: start x-coordinate postion by percent
    @type startY1: Number
    @param startY1: start y-coordinate postion by percent
    @type startX2: Number
    @param startX2: end x-coordinate postion by percent
    @type startY2: Number
    @param startY2: end y-coordinate postion by percent

    '''
    if not can_continue():
        return
    assert_type_int(startX1)
    assert_type_int(startY1)
    assert_type_int(startX2)
    assert_type_int(startY2)
    assert_type_string(mode)
    try:
        get_tls_thrift_client().client_uiautomator.zoom_by_param(mode, startX1, startY1, startX2, startY2)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def getDisplayWidth():
    '''
    get display width.

    @return: display width
    '''
    try:
        result=get_tls_thrift_client().client_uiautomator.getDisplayWidth()
        return str(result)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def getDisplayHeight():
    '''
    get display height.

    @return: display height
    '''
    try:
        result=get_tls_thrift_client().client_uiautomator.getDisplayHeight()
        return str(result)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def save_reboot_status(suit_name, case_name):
    '''
    save reboot status into files before reboot.

    @type suit_name: string
    @param suit_name: the current suit name while QSST run.
    @type case_name: string
    @param case_name: the current case name while QSST run.

    '''
    qsst_log_reboot_manual()

@api_log_decorator
def restore_reboot_status():
    '''
    remove previous reboot status files.

    '''
    qsst_log_restore_reboot()

@api_log_decorator
def pause_python_process():
    '''
    pause python process.
    attention:this function can't use on windows system.

    '''
    def myHandler(signum, frame):
        restore_reboot_status()
        qsst_log_case_status(STATUS_FAILED, "Something wrong, the device should be rebooted.", SEVERITY_HIGH)

    signal.signal(signal.SIGALRM, myHandler)
    signal.alarm(WAIT_TIME)
    signal.pause()

@api_log_decorator
def get_reboot_status(suit_name, case_name):
    '''
    get reboot status.

    @type suit_name: string
    @param suit_name: the current suit name.
    @type case_name: string
    @param case_name: the current case name.
    @return: True: reboot status, False:no.

    '''
    if is_suit_in_reboot_status(suit_name) and is_case_in_reboot_status(case_name):
        return True
    return False

#interval: set specific time (seconds) that device will wakeup.
#          default value is -1, means try to sleep device without register alarmer.
@api_log_decorator
def goToSleepMode(interval = -1):
    '''
    go to sleep mode.

    @type interval: number
    @param interval: set specific time (seconds) that device will wakeup.
                      default value is -1, means try to sleep device without register alarmer.

    '''
    if not can_continue():
        return
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        assert_type_int(interval)
        signal.signal(signal.SIGUSR1, wakeUpSignalHandler)
        try:
            result = get_tls_thrift_client().client_qsst.goToSleepMode(interval)
            if not result:
                send_key(KEYCODE_POWER)
        except Thrift.TException, tx:
            deal_remote_exception(tx)
        if(interval > 0):
            signal.pause()

@api_log_decorator
def wakeUpDevice():
    '''
    wake up device.

    '''
    if not can_continue():
        return
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        try:
            get_tls_thrift_client().client_qsst.wakeUpDevice()
        except Thrift.TException, tx:
            deal_remote_exception(tx)

@api_log_decorator
def unregisterAlarmer():
    '''
    finish the process of wake up device before time is up.

    '''
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone'):
        try:
            get_tls_thrift_client().client_qsst.unregisterAlarmer()
        except Thrift.TException, tx:
            deal_remote_exception(tx)

@api_log_decorator
def send_mms(smsto, content):
    '''
    send a mms to specific phone in background by sim card one.

    @type smsto: string
    @param smsto: the number of target phone.
    @type content: string
    @param content: the mms content.

    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_qsst.send_mms(smsto, content)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def mt_trigger_service_call(to, wait_time, hold_time, interval, num_of_calls=1, count_off=True):
    '''
    trigger mt service for a mt call

    @type to: string
    @param to: specify the target phone number.
    @type wait_time: number
    @param wait_time: time for waiting to connect.
    @type hold_time: number
    @param hold_time: holding time for each call.
    @type interval: number
    @param interval: time between two calls, should be larger than < hold_time + wait_time  + 10>
    @type num_of_calls: number
    @param num_of_calls: how many calls want to make.
    @type count_off: boolean
    @param count_off: will speak out the current number of calls once specified true.

    '''
    assert_type_string(to)
    assert_type_int(wait_time)
    assert_type_int(hold_time)
    assert_type_int(interval)
    assert_type_int(num_of_calls)

    trigger_dict = {}

    trigger_dict['\"ReqType\"'] = '\"MTCALL\"'
    trigger_dict['\"CountOff\"'] = str(count_off)
    trigger_dict['\"Interval\"'] = str(interval)
    trigger_dict['\"HoldTime\"'] = str(hold_time)
    trigger_dict['\"To\"'] = '\"' + to + '\"'
    trigger_dict['\"WaitTime\"'] = str(wait_time)
    trigger_dict['\"NumOfCalls\"'] = str(num_of_calls)

    try:
        result_bool=get_tls_thrift_client().client_qsst.mt_trigger_service(trigger_dict)
        return result_bool
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def mt_trigger_service_sms(msg_title_text, to, interval, time_out, count=1, msg_type=0, wap_url=" ",auto_tag=False):
    '''
    trigger mt service for a mt sms/mms/wap push/flash sms

    @type msg_title_text: string
    @param msg_title_text:This will be a body for SMS/WAP PUSH/FLASH SMS , and title for MMS.
                          If trigger mt service for MMS, The msg_title_text must be one of them as following:
                            MMS_DEMO_PLAINTEXT  ----> 'MMSDEMO_PlainText'
                            MMS_DEMO_PIC60K ----> 'MMSDEMO_Pic60K'
                            MMS_DEMO_PIC100K ----> 'MMSDEMO_Pic100K'
                            MMS_DEMO_AUDIO100K ----> 'MMSDEMO_Audio100K'
                            MMS_DEMO_AUDIO200K ----> 'MMSDEMO_Audio200K'
                            MMS_DEMO_AUDIO300K ----> 'MMSDEMO_Audio300K'
                            MMS_DEMO_VIDEO200K ----> 'MMSDEMO_Video200K'
                            MMS_DEMO_VIDEO300K ----> 'MMSDEMO_Video300K'
    @type to: string
    @param to:Specify the target phone number.
    @type interval: number
    @param interval:Time between two consecutive SMS/MMS/WAP PUSH/FLASH SMS.
    @type time_out: number
    @param time_out: Server will abandon the request if it waits over this time.
    @type count: number
    @param count:How many SMS/MMS/WAP PUSH/FLASH SMS you want to make.
    @type msg_type: number
    @param msg_type: Select SMS type you want to send, SMS/MMS/WAP PUSH/FLASH SMS supported.0 for standard SMS, 4 for MMS, 2 for WAP PUSH, 3 for FLASH SMS.
    @type wap_url: string
    @param wap_url: URL for WAP PUSH, if it is SMS/MMS/FLASH SMS, leave it "".
    @type auto_tag: boolean
    @param auto_tag: Whether the mms content contains timestamp and serial number.

    '''
    assert_type_string(msg_title_text)
    assert_type_string(to)
    assert_type_int(interval)
    assert_type_int(time_out)
    assert_type_int(count)
    assert_type_int(msg_type)
    assert_type_string(wap_url)

    trigger_dict = {}

    trigger_dict['\"ReqType\"'] = '\"REQ_SMS\"'
    trigger_dict['\"Count\"'] = str(count)
    trigger_dict['\"MsgTitleText\"'] = '\"' + msg_title_text + '\"'
    trigger_dict['\"Interval\"'] = str(interval)
    trigger_dict['\"WapURL\"'] = '\"' + wap_url + '\"'
    trigger_dict['\"To\"'] = '\"' + to + '\"'
    trigger_dict['\"TimeOut\"'] = str(time_out)
    trigger_dict['\"MsgType\"'] = str(msg_type)
    trigger_dict['\"AutoTag\"'] = str(auto_tag)

    try:
        result_bool=get_tls_thrift_client().client_qsst.mt_trigger_service(trigger_dict)
        return result_bool
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def mt_trigger_service_email(to, subject, body, cc=" ", bcc=" ", count=1):
    '''
    trigger mt service for a mt email

    @type to: string
    @param to:Send MT Email to this address
    @type subject: string
    @param subject:Subject for the email.
    @type body: string
    @param body:Email body.
    @type cc: string
    @param cc:Cc address.
    @type bcc: string
    @param bcc:Bcc address.
    @type count: number
    @param count:How many emails you want to make.

    '''
    assert_type_string(to)
    assert_type_string(subject)
    assert_type_string(body)
    assert_type_string(cc)
    assert_type_string(bcc)
    assert_type_int(count)

    trigger_dict = {}

    trigger_dict['\"ReqType\"'] = '\"SEND_EMAIL\"'
    trigger_dict['\"To\"'] = '\"' + to + '\"'
    trigger_dict['\"Body\"'] = '\"' + body + '\"'
    trigger_dict['\"Subject\"'] = '\"' + subject + '\"'
    trigger_dict['\"Cc\"'] = '\"' + cc + '\"'
    trigger_dict['\"Bcc\"'] = '\"' + bcc + '\"'
    trigger_dict['\"Count\"'] = str(count)

    try:
        result_bool=get_tls_thrift_client().client_qsst.mt_trigger_service(trigger_dict)
        return result_bool
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def mt_trigger_service(t_dict):
    '''
    trigger mt service : such as mt call, mt sms, mt email.

    @type t_dict: dict
    @param t_dict:
            Currently, the api support three types of mt trigger service.
            1. MT Call
                A demo MT Call request is :
                t_dict = {"ReqType":"MTCALL","CountOff":True,"Interval":60,"HoldTime":10,"To":"20365103","WaitTime":40,"NumOfCalls":1}
                ReqType: type of MT trigger service. must be MTCALL.
                CountOff: will speak out the current number of calls once specified True ,or False.
                Interval: time between two calls, should be larger than < hold_time + wait_time  + 10>
                HoldTime: holding time for each call.
                To: specify the target phone number.
                WaitTime: time for waiting to connect.
                NumOfCalls: how many calls want to make.

            2. MT SMS
               A demo MT SMS request:
               t_dict = {"ReqType":"REQ_SMS","Count":1,"MsgTitleText":"test sms","Interval":60,"WapURL":"wap.baidu.com","To":"13764637312","TimeOut":180,"MsgType":0,"AutoTag":True}
               ReqType: type of MT trigger service. must be REQ_SMS.
               Count: How many SMS/MMS/WAP PUSH/FLASH SMS you want to make.
               MsgTitleText: This will be a body for SMS/WAP PUSH/FLASH SMS , and title for MMS.
                             If trigger mt service for MMS, The msg_title_text must be one of them as following:
                                MMS_DEMO_PLAINTEXT  ----> 'MMSDEMO_PlainText'
                                MMS_DEMO_PIC60K ----> 'MMSDEMO_Pic60K'
                                MMS_DEMO_PIC100K ----> 'MMSDEMO_Pic100K'
                                MMS_DEMO_AUDIO100K ----> 'MMSDEMO_Audio100K'
                                MMS_DEMO_AUDIO200K ----> 'MMSDEMO_Audio200K'
                                MMS_DEMO_AUDIO300K ----> 'MMSDEMO_Audio300K'
                                MMS_DEMO_VIDEO200K ----> 'MMSDEMO_Video200K'
                                MMS_DEMO_VIDEO300K ----> 'MMSDEMO_Video300K'
               Interval: between two consecutive SMS/MMS/WAP PUSH/FLASH SMS.
               WapURL: URL for WAP PUSH, if it is SMS/MMS/FLASH SMS, leave it "".
               To: Specify the target phone number.
               TimeOut: Server will abandon the request if it waits over this time.
               MsgType: Select SMS type you want to send, SMS/MMS/WAP PUSH/FLASH SMS supported.0 for standard SMS, 4 for MMS, 2 for WAP PUSH, 3 for FLASH SMS.
               AutoTag: Whether the mms content contains timestamp and serial number. If True, contains, or False.

            3. MT Email
               A demo MT Email request:
               t_dict = {"ReqType":"SEND_EMAIL","Body":"Test Body","Count":1,"Subject":"Test Subject","To":"auto_test_email@163.com","Cc":"auto_test_email@163.com","Bcc":"auto_test_email@163.com"}
               ReqType: type of MT trigger service. must be SEND_EMAIL.
               Body: Email body. Can be "".
               Count: How many emails you want to send.
               Subject: Subject for the email.
               To: Send MT Email to this address.
               Cc: Cc address. Can be "".
               Bcc: Bcc address. Can be "".
    '''

    #analye the dict, and transfer to json formatted.
    trigger_dict = {}
    for (k,v) in  t_dict.items():
        #if value type is string. then add "" in the value. that is. value is abc. then change it to be "abc".
        if isinstance(v,str):
            v = '\"' + v + '\"'
        elif isinstance(v,int) or isinstance(v,bool):
            v = str(v)
        else :
            v = str(v)
        trigger_dict['\"' + k + '\"'] = v

    try:
        result_bool=get_tls_thrift_client().client_qsst.mt_trigger_service(trigger_dict)
        return result_bool
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def enable_scroll_profling():
    '''
    just used for debug fps.

    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.enable_scroll_profling()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def disable_scroll_profling():
    '''
    just used for debug fps.

    '''
    if not can_continue():
        return
    try:
        get_tls_thrift_client().client_uiautomator.disable_scroll_profling()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_postion():
    '''
    get postion of DUT.

    @return: the longitude and latitude.

    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_postion()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_speed():
    '''
    get speed of DUT.

    @return: the speed. unit is meter per second.

    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_speed()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#unit: the unit of battery temperate. eg: TEMP_UNIT_C,TEMP_UNIT_F.
@api_log_decorator
def get_battery_temperate(unit=TEMP_UNIT_C):
    '''
    get temperate of battery.

    @type unit: string
    @param unit: the unit of battery temperate. TEMP_UNIT_C:Celsius; TEMP_UNIT_F:Fahrenheit.
    @return: the temperate.

    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_battery_temperate(unit)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#return value x,y,z
#x: Acceleration force along the x axis
#y: Acceleration force along the y axis
#z: Acceleration force along the z axis
@api_log_decorator
def get_orientation():
    '''
    get orientation.

    @return: x,y,z.
             x: Acceleration force along the x axis
             y: Acceleration force along the y axis
             z: Acceleration force along the z axis.

    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_orientation()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_available_ram():
    '''
    get available RAM.

    @return: the available RAM. unit:M.

    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_available_ram()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_available_rom():
    '''
    get available ROM.

    @return: the available ROM. unit:M.

    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_available_rom()
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_wifi_rssi():
    '''
    get wifi rssi.

    @return: the rssi of the wifi.
             SIGNAL_STRENGTH_NONE_OR_UNKNOWN: none or unknown signal strength.
             SIGNAL_STRENGTH_POOR: poor signal strength.
             SIGNAL_STRENGTH_MODERATE: moderate signal strength.
             SIGNAL_STRENGTH_GOOD: good signal strength.
             SIGNAL_STRENGTH_GREAT: great signal strength.

    '''
    try:
        return get_tls_thrift_client().client_qsst.get_wifi_rssi()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#slotId: sim card. eg: SLOT_ONE,SLOT_TWO.
@api_log_decorator
def get_sim_card_state(slotId):
    '''
    get the state of the device SIM card in a slot.

    @type slotId: string
    @param slotId: the sim card. SLOT_ONE:slot1; SLOT_TWO:slot2.
    @return: the state of the device SIM card in the slot.
             SIM_STATE_ABSENT: SIM card state: no SIM card is available in the device.
             SIM_STATE_READY: SIM card state: Ready.
             SIM_STATE_DEACTIVATED: SIM card state: SIM Card Deactivated.
             SIM_STATE_UNKNOWN: SIM card state: SIM card is unknown or locked or error.
    '''
    try:
        return get_tls_thrift_client().client_qsst.get_sim_card_state(int(slotId))
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#slotId: sim card. eg: SLOT_ONE,SLOT_TWO.
@api_log_decorator
def get_sim_card_vendor(slotId):
    '''
    get the vender of the device SIM card in a slot.

    @type slotId: string
    @param slotId: the sim card. SLOT_ONE:slot1; SLOT_TWO:slot2.
    @return: the vender of the device SIM card in the slot.
             SIM_VENDOR_CHINA_MOBILE: SIM card vendor: China Mobile.
             SIM_VENDOR_CHINA_UNICOM: SIM card vendor: China Unicom.
             SIM_VENDOR_CHINA_TELECOM: SIM card vendor: China Telecom.
             ...
             'SIM_VENDOR_UNKNOW': SIM card vendor: unknown or locked or error
             'SIM_VENDOR_ABSENT': SIM card vendor: no available sim card
    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_sim_card_vendor(slotId)
        if result not in VENDOR:
            log_test_framework("SIMVENDOR_Slot"+slotId, "Current vendor " + result)
            return SIM_VENDOR_UNKNOW
        log_test_framework("SIMVENDOR_Slot"+slotId, "Current vendor " + VENDOR[result])
        return VENDOR[result]
    except Thrift.TException, tx:
        deal_remote_exception(tx)
#slotId: sim card. eg: SLOT_ONE,SLOT_TWO.
@api_log_decorator
def get_sim_card_rssi(slotId):
    '''
    get the rssi of the device SIM card in a slot.

    @type slotId: string
    @param slotId: the sim card. SLOT_ONE:slot1; SLOT_TWO:slot2.
    @return: the rssi of the device SIM card in the slot.
             SIGNAL_STRENGTH_NONE_OR_UNKNOWN: none or unknown signal strength.
             SIGNAL_STRENGTH_POOR: poor signal strength.
             SIGNAL_STRENGTH_MODERATE: moderate signal strength.
             SIGNAL_STRENGTH_GOOD: good signal strength.
             SIGNAL_STRENGTH_GREAT: great signal strength.
    '''
    try:
        return get_tls_thrift_client().client_qsst.get_sim_card_rssi(int(slotId))
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_bluetooth_enabled():
    '''
    get the status of the bluetooth device.

    @return: the status of the bluetooth device.
             True: enabled
             False: disabled.
    '''
    try:
        result_bool=get_tls_thrift_client().client_qsst.is_bluetooth_enabled()
        return result_bool
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def is_wifi_enabled():
    '''
    get the status of the wifi.

    @return: the status of the wifi.
             True: enabled
             False: disabled.
    '''
    try:
        result_bool=get_tls_thrift_client().client_qsst.is_wifi_enabled()
        return result_bool
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#slotId: sim card. eg: SLOT_ONE,SLOT_TWO.
@api_log_decorator
def get_networktype(slotId):
    '''
    get the network type of the device SIM card in a slot.

    @type slotId: string
    @param slotId: the sim card. SLOT_ONE:slot1; SLOT_TWO:slot2.
    @return: the network type of the device SIM card in the slot.
              "CDMA": Includes: CDMA-IS95A, CDMA-IS95B, 1xRTT.
              "EVDO": Includes: EvDo-rev.0, EvDo-rev.A, EvDo-rev.B, eHRPD.
              "GSM": Includes: GPRS.
              "EDGE": Includes: EDGE.
              "H": Includes: HSDPA, HSUPA, HSPA, HSPA+.
              "UMTS": Includes: UMTS.
              "LTE": Includes: LTE.
              "UNKNOWN": Network type is Unknown.
    '''
    try:
        result=get_tls_thrift_client().client_qsst.get_networktype(int(slotId))
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

#inner use: combine cmd.
@api_log_decorator
def get_logcat_cmd(tag,type,raw_cmd):
    '''
    combine command by params

    @type tag: string
    @param tag: the tag of logcat.
    @type type: string
    @param type: the log buffer of logcat.
    @type raw_cmd: string
    @param raw_cmd: the raw command.
    @return: combined command.

    '''
    if(raw_cmd == ""):
        cmd_tag = ""
        if(tag != ""):
            cmd_tag = " -s " + tag+":v "

        cmd_type = ""
        if(type != ""):
            for i in type.split(','):
                cmd_type = cmd_type + " -b " + i
        cmd = cmd_type + cmd_tag
    else:
        cmd = raw_cmd.replace('-d',' ')

    return cmd

#tag: logcat tag, can be empty
#type: log buffer, can be system,main,radio,events. such as system or system,radio.
#raw_cmd: when raw_cmd is not null, the tag and type are ignored
@api_log_decorator
def get_logcat_stream(tag='', type='', raw_cmd=''):
    '''
    get logcat stream in case.

    @type tag: string
    @param tag: the tag of logcat,can be empty.
    @type type: string
    @param type: the log buffer of logcat,can be system,main,radio,events. such as system or system,radio.
    @type raw_cmd: string
    @param raw_cmd: the raw command.when raw_cmd is not null, the tag and type are ignored.
    @return: logcat stream.

    '''
    cmd = get_logcat_cmd(tag,type,raw_cmd)
    osInfo = get_platform_info()
    try:
        if(osInfo == 'Linux-Phone'):
            pipe = Popen("logcat " + cmd,stdout=PIPE,shell=True,executable='sh',bufsize=1)
        elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
            pipe = Popen("adb logcat " + cmd,stdout=PIPE,bufsize=1)
    except Exception as e:
        log_test_framework(_LOG_TAG, "get_logcat_stream error"+str(e))
    return pipe

@api_log_decorator
def get_logcat_string(tag='', type='', raw_cmd=''):
    '''
    get logcat string in case.

    @type tag: string
    @param tag: the tag of logcat,can be empty.
    @type type: string
    @param type: the log buffer of logcat,can be system,main,radio,events. such as system or system,radio.
    @type raw_cmd: string
    @param raw_cmd: the raw command.when raw_cmd is not null, the tag and type are ignored.
    @return: logcat result string

    '''
    logcat_string = ""
    osInfo = get_platform_info()
    cmd = get_logcat_cmd(tag,type,raw_cmd)
    if(osInfo == 'Linux-Phone'):
        cmd = 'logcat -d ' + cmd
    elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
        cmd = 'adb logcat -d ' + cmd
    try:
        pipe = os.popen(cmd)
        logcat_string = pipe.read()
    except Exception as e:
        log_test_framework(_LOG_TAG, "get_logcat_string error"+str(e))
    return logcat_string

@api_log_decorator
def kill_pipe(pipe):
    '''
    kill pipe

    @type pipe: string
    @param pipe: the pipe need to kill

    '''
    #pipe.stdout.close()
    pipe.kill()

@api_log_decorator
def update_notificationbar(text):
    '''
    show progress on notificationbar when qsst is running.
    note:this api not support on PC

    @type tag: string
    @param tag: text that show on notification.

    '''
    try:
        get_tls_thrift_client().client_qsst.update_notificationbar(text)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def isAliveforProcess(pro_name):
    '''
    check a process's living state by given it's process name.

    @type pro_name: string
    @param pro_name: process name.
    @return: boolean
    '''
    os_info = get_platform_info()
    ps_cmd = None
    if os_info == "Linux-Phone":
        ps_cmd = ['ps']
    else:
        ps_cmd = ['adb', 'shell', 'ps']
    p = subprocess.Popen(ps_cmd,stdout=subprocess.PIPE)
    out = p.communicate()[0]
    for line in out.splitlines():
        if pro_name in line:
            return True
    return False

@api_log_decorator
def excute(codes):
    '''
    This is a common method, you can use it to operate view, such as click a view,
    get a text of a view etc.

    @type codes: string
    @param codes: the code that need excute. when uiautomator get these code, it will parse it and excute.
    @note: i assume you have learned uiautomator api, the code need follow the following rules:
            1. "UISELECTOR:;  //the head is UISELECTOR/UISCROLLABL/UIOBJECT, if the object need pass an object, you can write like this:
                UISCROLLABLE:[UISELECTOR:;
                              FUNCTION:1:scrollable;
                              FUNCTION_ARGS:boolean:true;];

                FUNCTION:argument number:function name;
                FUNCTION_ARGS:args type:args name; // if the function need pass an object as an argument, the args name can be a code snippet which is inclued by "[]"
                // for example:
                FUNCTION:2:childSelector;
                FUNCTION_ARGS:UiSelector:[UISELECTOR:;
                                          FUNCTION:1:className;
                                          FUNCTION_ARGS:String:android.widget.TextView;];
               "FUNCTION_ARGS:String:Apps;"
                .
                .
                .
            2. Sometime you maybe have requirement like this: First, new an UiSelector, second, use the UiSelector to new a UiScorllable
               finally, get an object by UiScrollable. you can write code as bellow:

               excute("UISELECTOR:;"
                       "FUNCTION:1:scrollable;"
                       "FUNCTION_ARGS:boolean:true;")
               excute("UISCROLLABLE:;"
                       "FUNCTION:2:getChildByText;"
                       "FUNCTION_ARGS:UiSelector:[UISELECTOR:;"
                                         "FUNCTION:1:className;"
                                         "FUNCTION_ARGS:String:android.widget.TextView;];"
                       "FUNCTION_ARGS:String:Apps;"
                       )
               excute("UIOBJECT:;"
                       "FUNCTION:0:click;"
                       )
    '''
    if not can_continue():
        return
    try:
        result=get_tls_thrift_client().client_uiautomator.excute(codes)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def interact_with_user_by_single_btn(title, msg, send_to="", send_msg="", enable_ring_shake=True,wait_timeout=-1):
    '''
    interact with user by alarm, it will be displyed to prompt user.it will ring and shake to prompt use,
    if you want to send a sms to prompt,you need to write send_to and send_msg arguments.

    here's an example:
    interact_with_user_by_single_btn("Title", "message.")

    @type title: string
    @param title: the dialog title.
    @type msg: string
    @param msg: the dialog message.
    @type send_to: string
    @param send_to: the phone number that receive sms.
    @type send_msg: string
    @param send_msg: the sms message.
    @type enable_ring_shake: boolean
    @param enable_ring_shake: whether enable ring and shake.
    @type wait_timeout: int , units seconds.
    @param wait_timeout:
        wait_timeout < 0, infinite wait until user interact.
        wait_timeout >= 0, wait for wait_timeout seconds,if timeout,result
    '''
    try:
        return get_tls_thrift_client().client_qsst.interactWithUserBySingleBtn(title, msg, send_to, send_msg, enable_ring_shake,wait_timeout)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def interact_with_user_by_multi_btn(title, msg, btns, send_to="",  send_msg="", enable_ring_shake=True,wait_timeout=-1,default_result=0,IsGetTimeout=False):
    '''
    interact with user by alarm, it will be displyed to prompt user,user can press button to
    select.it will ring and shake to prompt use, if you want to send a sms to prompt,you need to write send_to and send_msg arguments.

    here's an example:
    interact_with_user_by_multi_btn("Title", "message.", ["Very Good", "Good", "Bad"], "18621614361", "Come to operate.")

    @type title: string
    @param title: the dialog title.
    @type msg: string
    @param msg: the dialog message.
    @type btns: list
    @param btns: the list of button text.
    @type send_to: string
    @param send_to: the phone number that receive sms.
    @type send_msg: string
    @param send_msg: the sms message.
    @type enable_ring_shake: boolean
    @param enable_ring_shake: whether enable ring and shake.
    @type wait_timeout: int , units seconds.
    @param wait_timeout:
        wait_timeout < 0, infinite wait until user interact.
        wait_timeout >= 0, wait for wait_timeout seconds,if timeout,result default index

    @return: the index of btns
    '''
    try:
        index_btns =  get_tls_thrift_client().client_qsst.interactWithUserByMultiBtn(title, msg, btns, send_to, send_msg, enable_ring_shake,wait_timeout,default_result)
        if index_btns >= 10000:
            IsTimeout = True
            index_btns = index_btns - 10000
            log_test_framework(_LOG_TAG,' interactWithUserByMultiBtn is timeout , timeout result is ' +  str(index_btns))
            # should be NameError: global name 'qsst_log_path' is not defined...
            #qsst_log_msg('interactWithUserByList is timeout')
        else:
            IsTimeout = False
            log_test_framework(_LOG_TAG,' interactWithUserByMultiBtn is NOT timeout , USER input is ' + str(index_btns))
        if IsGetTimeout :
                return ( IsTimeout, index_btns )
        else:
            return index_btns

    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def interact_with_user_by_list(title, msg, list, send_to="",  send_msg="", enable_ring_shake=True,wait_timeout=-1,default_result=0,IsGetTimeout = False):
    '''
    interact with user by alarm, it will be displyed to prompt user,user can select item from list.
    it will ring and shake to prompt use, if you want to send a sms to prompt,you need to write send_to and send_msg arguments.

    here's an example:
    interact_with_user_by_list("Title", "message.", ["Very Good", "Good", "Bad", "Very Bad], "18621614361", "Come to operate.")

    @type title: string
    @param title: the dialog title.
    @type msg: string
    @param msg: the dialog message.
    @type list: list
    @param list: the list of item text.
    @type send_to: string
    @param send_to: the phone number that receive sms.
    @type send_msg: string
    @param send_msg: the sms message.
    @type enable_ring_shake: boolean
    @param enable_ring_shake: whether enable ring and shake.
    @type wait_timeout: int , units seconds.
    @param wait_timeout:
        wait_timeout < 0, infinite wait until user interact.
        wait_timeout >= 0, wait for wait_timeout seconds,if timeout,result default index

    @return: the index of list
    '''
    try:
        index_of_list = get_tls_thrift_client().client_qsst.interactWithUserByList(title, msg, list, send_to, send_msg, enable_ring_shake,wait_timeout,default_result)
        if index_of_list >= 10000:
            IsTimeout = True
            index_of_list = index_of_list - 10000
            log_test_framework(_LOG_TAG,' interactWithUserByList is timeout , timeout result is ' + str(index_of_list) )
            # should be NameError: global name 'qsst_log_path' is not defined...
            #qsst_log_msg('interactWithUserByList is timeout')
        else:
            IsTimeout = False
            log_test_framework(_LOG_TAG,' interactWithUserByList is NOT timeout , USER input is ' + str(index_of_list) )
        if IsGetTimeout :
                return ( IsTimeout, index_of_list )
        else:
            return index_of_list

    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def send_value_to_qsst(name,value):
    '''
    send some value to qsst service. such as current suit name ,case name ,ect.

    @type name: string
    @param name: name of the key.
    @type value: string
    @param value: the value of name.
    '''

    try:
        get_tls_thrift_client().client_qsst.get_value_from_client(str(name), str(value))
    except Thrift.TException, tx:
        deal_remote_exception(tx)

def get_bluetooth_name():
    try:
        bluetoothName = get_tls_thrift_client().client_qsst.getBluetoothName()
        return bluetoothName
    except Thrift.TException, tx:
        deal_remote_exception(tx)

def get_serial_number():
    '''
    generate a serial number for a phone, used as the unique identifier in the group test.
    It is a number combined by current time and a random number

    @return: a serial number string.

    '''
    serialNum = read_serial_number_from_file()
    if(serialNum == None):
        currentTime = time.time()
        randomNumber = random.random()
        serialNum = str(currentTime)+'_'+str(randomNumber)
        if(write_serial_number_to_file(serialNum)==False):
            serialNum = None
    return serialNum

def read_serial_number_from_file():
    '''
    read the serial number from a file stored under the settings directory.

    @return: a serial number string.

    '''
    osInfo = get_platform_info()
    currLocation = os.getcwd()
    if(osInfo == 'Linux-Phone' or osInfo == 'Linux-PC'):
        serialNumberFile  = currLocation +  '/settings/'+GROUP_SERIAL_NUMBER_FILE_NAME
    elif(osInfo == 'Windows'):
        serialNumberFile  = currLocation + '\\settings\\'+GROUP_SERIAL_NUMBER_FILE_NAME
    try:
        fileInput = open(serialNumberFile, 'r')
        serialNum = fileInput.readline()
        fileInput.close()
    except Exception,e:
        serialNum = None
    return serialNum

def write_serial_number_to_file(serialNum):
    '''
    store the serial number from a file stored under the settings directory.

    @type serialNum: string
    @param serialNum: the serial number to be stored.

    @return: a serial number string.

    '''
    if(serialNum == None):
        return False
    osInfo = get_platform_info()
    currLocation = os.getcwd()
    if(osInfo == 'Linux-Phone' or osInfo == 'Linux-PC'):
        serialNumberFile  = currLocation +  '/settings/'+GROUP_SERIAL_NUMBER_FILE_NAME
    elif(osInfo == 'Windows'):
        serialNumberFile  = currLocation + '\\settings\\'+GROUP_SERIAL_NUMBER_FILE_NAME
    try:
        if(os.path.exists(serialNumberFile)):
            os.remove(serialNumberFile)
        fileOutput = open(serialNumberFile, 'w')
        fileOutput.write(serialNum)
        fileOutput.close()
    except Exception,e:
        return False
    return True

def init_group_database():
    '''
    init the database and tables used in group test. If they are already initialized, nothing happens.

    '''
    try:
        result = execute_update_sql('CREATE DATABASE IF NOT EXISTS '+GOURP_DATABASE_NAME)

        createGroupsTableSql = 'CREATE TABLE IF NOT EXISTS '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' ('+ACT_AS_HOST_KEY+' varchar(255) default \' \', '+ \
        SLOT1_PHONE_NUMBER_KEY+' varchar(255) default \' \', '+ \
        SLOT2_PHONE_NUMBER_KEY+' varchar(255) default \' \', '+ \
        GROUP_NAME_KEY+' varchar(255) default \' \', '+ \
        DEVICE_NAME_KEY+' varchar(255) not null primary key, '+ \
        ROLE_NAME_KEY+' varchar(255) default \' \', '+ \
        STATUS_KEY+' varchar(255) default \' \', ' + \
        TEST_RESULT_KEY+' varchar(255) default \' \'' +')'
        log_test_framework(_LOG_TAG,'init_group_database Groups sql:'+createGroupsTableSql)
        result = execute_update_sql(createGroupsTableSql)

        createActionTableSql = 'CREATE TABLE IF NOT EXISTS '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+ \
        ' ('+ ACTION_ID_KEY+' int not null auto_increment primary key, '+\
        ACTION_KEY+' varchar(255) default \' \', '+ \
        DEVICE_NAME_KEY+' varchar(255) default \' \'' +')'
        result = execute_update_sql(createActionTableSql)
        log_test_framework(_LOG_TAG,'init_group_database actions sql:'+createActionTableSql)
    except AssertFailedException, tx:
        current_case_continue_flag = False
        print str(tx)

def attend_group(deviceInformation):
    '''
    a device attend the group test.

    @type deviceInformation: dict
    @param deviceInformation: a dictionary contains information of a device.

    '''
    try:
        check_device_information(deviceInformation)
        if(cmp(deviceInformation[ACT_AS_HOST_KEY],'True')==0):
            destroy_group(deviceInformation[GROUP_NAME_KEY])
        else:
            #deliver an register action and wait host to cosume it. If the action is consumed by host, it means host is
            #alive,and slave can attend this group
            deliver_action(GROUP_REGISTER_ACTION+deviceInformation[GROUP_NAME_KEY],deviceInformation[DEVICE_NAME_KEY])
            wait_for_action_consumed(GROUP_REGISTER_ACTION+deviceInformation[GROUP_NAME_KEY],deviceInformation[DEVICE_NAME_KEY])
        #(DEVICE_NAME_KEY,SLOT1_PHONE_NUMBER_KEY,ACT_AS_HOST_KEY,ROLE_NAME_KEY,GROUP_NAME_KEY,STATUS_KEY,TEST_RESULT_KEY)
        sqlFormat = 'insert into %s.%s (%s,%s,%s,%s,%s,%s,%s,%s) values (%s,%s,%s,%s,%s,%s,%s,%s)  ON DUPLICATE KEY UPDATE \
        %s=%s,%s=%s,%s=%s,%s=%s,%s=%s,%s=%s,%s=%s'
        values = (GOURP_DATABASE_NAME,GOURPS_TABLE_NAME,\
                  DEVICE_NAME_KEY,SLOT1_PHONE_NUMBER_KEY,SLOT2_PHONE_NUMBER_KEY,ACT_AS_HOST_KEY,ROLE_NAME_KEY,GROUP_NAME_KEY,STATUS_KEY,TEST_RESULT_KEY,\
                  "\'"+deviceInformation[DEVICE_NAME_KEY]+"\'",\
                  "\'"+deviceInformation[SLOT1_PHONE_NUMBER_KEY]+"\'",\
                  "\'"+deviceInformation[SLOT2_PHONE_NUMBER_KEY]+"\'",\
                  "\'"+deviceInformation[ACT_AS_HOST_KEY]+"\'",\
                  "\'"+deviceInformation[ROLE_NAME_KEY]+"\'",\
                  "\'"+deviceInformation[GROUP_NAME_KEY]+"\'",\
                  "\'"+STATUS_INITIALIZED_VALUE+"\'",\
                  "\'"+RESULT_FAILURE_VALUE+"\'",\
                  SLOT1_PHONE_NUMBER_KEY,"\'"+deviceInformation[SLOT1_PHONE_NUMBER_KEY]+"\'",\
                  SLOT2_PHONE_NUMBER_KEY,"\'"+deviceInformation[SLOT2_PHONE_NUMBER_KEY]+"\'",\
                  ACT_AS_HOST_KEY,"\'"+deviceInformation[ACT_AS_HOST_KEY]+"\'",\
                  ROLE_NAME_KEY,"\'"+deviceInformation[ROLE_NAME_KEY]+"\'",\
                  GROUP_NAME_KEY,"\'"+deviceInformation[GROUP_NAME_KEY]+"\'",\
                  STATUS_KEY,"\'"+STATUS_INITIALIZED_VALUE+"\'",\
                  TEST_RESULT_KEY,"\'"+RESULT_FAILURE_VALUE+"\'")
        sql = sqlFormat%values
        log_test_framework(_LOG_TAG,'attend_group sql:'+sql)
        result = execute_update_sql(sql)
        log_test_framework(_LOG_TAG,'attend_group result:'+str(result))
        #clean all actions of this device before start a group test
        clean_actions_by_device(deviceInformation[DEVICE_NAME_KEY])
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def check_device_information(deviceInformation):
    if(ACT_AS_HOST_KEY not in deviceInformation.keys()):
        deviceInformation[ACT_AS_HOST_KEY] = 'False'
    if(DEVICE_NAME_KEY not in deviceInformation.keys()):
        deviceInformation[DEVICE_NAME_KEY] = ' '
    if(SLOT1_PHONE_NUMBER_KEY not in deviceInformation.keys()):
        deviceInformation[SLOT1_PHONE_NUMBER_KEY] = ' '
    if(SLOT2_PHONE_NUMBER_KEY not in deviceInformation.keys()):
        deviceInformation[SLOT2_PHONE_NUMBER_KEY] = ' '
    if(ACT_AS_HOST_KEY not in deviceInformation.keys()):
        deviceInformation[ACT_AS_HOST_KEY] = ' '
    if(ROLE_NAME_KEY not in deviceInformation.keys()):
        deviceInformation[ROLE_NAME_KEY] = ' '
    if(GROUP_NAME_KEY not in deviceInformation.keys()):
        deviceInformation[GROUP_NAME_KEY] = ' '

def get_group_members(groupName):
    '''
    get group members by the group name.

    @type groupName: string
    @param groupName: the name of a group.

    @return: a dict containing device information of group members.

    '''
    try:
        sql = 'SELECT * FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        result = execute_sql(sql)
        members = result.result
        log_test_framework(_LOG_TAG,'get_group_members sql:'+sql)
        return members
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_group_members_count(groupName):
    '''
    get the amount of group members by the group name.

    @type groupName: string
    @param groupName: the name of a group.

    @return: the amount of group members(integer).

    '''
    try:
        sql = 'SELECT count(*) FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        queryResult = execute_sql(sql)
        log_test_framework(_LOG_TAG,'get_group_members_count sql:'+sql)
        element = queryResult.result[0]
        result = element['count(*)']
        log_test_framework(_LOG_TAG,'get_group_members_count element:'+str(element)+"  "+str(result))
        return int(result)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_group_members(expectedMemberCount, groupName, isHost=True, retryParam = None):
    '''
    wait for the amount of group members to reach a pre-set number.

    @type expectedMemberCount: int
    @param expectedMemberCount: expected amount of the members in a group.
    @type groupName: string
    @param groupName: the name of a group.
    @type isHost: boolean
    @param isHost: whether the curren device is host.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the amount of members that have already attended the group(integer).

    '''
    try:
        retry = retryParam
        count = 0
        while((retry == None) or (retry != 0)):
            if(isHost):
                clean_actions_by_name(GROUP_REGISTER_ACTION+groupName)
            count = get_group_members_count(groupName)
            if(count == expectedMemberCount):
                return count
            sleep(5)
            if(retry != None):
                retry = retry - 1
        return count
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def leave_group(deviceInformation):
    '''
    device can use this API to leave a group which will delete the record in database.

    @type deviceInformation: dict
    @param deviceInformation: a dictionary contains information of a device.

    '''
    try:
        sql = 'DELETE FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceInformation[DEVICE_NAME_KEY]+"\'"
        log_test_framework(_LOG_TAG,'leave_group sql:'+sql)
        execute_update_sql(sql)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_group_destroyed(groupName, retryParam = None):
    '''
    wait for group to be destroyed by host.

    @type groupName: string
    @param groupName: the name of a group.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the amount of members that have already attended the group(integer).
    '''
    try:
        retry = retryParam
        count = 0
        while((retry == None) or (retry != 0)):
            count = get_group_members_count(groupName)
            if(count == 0):
                return count
            sleep(5)
            if(retry != None):
                retry = retry - 1
        return count
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def destroy_group(groupName):
    '''
    destroy a group by the group name.

    @type groupName: string
    @param groupName: the name of a group.

    '''
    try:
        sql = 'DELETE FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        log_test_framework(_LOG_TAG,'destroy_group sql:'+sql)
        execute_update_sql(sql)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def set_role_name(deviceName,roleName):
    '''
    set the role name of a device.

    @type deviceName: string
    @param deviceName: the name of a device, it is generated with the API get_serial_number.
    @type roleName: string
    @param roleName: the role name of a device, it is used to control the logic of a device in group test.

    '''
    try:
        sql = 'UPDATE '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' SET '+ \
        ROLE_NAME_KEY+'='+"\'"+roleName+"\'"\
        ' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        log_test_framework(_LOG_TAG,'set_role_name sql:'+sql)
        execute_update_sql(sql)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_role_name(deviceName):
    '''
    get the role name of a device.

    @type deviceName: string
    @param deviceName: the name of a device, it is generated with the API get_serial_number.
    @return: the role name of a device, it is used to control the logic of a device in group test.

    '''
    try:
        sql = 'SELECT '+ ROLE_NAME_KEY+' FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        log_test_framework(_LOG_TAG,'get_role_name sql:'+sql)
        result = execute_sql(sql)
        element = result.result[0]
        roleName = element[ROLE_NAME_KEY]
        return roleName
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_slot1_number_by_role_name(roleName,groupName):
    '''
    get the slot 1 phone number of a device stored in the database.

    @type roleName: string
    @param roleName: the role name of a device.
    @type groupName: string
    @param groupName: the group name of a device.
    @return: the slot 1 phone number of the device identified by the roleName and groupName.

    '''
    try:
        sql = 'SELECT '+ SLOT1_PHONE_NUMBER_KEY+' FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+ROLE_NAME_KEY+'='+"\'"+roleName+"\'" \
               + ' AND '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        log_test_framework(_LOG_TAG,'get_slot1_number_by_role_name sql:'+sql)
        result = execute_sql(sql)
        element = result.result[0]
        phoneNumber = element[SLOT1_PHONE_NUMBER_KEY]
        return phoneNumber
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_role_name(deviceName,retryParam = None):
    '''
    wait for host to assign a role name.

    @type deviceName: string
    @param deviceName: the name of a device, it is generated with the API get_serial_number.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the role name assigned by host,defult is ' ', means no role name is assigned.
    '''
    try:
        retry = retryParam
        roleName = ' '
        while((retry == None) or (retry != 0)):
            roleName = get_role_name(deviceName)
            if(cmp(roleName,' ')==0):
                sleep(5)
            else:
                return roleName
            if(retry != None):
                retry = retry - 1
        return roleName
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_device_name_by_role_and_group_name(roleName,groupName):
    '''
    query the name of a device stored in the database by roleName and groupName.

    @type roleName: string
    @param roleName: the role name of a device.
    @type groupName: string
    @param groupName: the group name of a device.
    @return: the device name stored in the database.

    '''
    try:
        sql = 'SELECT '+ DEVICE_NAME_KEY+' FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+ROLE_NAME_KEY+'='+"\'"+roleName+"\'" \
               + ' AND '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        log_test_framework(_LOG_TAG,'get_device_name_by_role_and_group_name sql:'+sql)
        result = execute_sql(sql)
        element = result.result[0]
        deviceName = element[DEVICE_NAME_KEY]
        return deviceName
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def deliver_action_by_role_name(action,roleName,groupName):
    '''
    deliver an action to a device specified by roleName and groupName.

    @type action: string
    @param action: the action to be delivered.
    @type roleName: string
    @param roleName: the role name of a device.
    @type groupName: string
    @param groupName: the group name of a device.

    '''
    try:
        deviceName = get_device_name_by_role_and_group_name(roleName,groupName)
        result = deliver_action(action,deviceName)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def deliver_action(action,deviceName):
    '''
    deliver an action to a device specified by deviceName.

    @type action: string
    @param action: the action to be delivered.
    @type deviceName: string
    @param deviceName: the name of a device.

    '''
    try:
        sql = 'INSERT INTO '+ GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' ('+ \
        ACTION_KEY+','+DEVICE_NAME_KEY+') '+ \
        'VALUES'+' ('+"\'"+action+"\'"+','+"\'"+deviceName+"\'"+') '
        log_test_framework(_LOG_TAG,'deliver_action sql:'+sql)
        result = execute_update_sql(sql)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_action_count(deviceName):
    '''
    query the amount of actions deliver to a device.

    @type deviceName: string
    @param deviceName: the name of a device.
    @return: the amount of actions(int)

    '''
    try:
        sql = 'SELECT count(*) FROM '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        queryResult = execute_sql(sql)
        log_test_framework(_LOG_TAG,'get_action_count sql:'+sql)
        element = queryResult.result[0]
        result = element['count(*)']
        return int(result)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_amount_by_action_and_device(actionName, deviceName):
    '''
    query the amount of actions deliver to a device by action name.

    @type actionName: string
    @param actionName: the name of a action.
    @type deviceName: string
    @param deviceName: the name of a device.
    @return: the amount of actions(int)

    '''
    try:
        sql = 'SELECT count(*) FROM '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'" \
        + ' AND '+ACTION_KEY+'='+"\'"+actionName+"\'"
        queryResult = execute_sql(sql)
        log_test_framework(_LOG_TAG,'get_amount_by_action_and_device sql:'+sql)
        element = queryResult.result[0]
        result = element['count(*)']
        return int(result)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def consume_one_action(deviceName):
    '''
    consume an action deliver to the device.

    @type deviceName: string
    @param deviceName: the name of a device.
    @return: the action(string)

    '''
    try:
        sql = 'SELECT * FROM '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        result = execute_sql(sql)
        log_test_framework(_LOG_TAG,'consume_one_action sql:'+sql)
        element = result.result[0]
        action = element[ACTION_KEY]
        actionID = element[ACTION_ID_KEY]
        deleteActionSql = 'DELETE FROM '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' WHERE '+ACTION_ID_KEY+'='+str(actionID)
        result = execute_update_sql(deleteActionSql)
        log_test_framework(_LOG_TAG,'consume_one_action sql:'+deleteActionSql)
        return action
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def clean_actions_by_name(actionName):
    '''
    clear all actions spcecified by the action name.

    @type actionName: string
    @param actionName: the name of a action.

    '''
    try:
        deleteActionsSql = 'DELETE FROM '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' WHERE '+ACTION_KEY+'='+"\'"+actionName+"\'"
        result = execute_update_sql(deleteActionsSql)
        log_test_framework(_LOG_TAG,'clean_actions_by_name sql:'+deleteActionsSql)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def clean_actions_by_device(deviceName):
    '''
    clear all actions delivered to a device.

    @type deviceName: string
    @param deviceName: the name of a device.

    '''
    try:
        deleteActionsSql = 'DELETE FROM '+GOURP_DATABASE_NAME+'.'+ACTIONS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        result = execute_update_sql(deleteActionsSql)
        log_test_framework(_LOG_TAG,'clean_actions_by_device sql:'+deleteActionsSql)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_action(deviceName,retryParam = None):
    '''
    device use this API to wait until an action to come.

    @type deviceName: string
    @param deviceName: the name of a device.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the amount of actions delivered to this device(integer).
    '''
    try:
        retry = retryParam
        count = 0
        while((retry == None) or (retry != 0)):
            count = get_action_count(deviceName)
            if(count > 0):
                return count
            sleep(5)
            if(retry != None):
                retry = retry - 1
        return count
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_action_consumed(actionName, deviceName,retryParam = None):
    '''
    device use this API to wait until an action to be consumed.

    @type actionName: string
    @param actionName: the name of an action.
    @type deviceName: string
    @param deviceName: the name of a device.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the amount of actions with the name of actionName delivered to this device(integer).
    '''
    try:
        retry = retryParam
        count = 0
        while((retry == None) or (retry != 0)):
            count = get_amount_by_action_and_device(actionName,deviceName)
            if(count == 0):
                return count
            sleep(5)
            if(retry != None):
                retry = retry - 1
        return count
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def set_status(status, deviceName):
    '''
    set the status of a device.

    @type status: string
    @param status: status of a device,there are three different statuses:STATUS_INITIALIZED_VALUE,STATUS_READY_VALUE,STATUS_FINISHED_VALUE.
    @type deviceName: string
    @param deviceName: the name of a device.

    '''
    try:
        sql = 'UPDATE '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' SET '+ \
        STATUS_KEY+'='+"\'"+status+"\'"\
        ' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        log_test_framework(_LOG_TAG,'set_status sql:'+sql)
        execute_update_sql(sql)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_status(deviceName):
    '''
    get the status of a device.

    @type deviceName: string
    @param deviceName: the name of a device.
    @return: status of a device,there are three different statuses:STATUS_INITIALIZED_VALUE,STATUS_READY_VALUE,STATUS_FINISHED_VALUE

    '''
    try:
        sql = 'SELECT '+ STATUS_KEY+' FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        log_test_framework(_LOG_TAG,'get_status sql:'+sql)
        result = execute_sql(sql)
        element = result.result[0]
        status = element[STATUS_KEY]
        return status
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_test_result_by_role_name(roleName,groupName):
    '''
    get the test result of a device by role name and group name.

    @type roleName: string
    @param roleName: the role name of a device.
    @type groupName: string
    @param groupName: the group name of a device.
    @return: the test result(string)

    '''
    try:
        sql = 'SELECT '+ TEST_RESULT_KEY+' FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+ROLE_NAME_KEY+'='+"\'"+roleName+"\'" \
               + ' AND '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        log_test_framework(_LOG_TAG,'get_test_result_by_role_name sql:'+sql)
        result = execute_sql(sql)
        element = result.result[0]
        result = element[TEST_RESULT_KEY]
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def set_test_result(result, deviceName):
    '''
    set the test result of a device

    @type result: string
    @param result: the test result.
    @type deviceName: string
    @param deviceName: the name of a device.

    '''
    try:
        sql = 'UPDATE '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' SET '+ \
        TEST_RESULT_KEY+'='+"\'"+result+"\'"\
        ' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        log_test_framework(_LOG_TAG,'set_test_result sql:'+sql)
        execute_update_sql(sql)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_test_result(deviceName):
    '''
    get the test result of a device.

    @type deviceName: string
    @param deviceName: the name of a device.
    @return: the test result(string)

    '''
    try:
        sql = 'SELECT '+ TEST_RESULT_KEY+' FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+DEVICE_NAME_KEY+'='+"\'"+deviceName+"\'"
        log_test_framework(_LOG_TAG,'get_test_result sql:'+sql)
        result = execute_sql(sql)
        element = result.result[0]
        result = element[TEST_RESULT_KEY]
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_finished_members_count(groupName):
    '''
    get the amount of devices which status is STATUS_FINISHED_VALUE.

    @type groupName: string
    @param groupName: the name of a group.
    @return: amount of finished status devices

    '''
    try:
        sql = 'SELECT count(*) FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+ \
        STATUS_KEY+'='+"\'"+STATUS_FINISHED_VALUE+"\'" +\
        ' AND '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        result = execute_sql(sql)
        log_test_framework(_LOG_TAG,'get_finished_members_count sql:'+sql)
        element = result.result[0]
        count = element['count(*)']
        return int(count)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def get_ready_members_count(groupName):
    '''
    get the amount of devices which status is STATUS_READY_VALUE.

    @type groupName: string
    @param groupName: the name of a group.
    @return: amount of ready status devices

    '''
    try:
        sql = 'SELECT count(*) FROM '+GOURP_DATABASE_NAME+'.'+GOURPS_TABLE_NAME+' WHERE '+ \
        STATUS_KEY+'='+"\'"+STATUS_READY_VALUE+"\'" +\
        ' AND '+GROUP_NAME_KEY+'='+"\'"+groupName+"\'"
        result = execute_sql(sql)
        log_test_framework(_LOG_TAG,'get_ready_members_count sql:'+sql)
        element = result.result[0]
        count = element['count(*)']
        return int(count)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_members_finished(expectedMemberCount,groupName,retryParam = None):
    '''
    wait for members of a group to get the finished status.

    @type expectedMemberCount: int
    @param expectedMemberCount: the expected member amount of a group.
    @type groupName: string
    @param groupName: the name of a group.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the amount of devices in finished status(integer).
    '''
    try:
        retry = retryParam
        count = 0
        while((retry == None) or (retry != 0)):
            count = get_finished_members_count(groupName)
            if(count == expectedMemberCount):
                return count
            sleep(5)
            if(retry != None):
                retry = retry - 1
        return count
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def wait_for_members_ready(expectedMemberCount,groupName,retryParam = None):
    '''
    wait for members of a group to get the ready status.

    @type expectedMemberCount: int
    @param expectedMemberCount: the expected member amount of a group.
    @type groupName: string
    @param groupName: the name of a group.
    @type retryParam: int
    @param retryParam: retry times of the wait option, default is None,and will wait forever.

    @return: the amount of devices in ready status(integer).
    '''
    try:
        retry = retryParam
        count = 0
        while((retry == None) or (retry != 0)):
            count = get_ready_members_count(groupName)
            if(count == expectedMemberCount):
                return count
            sleep(5)
            if(retry != None):
                retry = retry - 1
        return count
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def execute_sql(sql):
    '''
    execute a sql to query the database.

    @type sql: string
    @param sql: the sql to be executed.
    @return: a int number returned by database

    '''
    try:
        result = utility_wrapper.client_grouptest.databaseExecuteQuery(sql)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

def execute_update_sql(sql):
    '''
    execute a sql to update the database.

    @type sql: string
    @param sql: the sql to be executed.
    @return: a int number returned by database

    '''
    try:
        result = utility_wrapper.client_grouptest.databaseExecuteUpdate(sql)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def disable_watcher_anr_fc():
    '''
        disable watcher ANR and FC, when need click some views that can not click in monkey test scenario.
    '''
    try:
        result=get_tls_thrift_client().client_qsst.disable_watcher_anr_fc(True)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def enable_watcher_anr_fc():
    '''
        enable watcher ANR and FC.
    '''
    try:
        result=get_tls_thrift_client().client_qsst.disable_watcher_anr_fc(False)
        return result
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def init_server_side_log():
    '''
    init server side log system.
    '''
    try:
        utility_wrapper.client_grouptest.initLog()
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def mkdir_on_server_side(dir):
    '''
    clear server's log. it's used for fetching adblog at server side.
    '''
    try:
        utility_wrapper.client_grouptest.mkdir(dir)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def clear_adb_log():
    '''
    clear server's log. it's used for fetching adblog at server side.
    '''
    try:
        utility_wrapper.client_grouptest.clearAdbLog()
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def start_capture_adblog(cmd):
    '''
    start capture adblog at server side. the adblog will be cleard automatic before captureing adblog.
    normally, it's called at the beginnig of a case.

    @type cmd: string
    @param cmd: adb command.
    @return: the pid of adb process

    here is an example:
    start_capture_adblog("adb logcat -v time > E:\\adb.log")
    the adblog will be saved in E:\adb.log, the file is in server side.

    '''
    try:
        result = utility_wrapper.client_grouptest.startCaptureAdbLog(cmd)
        return result
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def stop_capture_adblog(pid):
    '''
    stop capture adblog, the api will send a signal to server to stop capture adblog.
    normally, it's called at the end of a case.

    @type pid: string
    @param pid: the adb process pid

    '''
    try:
        utility_wrapper.client_grouptest.stopCaptureAdbLog(pid)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def load_configuration(file):
    '''
    load QXDM configuration file.
    note: the file is server side file.

    @type file: string
    @param file: the QXDM cofiguration file.
    @return: whether load configuration sccussed.
    '''
    try:
        return utility_wrapper.client_grouptest.loadConfiguration(file)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def comPort(port):
    '''
    let phone to connect to QXDM.

    @type port: string
    @param file: COM port.
    @return: whether connect the port successed.
    '''
    try:
        return utility_wrapper.client_grouptest.comPort(port)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def clear_view_items():
    '''
    clear view items in QXDM.

    @return: whether clear view tiems successed.
    '''
    try:
        return utility_wrapper.client_grouptest.clearViewItems()
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def save_item_store(path):
    '''
    save the item of QXDM

    @type path: string
    @param path: the path of .isf file
    @return: whether save item successed.

    here is an example:
    save_item_store("E:\\")
    the isf file will be saved in E:\ of server side.
    the isf file's name will be specfied by QXDM.
    '''
    try:
        return utility_wrapper.client_grouptest.saveItemStore(path)
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def quit_qxdm():
    '''
    quit QXDM

    @return: whether quit qxdm successed.
    '''
    try:
        return utility_wrapper.client_grouptest.quitQXDM()
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def get_serial_number_from_pc():
    '''
    get serial number.

    @return: the device serial number when device connected PC.
    @note: the hoststub must be running first. the serial number is fetched from hoststub.
    '''
    try:
        return utility_wrapper.client_grouptest.getSerialNumber()
    except Thrift.TException, tx:
        current_case_continue_flag = False
        raise AssertFailedException(tx)

@api_log_decorator
def get_ftp_upload_info(localFileName, remoteDir):
    '''
    get upload throuthput info of FTP.

    @type localFilePath: string
    @param localFilePath: the absolute path of local file that will be uploaded
    @type remoteDir: string
    @param remoteDir: remote directory for placing the uploaded file in the FTP server
    '''
    try:
        import settings.common as SC
        ftpUrl = SC.PRIVATE_FTP_HOSTNAME
        ftpPort = SC.PRIVATE_FTP_PORT
        username = SC.PRIVATE_FTP_USERNAME
        password = SC.PRIVATE_FTP_PASSWORD
        isActive = SC.PRIVATE_FTP_ISACTIVE

        operation = FTP_OP_UPLOAD
        results_dict = {'result':''}
        upload_results =  get_tls_thrift_client().client_qsst.get_ftp_tp_info(ftpUrl, int(ftpPort), username, password, localFileName, remoteDir, operation, isActive)
        if upload_results in ftp_invalid_info:
            results_dict['result'] = OP_FAILED
            results_dict['info'] = ftp_invalid_info[upload_results]
            return results_dict

        results_dict['result'] = OP_SUCCEED
        results_dict['info'] = get_dict_from_results(upload_results)
        return results_dict

    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_ftp_download_info(remoteFilePath, localFileName):
    '''
    get download throuthput info of FTP.

    @type remoteFilePath: string
    @param filePath: path of remote file in the FTP server that will be downloaded
    @type localDir: string
    @param localDir: local directory for placing the downloaded file.
    '''
    try:
        import settings.common as SC
        ftpUrl = SC.PRIVATE_FTP_HOSTNAME
        ftpPort = SC.PRIVATE_FTP_PORT
        username = SC.PRIVATE_FTP_USERNAME
        password = SC.PRIVATE_FTP_PASSWORD
        isActive = SC.PRIVATE_FTP_ISACTIVE

        operation = FTP_OP_DOWNLOAD
        results_dict = {'result':''}
        download_results =  get_tls_thrift_client().client_qsst.get_ftp_tp_info(ftpUrl, int(ftpPort), username, password, remoteFilePath, localFileName, operation, isActive)
        if download_results in ftp_invalid_info:
            results_dict['result'] = OP_FAILED
            results_dict['info'] = ftp_invalid_info[download_results]
            return results_dict

        results_dict['result'] = OP_SUCCEED
        results_dict['info'] = get_dict_from_results(download_results)
        return results_dict

    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def start_new_track(name, description=''):
    '''
    start an new track.
    The api only apply to local tracking.

    @type name: string
    @param name: name of track
    @type description: string
    @param description: description of track
    @return: start successfully or not.
    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return False;

    try:
        if not SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            return get_tls_thrift_client().client_mytrackservice.start_new_track(str(name), str(description))
    except Thrift.TException, tx:
        deal_remote_exception(tx)

    return False;

@api_log_decorator
def pause_current_track():
    '''
    pause current track.
    The api only apply to local tracking.

    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return

    try:
        if not SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            get_tls_thrift_client().client_mytrackservice.pause_current_track()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def end_current_track():
    '''
    end current track.
    The api only apply to local tracking.

    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return

    try:
        if not SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            get_tls_thrift_client().client_mytrackservice.end_current_track()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def end_current_track_and_export_kml(path):
    '''
    end current track and export the track as KML in some location.
    The api only apply to local tracking.

    @type path: string
    @param path: the kml path when local recording track.

    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return

    try:
        if not SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            get_tls_thrift_client().client_mytrackservice.end_current_track_and_export_kml()
            #move kml file to log directory.
            sleep(2)
            osInfo = get_platform_info()
            kml_temp_path = "/sdcard/MyTracks/kml/" + get_timestring_log_name() + ".kml";
            if(osInfo == 'Linux-Phone'):
                cmd = "mv " + kml_temp_path + " " + path
            elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
                cmd= 'adb pull '+ kml_temp_path + " " + path[0:len(path)-1]
            log_test_framework("case_utility","cmd : " + cmd)
            os.system(cmd)
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def resume_current_track():
    '''
    resume the current track maybe paused.
    The api only apply to local tracking.

    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return

    try:
        if not SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            get_tls_thrift_client().client_mytrackservice.resume_current_track()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def insert_waypoint(name, description='', category=''):
    '''
    insert a waypoint in track.

    @type name: string
    @param name: name of waypoint
    @type description: string
    @param description: description of waypoint
    @type category: string
    @param category: category of waypoint
    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return

    try:
        if SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            serialNumber = get_serial_number()
            utility_wrapper.client_grouptest.insertWaypoint(str(name), str(description), str(category), str(serialNumber))
        else:
            get_tls_thrift_client().client_mytrackservice.insert_waypoint(str(name), str(description), str(category))
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def get_recording_track_id():
    '''
    get recording track id

    @return: recording track id
    '''
    import settings.common as SC
    if not SC.PRIVATE_TRACKING_TRACKING_PATH:
        return

    try:
        if SC.PRIVATE_TRACKING_TRACKING_IN_CLOUD:
            return utility_wrapper.client_grouptest.get_recording_track_id()
        else:
            return get_tls_thrift_client().client_mytrackservice.get_recording_track_id()
    except Thrift.TException, tx:
        deal_remote_exception(tx)

@api_log_decorator
def invokeHostCmd(cmdFilePath, params=""):
    '''
    invoke command int the Host-stub side.

    @type cmdFilePath: string
    @param path: the path of .isf file
    @type params: string, more params should be separated by space.
    @param params: params of cmdFilePath
    @return: if failed return -1, else return other value based on cmdFile or command.

    here are two examples:
    Without params: invokeHostCmd("E:\\test.bat")
    With params: invokeHostCmd("E:\\test.bat", "param1 param2 param3")

    '''
    try:
        return utility_wrapper.client_grouptest.invokeHostCmd(cmdFilePath, params)
    except Thrift.TException, tx:
        deal_remote_exception(tx)
        

'''
    @attention: modify by huitingn@qti.qualcomm.com
'''
def repeat_cmcc_devci(funcName,iterationNum=3):
    results = []
    for i in range(iterationNum):
        print_log_line('This is iteration %d'%(i+1))
        func = funcName()
        results.append(str(func))
        #print type(func)
        #print type(str(func))
        
    #a = ("True "*iterationNum).split(" ")[:-1]
    if results==("True "*iterationNum).split(" ")[:-1]:
        case_flag = True
    else: case_flag  = False
    print results    
    return case_flag
