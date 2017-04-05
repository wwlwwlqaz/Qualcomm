from test_suit_base import TestSuitBase
from case_utility import *



class test_suit_ui_launcher(TestSuitBase):
    pass

SEARCH_BY_TEXT = 0
SEARCH_BY_ID = 1
SEARCH_BY_DESC = 2
WIDGET_LIST={'Analog clock':['','analog_appwidget'],\
             'Bookmark':[],\
             'Bookmarks':[],\
             'Calendar':['','date'],\
             'CalendarWidget':['','date_view'],\
             'Cell Broadcast':['','textCB'],\
             'Contact':[],\
             'Data monitor':['','data_month'],\
             'Digital clock':['','the_clock'],\
             'Direct dial':[],\
             'Direct message':[],\
             'Email':[],\
             'Email folder':[],\
             'Home screen tips':['','bugdroid'],\
             'LED flashlight':['','LEDSwitch'],\
             'Messaging':[],\
             'Music':[],\
             'Music playlist':[],\
             'My Tracks':[],\
             'Photo Gallery':[],\
             'Power control':[],\
             'Search':['','search_plate'],\
             'Settings shortcut':['',''],\
             }

SIM_INFO_INDEX = {'My phone number':6,\
                  'Network':8,\
                  'Signal strength':10,\
                  'Mobile network type':12,\
                  'Service state':14,\
                  'Roaming':16,\
                  'IMEI':5,\
                  'IMEI SV':7,\
                  'Mobile network state':11,\
                  }
SIM_REFER_INDEX = {'My phone number':'',\
                  'Network':'',\
                  'Signal strength':'',\
                  'Mobile network type':'',\
                  'Service state':'',\
                  'Roaming':'',\
                  'IMEI':'',\
                  'IMEI SV':'',\
                  'Mobile network state':'',\
                  }

interval = 2
begin = 2
STORAGE_INFO_INDEX = {'Total space':begin,\
                      'Available':begin+interval,\
                      'Apps (app data & media content)':begin+2*interval,\
                      'Pictures, videos':begin+3*interval,\
                      'Audio (music, ringtones, podcasts, etc.)':begin+4*interval,\
                      'Downloads':begin+5*interval,\
                      'Cached data':begin+2*interval,\
                      'Misc.':begin+3*interval,\
                      }

STORAGE_REFER_INDEX = {'Total space':'',\
                      'Available':'',\
                      'Apps (app data & media content)':'',\
                      'Pictures, videos':'',\
                      'Audio (music, ringtones, podcasts, etc.)':'',\
                      'Downloads':'',\
                      'Cached data':'',\
                      'Misc.':'',\
                      }


def exit_cur_case(case_tag):
    '''
    goback to homescreen. exit current case.
    
    @type case_tag: string
    @param case_tag:the calling case'TAG
    
    '''
    global current_case_continue_flag
    current_case_continue_flag = True
    
    func = lambda:(search_view_by_desc('Apps') or goback())
    if not wait_for_fun(func,True,5):
        send_key(KEY_HOME)
        #if not search_view_by_desc('Apps'):    log_test_framework(case_tag, "exit is wrong, may influence the next case")
        
        
import re,copy
global preWorkFlag
preWorkFlag = False
def pre_work():
    tag = 'pre_work()'
    
    toolsLocation = r'C:\Public\some_software_install_package'
    command = 'adb install %s%sXAgentORB_System.apk'%(toolsLocation,os.sep)
    result = copy.copy(os.popen(command).read())
    if re.search('(?s)XAgentORB_System.apk.*(Success|ALREADY_EXISTS)',result) is None:
        log_test_case(TAG, 'adb install apk is failed')
        set_can_continue()
        return
    else:
        command = 'adb shell am startservice -n com.android.xagent.orb/.XAgentORBService'
        os.system(command)
        
        command = 'adb devices'
        result = copy.copy(os.popen(command).read())
        try:deviceID = re.search('([\d\w]*)(?=\s*device\s)',result).group(1)
        except:
            log_test_case(TAG, 'cannot get deviceID. You may need to check adb connection.')
            set_cannot_continue()
            return
    global preWorkFlag
    preWorkFlag = True
    return (toolsLocation,deviceID)
    