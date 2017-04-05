#coding=utf-8
'''


@author: huitingn
'''
from utility_wrapper import *
import fs_wrapper
from test_suit_base import TestSuitBase
from case_utility import *
from qrd_shared.case import *
import string


CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}
BOOL_STK_WIFI_CHECK = False
BOOL_STK_MOBILE_NETWORK_CHECK = False


URL_TITLE = {'百度':('www.baidu.com','百度一下'),
              '新浪':('sina.cn','手机新浪网'),
              '豌豆荚':('www.wandoujia.com','安卓手机娱乐第一入口-豌豆荚'),
              '百度视频':('m.video.baidu.com','精选_百度视频'),
              '百度音乐':('music.baidu.com','百度音乐-移动版'),
              '优酷':('www.youku.com','优酷-中国领先')}
'''
HOMEPAGE = 'Homepage'
STOP = 'Stop'
BACK = 'Back'
FORWARD = 'Forward'
'''
POSITION = {'video':(443,683),
            'music':(443,780)}


class test_suit_ui_browser(TestSuitBase):
    '''
    test_suit_browser is a class for browser suit.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    pass


def exit_cur_case(case_tag):
    '''
    goback to homescreen. exit current case.
    
    @type case_tag: string
    @param case_tag:the calling case'TAG
    
    '''
    global current_case_continue_flag
    current_case_continue_flag = True
    
    # only for browser
    func = lambda:( (is_view_enabled_by_id(VIEW_TEXT_VIEW, 'alertTitle', isScrollable=0) and not click_button_by_text('Quit')) or goback() )
    if not wait_for_fun(func,True,3):
        # only for browser
        send_key(KEY_HOME)
        #if not search_view_by_desc('Apps'):    log_test_framework(case_tag, "exit is wrong, may influence the next case")
        
def init_and_open_wifi():
    start_activity("com.android.settings", ".Settings")
    # remove for UI change in AndroidL.
    #settings.whether_open_mobile_data(False)
    WIFI_NAME = 'Hydra'
    #WIFI_PASSWORD_SEQUENCE = ['k','num_sign','5','num_sign','x','num_sign','4','8','num_sign','caps','v','caps','z','num_sign','3']
    WIFI_PASSWORD_SEQUENCE = ['caps','k','num_sign','5','num_sign','x','num_sign','4','8','num_sign','caps','v','z','num_sign','3'] # this is for 8994, screen is 1600*2416
    settings.enable_wifi(WIFI_NAME, WIFI_PASSWORD_SEQUENCE)



def rand_name(prefix = '', only_letter = False, name_length = 8):
    '''
    return a random name.
    can assign the prefix, name_length, letter&digit.
    
    @type prefix: string
    @param prefix: the string in beginning
    @type only_letter: boolean
    @param only_letter: True is only_letter, False is letter&digit
    @type name_length: number
    @param name_length: the max length of rand_name string
    '''
    if only_letter:
        char_list = list(string.ascii_letters)
    else:
        char_list = list(string.ascii_letters + '0123456789')
    n = random.randint(1,name_length - len(prefix))
    dir_name = random.sample(char_list, n)
    # e.g:dir_name = ['V', '3', 'P', 'U', 'G', '2']
    #     ''.join(dir_name) = 'V3PUG2'
    return prefix+''.join(dir_name)


def take_screenshot():
    '''take a screenshot and save to log/suit_name/case_name/'''
    make_case_log_dir()
    global osInfo
    if(osInfo == 'Linux-Phone'):
        cmd = 'screencap -p ' + get_case_logging_path() + get_file_timestring() + '.jpg'
        run_cmd(cmd)
    elif(osInfo == 'Linux-PC' or osInfo =='Windows'):
        import settings.common as SC
        run_cmd(' mkdir ' + SC.PUBLIC_LOG_PATH)
        temp_file= ' ' + SC.PUBLIC_LOG_PATH + '/temp.jpg '
        cmd= 'screencap -p ' + temp_file
        run_cmd(cmd)
        cmd= 'adb pull '+temp_file + get_case_logging_path() + get_file_timestring() + '.jpg'
        os.system(cmd)




def exit_browser():
    sleep(2)
    
    close_other_tabs(left=0)
    
    '''try:
        click_menuitem_by_text(browser.get_value('exit'))
        click_button_by_text(browser.get_value('quit'))
    except:goback()'''




def stop_page():
    try:
        scroll_to_top()
        click_imageview_by_id('stop',isScrollable=0)
    except:pass




def close_other_tabs(left=1):
    sleep(1)
    
    windowNum = get_view_text_by_id(VIEW_TEXT_VIEW, 'tab_switcher_text')
    windowNum = int(windowNum)
    
    if windowNum>left:
        click_imageview_by_id('tab_switcher')
        for i in range(windowNum-left):
            click_imageview_by_id('closetab')
        if left>0:click_imageview_by_id('tab_view') # now should be just 1 window in browser  
        

def open_browser():
    launcher.launch_from_launcher('browser')
    if search_text(browser.get_value('quit'),isScrollable=0) and search_text('Minimize',isScrollable=0):goback()
    
    stop_page()
    close_other_tabs()
    
    
def wlan_state():
    drag_by_param(50, 0, 50, 95, 2)
    drag_by_param(50, 0, 50, 95, 10)
    
    if is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Hydra', isScrollable=0):return True
    else:return False