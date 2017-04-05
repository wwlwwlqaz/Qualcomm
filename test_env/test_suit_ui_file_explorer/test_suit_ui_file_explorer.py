'''
   A class extends TestSuitBase for basic utility test of FileExplorer.


   @author: U{huitingn<huitingn@qti.qualcomm.com>}
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

import string,random,subprocess,shlex,re
from case_utility import *
import os,itertools
from qrd_shared.case import *
import test_suit_ui_gallery.test_suit_ui_gallery



CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}
BOOL_STK_VOCIE_CALL_CHECK = False

class test_suit_ui_file_explorer(TestSuitBase):
    '''
    test_suit_ui_file_explorer is a class for basic utility test of FileExplorer.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    pass



def rand_name(prefix = 'QT', only_letter = False, name_length = 8):
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



def exit_cur_case(case_tag):
    '''
    goback to homescreen. exit current case.
    
    @type case_tag: string
    @param case_tag:the calling case'TAG
    
    '''
    global current_case_continue_flag
    current_case_continue_flag = True
    
    func = lambda:( search_view_by_desc('Apps') or goback() )
    if not wait_for_fun(func,True,5):
        send_key(KEY_HOME)
        #if not search_view_by_desc('Apps'):    log_test_case(case_tag, "exit is wrong, may influence the next case")


def file_num_in_dir(file_type,dir):
    '''
    get the file number of specified file_type in appointed dir.

    @type file_type: string
    @param file_type: the type of file. e.g.:'jpg'
    @type dir: string
    @param dir: e.g.:'/sdcard/DCIM/Camera'
    @return: the number of specified file_type in appointed dir.
    '''
    #strCMD = "adb shell \"ls -l '/sdcard/DCIM/Camera' | grep '.jpg'\""
    strCMD = "adb shell \"ls -l '%s' | grep '.jpg'\""%dir
    p1 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
    (output,erroutput) = p1.communicate()
    p1.stdout.close()

    file_type = "\.%s.*\n"%file_type
    TYPE = re.compile( file_type )
    num1 = len(TYPE.findall(output))
    return num1

'''
Function relative_path() is used to get path2'relative_path to path1 

@return: string.
        path2'relative_path to path1

'''
def all_equal(elements):  
    first_element = elements[0]  
    for other_element in elements[1:]:  
        if other_element != first_element : return False  
    return True  
  
def common_prefix(*sequences):  
    if not sequences: return[],[]  
    common = []  
    for elements in itertools.izip(*sequences):  
        if not all_equal(elements):break  
        common.append(elements[0])  
    return common,[sequence[len(common):] for sequence in sequences]  
  
def relative_path(path1,path2, sep=os.path.sep, pardir=os.path.pardir):  
    '''
    Function relative_path() is used to get path2'relative_path to path1 
    
    @return: string.
            path2'relative_path to path1
    '''
    if r'/'==path1:
        return path2
    else:
        common,(u1,u2) = common_prefix(path1.split(sep),path2.split(sep))  
        if not common:  
            return path2      
        return sep.join([pardir] * len(u1) + u2)

'''

'''
def goto_dir(dir,window='Folder',go_from_home_screen=True):
    '''
    goto the appointed dir in FileExplorer.

    @type dir: string
    @param dir: e.g.:'/Phone storage/DCIM/Camera'
    @type window: string
    @param dir: e.g.:'Category' or 'Folder'
    @type go_from_home_screen:boolean
    @param go_from_home_screen:
    True is back to homescreen first and then goto dir
    False is goto dir from current view 
    @return: True for success, False for fail.
    '''
    tag = 'goto_dir()'
    
    log_test_framework(TAG,"start")
    if (window != 'Category')&(window !='Folder'):
        set_cannot_continue()
        return
    

    if go_from_home_screen:
        goto_FileExplorer()
        # click_textview_by_text(window,isScrollable=0) # this UI is removed in Android L
    
    
    #cur_path = get_view_text_by_id(VIEW_TEXT_VIEW,'tv_path')
    cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
    if cur_path is '':
        goback()
        cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
    want_path = dir
    
    if cur_path==want_path:
        goback()
        goto_dir(dir,window,go_from_home_screen=False) # update view
        return
    
    if re.findall('/.*',cur_path):
        path = relative_path(cur_path, want_path, r'/')
    else:
        path = '/'+dir
    
    dir = path
    sep = '/'
    sequ = dir.split('%s'%sep)
    if go_from_home_screen == True:
        for s in sequ:
            if s == '':     pass
            elif s == '..': goback()
            else:
                click_textview_by_text(s)
    else:
        for s in sequ:
            if s == '':     pass
            elif s == '..': goback()
            else:
                func = lambda:search_text(s,isScrollable=0) or drag_by_param(50,70,50,35,20)
                if wait_for_fun(func,True,60):
                    click_textview_by_text(s)
                else:
                    take_screenshot()
                    log_test_framework(TAG,"cannot goto %s"%want_path)
                    try:click_button_by_text('Cancel')
                    except:pass
                    set_cannot_continue()
                    break
        
    sleep(1)
    log_test_framework(TAG,"end")

