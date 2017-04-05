# -*- coding: utf-8 -*-  
'''

@author: huitingn
@version:

'''
from utility_wrapper import *
import fs_wrapper
from test_suit_base import TestSuitBase
from case_utility import *
import re, datetime, shlex
from qrd_shared.case import *


CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}
BOOL_STK_WIFI_CHECK = False
BOOL_STK_MOBILE_NETWORK_CHECK = False

class test_suit_ui_dev_ci(TestSuitBase):
    '''
    test_suit_ui_message is a class for browser suit.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    pass



def exit_cur_case(case_tag):
    '''
    goback to homescreen. exit current case.
    
    @type case_tag: string
    @param case_tag:the calling case'tag
    
    '''
    tag = 'exit_cur_case(%s)' % case_tag
    
    global current_case_continue_flag
    current_case_continue_flag = True
    
    log_test_framework(tag, 'start')
    func = lambda:(search_view_by_desc('Apps') or goback())
    if not wait_for_fun(func, True, 5):
        send_key(KEY_HOME)
        # if not search_view_by_desc('Apps'):    log_test_framework(case_tag, "exit is wrong, may influence the next case")





def message_num_in_thread(thread=''):
    '''
    @type thread: string
    @param thread:
    '''
    
    tag = 'message_num_in_thread()'
    log_test_framework(tag, 'start')
    # syscode = sys.getfilesystemencoding()
    
    try:drag_by_param(50, 30, 50, 80, 20)  # scroll_to_top()
    except:pass
    
    if '' == thread:
        head = get_view_text_by_id(VIEW_TEXT_VIEW, 'from', isScrollable=0).decode('utf-8')
    
    else:
        drag_by_param(50, 20, 50, 80, 10)
        thread = str(thread)
        left = '.*' + thread[0:3] + '\s?' + thread[3:7] + '\s?' + thread[7:11] + '.*'
        head = get_text(left, isScrollable=1, searchFlag=TEXT_MATCHES_REGEX)
        if head is '':
            log_test_framework(tag, 'cannot find thread = ' + thread)
            n = 0
            return (n, thread, left)  # left should be 'NULL'??


    if re.search(u'\xa0', head):
        [left, right] = head.split(u'\xa0')
        n = re.search('\d+', right).group()
        n = int(n)
    else:
        left = head
        # thread = s
        n = 1  # n = '1'
        
    thread = left.replace(u' ', u'')  # remove all space
    thread = thread.replace(u'+86', u'')
    
    
    log_test_framework(tag, 'thread = ' + thread)
    log_test_framework(tag, 'n = ' + str(n))


    # n = int(n)
    log_test_framework(tag, 'end')
    return (n, thread, left)
        




def pre_check(check_range='all'):
    tag = 'pre_check()'
    log_test_framework(tag, 'start')
    
    # mms.click_home_icon()
    if search_text('No conversations', isScrollable=0):
        log_test_framework(tag, 'no conversations to be deleted')
        set_cannot_continue()
        take_screenshot()
        
    if 'mms' == check_range:
        if not is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'attachment'):
            log_test_framework(tag, 'no thread contains attachment')
            set_cannot_continue()
    
    
    # a = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Draft', searchFlag=TEXT_CONTAINS)        
    while is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Draft', isScrollable=1, searchFlag=TEXT_CONTAINS):
        log_test_framework(tag, 'in while(Draft): still have draft in msg-box')
        click_textview_by_text('Draft', isScrollable=0, searchFlag=TEXT_CONTAINS)
        
        try:click_menuitem_by_text('Discard', isScrollable=0)
        except:
            goback()
            try:clear_edittext_by_id('embedded_text_editor', isScrollable=0)
            except:pass
            try:click_button_by_id('remove_image_button', isScrollable=0, waitForView=1)
            except:pass
            try:click_button_by_id('remove_slideshow_button', isScrollable=0)
            except:pass
            try:clear_edittext_by_id('subject', isScrollable=0)
            except:pass
            try:click_textview_by_id('recipients_editor', isScrollable=0)
            except:pass
        else:pass
        
        click_imageview_by_desc('Navigate up')
    
    
    # click_imageview_by_desc('Navigate up')
    while True:
        try:scroll_to_top()
        except:pass
        a = is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'error', isScrollable=1)
        b = search_view_by_id('error')
        if a and b is True:
            click_imageview_by_id('error', isScrollable=0)
            log_test_framework(tag, 'in while(error):still have error in some thread')
            click_imageview_by_id('delivered_indicator', waitForView=1)
            try:
                clear_edittext_by_id('embedded_text_editor')
                click_button_by_id('remove_image_button', isScrollable=0, waitForView=1)
            except:pass
            click_imageview_by_desc('Navigate up')
        else:break
        
    
    
    '''
    # turn off airplane mode
    notificationBar.drag_down()
    mode = get_view_text_by_id(VIEW_TEXT_VIEW,'subs_label',isScrollable=0)
    if is_view_enabled_by_text(VIEW_TEXT_VIEW,'Airplane Mode',isScrollable=0):
        scroll_down()
        click_textview_by_text('Airplane mode')
        goback()
    goback()
    '''
    notificationBar.airplane_mode('off')

    
    log_test_framework(tag, 'end')



def message_num_in_SIM():
    tag = 'message_num_in_SIM()'
    
    # log_test_framework(tag,'start')
    number = -1
    mms.click_home_icon()
    send_key(KEY_MENU)
    click_textview_by_text('Settings')
    click_textview_by_text('Manage SIM card messages')
    func = lambda:search_text('Text messages on SIM card', isScrollable=0)
    if wait_for_fun(func, True, 15):
        send_key(KEY_MENU)
        click_textview_by_text('SIM Capacity')
        try:
            number = re.findall('(?<=Used: )\d+(?=\nCapacity:)', get_text('Used:'))[0]
        except:
            take_screenshot()
            log_test_framework(tag, 'cannot get message number')
            set_cannot_continue()
    
    goback()
    goback()
    
    return int(number)


def timestring_in_mp():
    tag = 'timestring_in_mp()'
    
    os.system('adb logcat -c')
    log = get_logcat_string(raw_cmd='-v time')
    pattern = r'(?<=\r\n).+?'  # min match
    line = re.findall(pattern, log)[-1].decode('utf-8')
    pattern = '\d{2}-\d{2} \d{2}:\d{2}:\d{2}.'
    timeString = re.findall(pattern, line)[0]
    curTime = datetime.datetime.strptime(timeString, '%m-%d %H:%M:%S')
    # (month,day,hour,minute,second) = shlex.split(curTime.strftime('%m %d %H %M %S'))

    
def get_unread_number():
    
    unread = get_view_text_by_id(VIEW_TEXT_VIEW, 'unread_conv_count', isScrollable=0)
    if unread is '':
        return 0
        log_test_case('wxiang' ,'0')
    else:
        return int(unread)
        log_test_case('wxiang' ,str(unread))

def reply_sms():
    tag = 'reply_sms()'
    
    entertext_edittext_by_id('embedded_text_editor', 'reply sms')
    if search_view_by_id('first_send_button_sms_view'):
        click_imageview_by_id('first_send_button_sms_view')
    else:
        click_imageview_by_id('send_button_sms')
        
def reply_mms():
    tag = 'reply_mms()'
    
    entertext_edittext_by_id('embedded_text_editor', 'reply mms')
    click_textview_by_desc('Attach', isScrollable=0)
    click_textview_by_text('Capture picture', waitForView=1)
    if is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Complete action using'):
        click_button_by_text('Always')
        
    click_imageview_by_desc('Shutter', isScrollable=0, waitForView=1)
    func = lambda:is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'done_button')
    if wait_for_fun(func, True, 10):
        click_imageview_by_id('done_button', isScrollable=0, waitForView=1)
    else:
        take_screenshot()
        log_test_framework(tag, "cannot click_imageview_by_id'done_button'")
        set_cannot_continue()
    
    if can_continue():                
        if is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'first_send_button_sms_view', isScrollable=0):
            click_imageview_by_id('first_send_button_sms_view', isScrollable=0)
        elif is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'send_button_mms', isScrollable=0):
            click_imageview_by_id('send_button_mms', isScrollable=0)
        else:
            click_button_by_id('send_slideshow_button', isScrollable=0)
            
        if is_view_enabled_by_text(VIEW_BUTTON, 'OK', isScrollable=0):
            click_button_by_text('OK')
        


def forward_sms_in_thread(forwardTo, thread=''):
    tag = 'forward_sms_in_thread()'
    
    #mms.click_home_icon()
    if '' == thread:
        head = get_view_text_by_id(VIEW_TEXT_VIEW, 'from', isScrollable=0).decode('utf-8')
    
    else:
        thread = str(thread)
        left = '.*' + thread[0:3] + '\s?' + thread[3:7] + '\s?' + thread[7:11] + '.*'
        head = get_text(left, searchFlag=TEXT_MATCHES_REGEX, isScrollable=1)
        if head is '':
            log_test_framework(tag, 'cannot find thread = ' + thread)
            #content = 'NULL'
            #return content
    
    
    click_textview_by_text(head)
    try:scroll_to_top()
    except:pass
    
    if search_text('Sent', isScrollable=0, searchFlag=TEXT_CONTAINS):
        text_date = get_view_text_by_id(VIEW_TEXT_VIEW, 'date_view')
        log_test_framework('weixiang', str(text_date))
        click_textview_by_text(text_date, clickType=LONG_CLICK)
        sleep(10)
        click_textview_by_id('forward')
        click_textview_by_id('recipients_editor')
        ime.IME_input_number(1, forwardTo, "c")
        click_textview_by_id('send_button_sms')
        take_screenshot()
        flag = True
    else:
        flag = False
    """
    flag = False
    for i in range(10):  # scroll down for 10 pages
        if flag is True:
            break
        #for index in range(3, 16, 2):
        for index in range(1, 10, 1):
            try:
                content = get_view_text_by_index(VIEW_TEXT_VIEW, index)
                click_textview_by_index(index + 1)
                if content == 'Type message':  # this is the bottom of current page
                    log_test_framework('weixiang', 'xxxxxxxxxx1')
                    goback()
                    drag_by_param(50, 70, 50, 20, 20)
                    break
            except:
                if search_text('Message details', isScrollable=0):goback()
                # scroll_down()
                log_test_framework('weixiang', 'xxxxxxxxxx2')
                drag_by_param(50, 70, 50, 20, 20)
                break
            
            if search_text('Type: Text message', isScrollable=0, searchFlag=TEXT_CONTAINS):
                log_test_framework('weixiang', 'xxxxxxxxxx3')
                if search_text('Message details', isScrollable=0):goback()
                log_test_framework('weixiang', 'xxxxxxxxxx4')
                text = get_view_text_by_index(VIEW_TEXT_VIEW, index)
                click_textview_by_text(text, clickType=LONG_CLICK)
                
                sleep(10)
                click_textview_by_id('forward')
                click_textview_by_id('recipients_editor')
                ime.IME_input_number(1, forwardTo, "c")
                click_textview_by_id('send_button_sms')
                take_screenshot()
                flag = True
                break
            elif search_text('Message details', isScrollable=0):goback()

    """
    if not flag:
        log_test_framework('weixiang', 'xxxxxxxxxx5')
        log_test_framework(tag, 'no sms in thread = ' + thread)
        content = 'NULL'
    
    mms.go_home()
    #return content


def forward_mms_in_thread(forwardTo, thread=''):
    tag = 'forward_sms_in_thread()'
    
    mms.click_home_icon()
    if '' == thread:
        click_imageview_by_id('attachment')
        s = get_view_text_by_id(VIEW_TEXT_VIEW, 'action_bar_title', isScrollable=0).decode('utf-8')
    
    else:
        thread = str(thread)
        thread = thread[0:3] + '\s?' + thread[3:7] + '\s?' + thread[7:11] + '.*'
        s = get_text(thread, searchFlag=TEXT_MATCHES_REGEX, isScrollable=1)
        if not s:
            log_test_framework(tag, 'cannot find thread = ' + thread)
            content = 'NULL'
            return content
        click_textview_by_text(s, searchFlag=TEXT_MATCHES_REGEX)
    log_test_framework(tag, 's = ' + s)
    
    
    try:scroll_to_top()
    except:pass
    flag = False

    for i in range(10):  # scroll 10 pages at most
        if flag:
            break
        for index in range(3, 16, 2):
            try:
                content = get_view_text_by_index(VIEW_TEXT_VIEW, index)
                edittextFlag = get_view_text_by_index(VIEW_TEXT_VIEW, index + 1)
                click_textview_by_index(index)
                if edittextFlag == 'Type message':  # this is the text show in edittext
                    goback()
                    drag_by_param(50, 70, 50, 20, 20)
                    break
            except:
                if search_text('Message details', isScrollable=0):goback()
                # scroll_down()
                drag_by_param(50, 70, 50, 20, 20)
                break
            
            if search_text('Type: Multimedia message', isScrollable=0, searchFlag=TEXT_CONTAINS):
                if search_text('Message details', isScrollable=0):goback()
                text = get_view_text_by_index(VIEW_TEXT_VIEW, index)
                click_textview_by_text(text, clickType=LONG_CLICK)
                
                click_textview_by_text('Forward')
                click_textview_by_id('recipients_editor')
                ime.IME_input_number(1, forwardTo, "c")
                
                # entertext_edittext_by_id('subject','Forward mms')
                click_view_by_container_id('recipients_subject_linear', 'android.widget.EditText', 0)
                ime.IME_input_english(1, '', input_type='p')
                entertext_edittext_on_focused('forward mms', isScrollable=0, isClear=0)
                
                
                if is_view_enabled_by_id(VIEW_BUTTON, 'send_slideshow_button', isScrollable=0):  click_button_by_id('send_slideshow_button', isScrollable=0)
                elif is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'send_button_mms', isScrollable=0):  click_imageview_by_id('send_button_mms', isScrollable=0)
                    
                if is_view_enabled_by_text(VIEW_BUTTON, 'OK', isScrollable=0):
                    click_button_by_text('OK')
                take_screenshot()
                flag = True
                break
            
            elif search_text('Message details', isScrollable=0):goback()

    
    if flag is False:
        log_test_framework(tag, 'no mms in thread = ' + thread)
        content = 'NULL'
    
    mms.click_home_icon()
    return content

def creat_slideshow(thread):
    tag = 'creat_slideshow()'
    
    mms.click_home_icon()
    click_textview_by_id('action_compose_new', isScrollable=0)
    entertext_edittext_by_id('recipients_editor', thread, isScrollable=0)
    click_textview_by_desc('Attach', isScrollable=0)
    click_textview_by_text('Slideshow')
    
    click_textview_by_text('Slide 1', isScrollable=0)
    # click_button_by_text('Add picture',isScrollable=0)
    # click_imageview_by_id('icon_mime',isScrollable=0)
    click_menuitem_by_text('Duration.*', searchFlag=TEXT_MATCHES_REGEX)
    click_textview_by_text('10 seconds')
    entertext_edittext_by_id('text_message', 'new slideshow 1', isScrollable=0)
    
    click_menuitem_by_text('Add slide', isScrollable=0)
    # click_button_by_text('Add picture',isScrollable=0)
    # click_imageview_by_id('icon_mime',isScrollable=0)
    click_menuitem_by_text('Duration.*', searchFlag=TEXT_MATCHES_REGEX)
    click_textview_by_text('10 seconds')
    entertext_edittext_by_id('text_message', 'new slideshow 2', isScrollable=0)
    
    click_button_by_id('done_button', isScrollable=0)
    click_button_by_id('send_slideshow_button', isScrollable=0)
    # click_textview_by_id('send_button_mms',isScrollable=0)
    
    mms.click_home_icon()
    sleep(3)
    
    pass


def send_msg(category='sms'):
    tag = 'send_msg(%s)' % category
    
    mms.click_home_icon()
    click_textview_by_id('action_compose_new', isScrollable=0)



def msg_exist(thread, content):
    thread = str(thread)
    tag = 'msg_exist(%s,%s)' % (thread, content)
    log_test_case(tag, 'start')

    thread = '(+86)?' + thread[0:3] + '\s?' + thread[3:7] + '\s?' + thread[7:11] + '.*'
    click_textview_by_text(thread, searchFlag=TEXT_MATCHES_REGEX)
    if is_view_enabled_by_text(VIEW_TEXT_VIEW, '.*' + content, searchFlag=TEXT_MATCHES_REGEX):
        log_test_case(tag, 'true end')
        return True

    log_test_case(tag, 'false end')
    return False