'''
'''
def goto_FileExplorer():
    # launcher.launch_from_launcher("file_explorer")
    launcher.back_to_launcher()
    click_textview_by_desc('Apps')
    sleep(1)
    click_textview_by_text('Apps')
    if search_text('File Explorer',0,1):
        click_textview_by_text('File Explorer',0)        



def drag_up():
    drag_by_param(50, 100, 50, 10, 10)
    
    
def run_monkey_in_camera():
    tag = 'run_monkey_in_camera()'
    log_test_framework(TAG, "start")
    
    
    
    package = 'com.android.camera2'
    monkey_num = '1000'
    strCMD = "adb shell monkey -p " + package + ' '+ monkey_num +" --throttle 1000 --monitor-native-crashes --kill-process-after-error"
    p1 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
    (result,erroutput) = p1.communicate()
    p1.stdout.close()
    
    goback()
    goback()
    send_key(KEY_HOME)
    



def enable_bluetooth():
    tag = 'enable_bluetooth()'
    log_test_framework(TAG, "start")
    
    
    #start_activity("com.android.settings", ".Settings")
    launcher.launch_from_launcher('settings')
    click_textview_by_text("Bluetooth",waitForView=1)
    if search_text("When Bluetooth is turned on,"):
        click_textview_by_text('OFF')
        sleep(5)
    log_test_framework(TAG, "turn on bluetooth")


def bluetooth_pair():
    tag = 'bluetooth_pair()'
    log_test_framework(TAG, "start")
    
    flag = False
    # pair with another device
    if not search_text('Paired devices',isScrollable=0,searchFlag=TEXT_MATCHES):
        reciver = get_view_text_by_index(VIEW_TEXT_VIEW, 5)
        #reciver = get_view_text_by_index(VIEW_TEXT_VIEW, 6)
        click_textview_by_text(reciver)
        func = lambda:search_text('Bluetooth pairing request',isScrollable=0) ## also in slave:start #should open bt before
        if wait_for_fun(func,True,5):
            click_button_by_text('Pair')## also in slave:end
            func = lambda:search_text('Paired devices',isScrollable=0,searchFlag=TEXT_MATCHES)
            if wait_for_fun(func,True,30):
                flag = True
            else:
                log_test_framework(TAG,"cannot pair device")
                if search_text("Couldn't pair with",isScrollable=0):
                    click_button_by_text('OK')
    else:
        #click_imageview_by_id('icon',isScrollable=0) 
        flag = True
    
    return flag


def disable_bluetooth():
    tag = 'disable_bluetooth()'
    log_test_framework(TAG, "start")
    #start_activity("com.android.settings", ".Settings")
    launcher.launch_from_launcher('settings')
    click_textview_by_text("Bluetooth",waitForView=1)
    if search_text("When Bluetooth is turned on,"):
        click_textview_by_text('ON')
        sleep(5)
    log_test_framework(TAG, "turn off bluetooth")

            
def share_by_bluetooth(): #item_name_num
    tag = 'share_by_bluetooth()'
    log_test_framework(TAG, "start")
    
    flag = False
    notificationBar.clear_all()
    
    # click 'share' and choose 'share way'
    try:
        click_imageview_by_desc('Share',isScrollable=0)
        click_textview_by_text('Bluetooth',isScrollable=0)
    except:
        goback()
        click_view_by_container_id('default_activity_button', 'android.widget.ImageView', 0)
    
    if search_text('Just once',isScrollable=0):
        click_button_by_text('Just once',isScrollable=0)
    
    '''
    if not search_text('Paired devices',isScrollable=0,searchFlag=TEXT_MATCHES):
        click_view_by_container_id('list','android.widget.ImageView',0)
    '''
    click_imageview_by_id('icon',isScrollable=0)  ## slave should do something:accept

    notificationBar.drag_down()
    func = lambda:(not search_text('Bluetooth share: Sending') and search_text('Bluetooth share: Sent files'))
    if wait_for_fun(func,True,90):
        info = get_text('successful')
        #successful_num = int(len(re.findall('\d(?<=successful)',info)))
        unsuccessful_num = int(re.findall('(\d+)(?= unsuccessful)',info)[0])
        if unsuccessful_num > 0: # or successful_num < item_name_num
            flag = False
        else:
            flag = True

    return flag
                
 
 
def share_by_email(receiverEmail=SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE): 
    '''
    share the chosen item by email.

    @return flag: boolean
    True means the item has been shared by email and received.
    False means hasn't.
    '''
    tag = 'share_by_email()'
    log_test_framework(TAG, "start")
    
    
    # click 'share'
    click_textview_by_desc('Share',isScrollable=0)
    
    # choose 'share way'
    click_textview_by_text('Email',isScrollable=0)
    if search_text('Just once',isScrollable=0):
        click_button_by_text('Just once',isScrollable=0)
    
    # sent item by email
    email_subject =  rand_name(only_letter = True).lower()
    email.send_email_to(receiverEmail, email_subject, '',attachment=False, sendFlag=False)
    log_test_case(TAG,'email_subject = %s'%email_subject)
    
    return email_subject
    

def subject_received_by_email(subject,TIME = 5):
    '''
    check if specific subject email has been received
    only check the most new mail in inbox.

    @type subject: string
    @param subject: the subject of email.
    @type TIME: number
    @param TIME: try time.
    @return flag: boolean
    True means the specific subject email has been received
    False means hasn't.
    '''
    tag = 'subject_received_by_email(subject)'
    log_test_framework(TAG, "start")
    
    
    flag = False
    launcher.launch_from_launcher('email')
    if is_view_enabled_by_id(VIEW_IMAGE_VIEW,'arrow') and is_view_enabled_by_id(VIEW_IMAGE_VIEW,'dismiss_button'):
        click_imageview_by_id('dismiss_button')
        
    for t in range(TIME):
        click_view_by_container_id('list','android.view.View',0)
        if subject == get_view_text_by_id(VIEW_TEXT_VIEW,'subject',isScrollable=0):
            take_screenshot()
            flag = True
            return flag
        else:
            if is_view_enabled_by_id(VIEW_IMAGE_VIEW,'up',isScrollable=0) and is_view_enabled_by_id(VIEW_TEXT_VIEW,'subject',isScrollable=0):
                click_imageview_by_id('up')
            sleep(1)
            scroll_to_top()
            func = lambda:is_view_enabled_by_id(VIEW_TEXT_VIEW,'compose')
            wait_for_fun(func,True,5)
    
    return flag


def share_by_mms(forwardTo=SC.PUBLIC_SLOT1_PHONE_NUMBER_SEQUENCE): 
    '''
    share the chosen item by mms.

    @return flag: boolean
    True means the item has been shared by mms and received.
    False means hasn't.
    '''
    tag = 'share_by_mms()'
    log_test_framework(TAG, "start")
    
    
    # click 'share'
    click_textview_by_desc('Share',isScrollable=0)
    
    # choose 'share way'
    click_textview_by_text('Messaging',isScrollable=0)
    if search_text('Just once',isScrollable=0):
        click_button_by_text('Just once',isScrollable=0)
    
    # sent item by mms
    send_to_seq = forwardTo
    write_mms(send_to_seq)
    



def write_mms(send_to_seq):
    tag = 'write_mms()'
    log_test_framework(TAG, "start")
    
    
    click_textview_by_text('To')
    # PUBLIC_SLOT1_PHONE_NUMBER_SEQUENCE = ['num_sign', '1', '3', '6', '3', '6', '5', '9', '1', '2', '6', '0']

    #ime.IME_input(ime_type=1, content_seq=send_to_seq)
    ime.IME_input_number(1, SC.PUBLIC_SLOT1_PHONE_NUMBER, 'c')
    func = lambda:is_view_enabled_by_id(VIEW_TEXT_VIEW, 'send_button_mms',isScrollable=0)
    if not wait_for_fun(func,True,3):
        take_screenshot()
        set_cannot_continue()
        log_test_case(TAG, "'send'button is not enabled, maybe no SIM in phone")
    else:
        # send MMS
        click_textview_by_id('send_button_mms')
        if is_view_enabled_by_text(VIEW_BUTTON,'OK',isScrollable=0):
            click_button_by_text('OK')
        sleep(2)
        goback()
        goback()
        goback()


def send_state(receiver_num):
    '''
    check if specific receiver_num has received MMS.

    @type receiver_num: string
    @param receiver_num: the receiver's phone no.
    @return flag: boolean
    True means the specific receiver_num has received MMS.
    False means hasn't.
    '''
    tag = 'send_state(receiver_num)'
    log_test_framework(TAG, "start")
    
    
    flag = False
    
    #launcher = Launcher();
    
    send_key(KEY_HOME)
    launcher.launch_from_launcher('mms')
    #start_activity("com.android.mms","com.android.mms.ui.ConversationList") 

    mms.click_home_icon()
    func = lambda:search_text(receiver_num, searchFlag=TEXT_CONTAINS)# search '1 363-659-1260'
    if not wait_for_fun(func, True, 3):
        set_cannot_continue()
        log_test_case(TAG, "cannot find the 'receiver_num' in Messaging conversation list")
    else:
        click_textview_by_text(receiver_num, searchFlag=TEXT_CONTAINS)# click '1 363-659-1260'
        # wait until MMS has been sent
        func = lambda:search_text('SENDING',searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func,False,60):
            set_cannot_continue()
            log_test_case(TAG, "the MMS has been sending for more than 60s")
        else:
            mms.click_home_icon() 
            func = lambda:search_text(mms.get_value("received"), searchFlag=TEXT_CONTAINS,isScrollable=0)
            if not wait_for_fun(func,True,5):
                set_cannot_continue()
                log_test_case(TAG, "Received MMS on slot1 failed.")
            else:
                flag = True
    
    return flag




def phone_seq_to_phone_no(phone_seq):
    tag = 'phone_seq_to_phone_no(phone_seq)'
    log_test_framework(TAG, "start")
    
    
    # get the number to send MMS
    # phone_no == 'num_sign13636591260'
    phone_no = ''.join(phone_seq)
    # phone_no == '13636591260'
    phone_no = re.findall('\d{11}',phone_no)[0]
    phone_no = phone_no[0:3]+' '+phone_no[3:7]+' '+phone_no[7:]
    
    return phone_no



                

def deal_with_permission(permission):
    '''
    deal with the annoying permission dialog.
    
    @type permission: boolean
    @param permission:True is 'Allow', False is 'Deny'
    
    '''
    tag = 'deal_with_permission(permission)'
    if True == permission: 
        permission = 'Allow'
    elif False == permission: 
        permission = 'Deny'
    else: 
        set_cannot_continue()
        log_test_framework(TAG, "parameter is wrong. It can only be True or False")
    
    func = lambda:search_text('Permission') and \
        ( click_checkbox_by_id('permission_remember_choice_checkbox',isScrollable=0) or click_button_by_text(permission,isScrollable=0) )
    
    wait_for_fun(func,False,10)
    
    



def random_index_list_in_folder(folder,filetype):
    tag = 'random_index_list_in_folder()'
    log_test_framework(TAG,'start')

    
    IndexBase = 5
    
    num = num_of_filetype_in_folder(folder,filetype)
    assert num!=0 and num!=1 and num!=2,TAG+'%s return %s.\n'%(TAG,str(num))+'cannot produce random_index_list_in_folder()'
    
    list_len = random.randint(1,min((num,8))-1)
    random_list = random.sample(range(1*2,(list_len+1)*2,2),list_len) # step=2 even number
    index_base = [IndexBase for i in range(1,list_len+1)]
    random_index_list = [random_list[i] + index_base[i] for i in range(list_len)]

    
    log_test_framework(TAG,'end')
    return (random_index_list,num)

    
def num_of_filetype_in_folder(folder,filetype):
    tag = 'num_of_filetype_in_folder()'
    log_test_framework(TAG,'start')
    
    
    folder_in_mp = re.sub('Phone storage','sdcard',folder) #replace the name:/Phone storage/... to /sdcard/...
    strCMD = "adb shell \"ls -l '%s' | grep '%s'\""%(folder_in_mp,filetype)
    p1 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
    (output,erroutput) = p1.communicate()
    p1.stdout.close()

    FILETYPE = re.compile( "%s.*\n" %(filetype))
    num = len(FILETYPE.findall(output))

    
    log_test_framework(TAG,'end')
    return num



def preprocess(case_tag,work_dir,floor=0):
    tag = 'preprocess()'    
    log_test_framework(TAG,'start')
    
    
    number = num_of_filetype_in_folder(work_dir,'.jpg')
    if number<floor:
        launcher.launch_from_launcher('gallery')
        if floor==0 : n = random.randint(1,7)
        else: n = floor
        test_suit_ui_gallery.test_suit_ui_gallery.take_photo_in_gallery(case_tag,n)
        number = num_of_filetype_in_folder(work_dir,'.jpg')
        launcher.back_to_launcher()
        #send_key(KEY_HOME)
    
    
    log_test_framework(TAG,'end')
    return number
    
    