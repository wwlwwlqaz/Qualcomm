'''
   A class extends TestSuitBase for APP install, launch, exit, and then uninstall.


   @author: huitingn@qti.qualcomm.com
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




CASE_PLUG_IN_FUNCTION_NAME = 'case_plug_in'
test_suit_config_map = {}
global_suit_config_map = {}

class test_suit_ui_apk_cmcc(TestSuitBase):
    '''
    test_suit_nhtApp is a class for App install, launch, exit, and then uninstall.

    @see: L{TestSuitBase <TestSuitBase>}
    '''
    
    pass


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
    log_test_framework(tag,'start')
    if (window != 'Category')&(window !='Folder'):
        set_cannot_continue()
        return
    
    if go_from_home_screen:
        try:goto_FileExplorer()
        except:goto_FileExplorer()
        '''
        if not search_text(window,isScrollable=0,searchFlag=TEXT_MATCHES):
            goback()
        click_textview_by_text(window,isScrollable=0)
        '''
   
    
    cur_path = get_view_text_by_index(VIEW_TEXT_VIEW,0)
    want_path = dir
    if re.findall('/.*',cur_path):
        path = relative_path(cur_path, want_path, r'/')
    else:
        path = '/'+dir
    
    dir = path
    sep = '/'
    sequ = dir.split('%s'%sep)
    for s in sequ:
        if s == '':     pass
        elif s == '..': goback()
        else:           click_textview_by_text(s)
    sleep(1)
    
    log_test_framework(tag,'end')

'''
'''
    
def goto_FileExplorer():
    tag = 'goto_FileExplorer()'
    log_test_framework(tag,'start')
    # launcher.launch_from_launcher("file_explorer")
    launcher.back_to_launcher()
    send_key(KEY_HOME) # add for Android L notification
    goback()
    goback()
    click_textview_by_desc('Apps')
    sleep(1)
    click_textview_by_text('Apps')
    if search_text('File Explorer',0,1):
        click_textview_by_text('File Explorer',0)
    
    log_test_framework(tag,'end') 


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
        #if not search_view_by_desc('Apps'):    log_test_case(case_tag, "exit is wrong, may influence the next case")


def deal_with_install_block():
    tag = 'deal_with_install_block()'
    start_activity('com.android.settings','com.android.settings.Settings')
    if search_text('Security'):
        click_textview_by_text('Security')
        #log_test_framework(TAG,'Settings-Security')
        if search_text('Unknown sources'):
            #click_imageview_by_text('OFF')
            if is_view_enabled_by_text(VIEW_COMPOUNDBUTTON,'OFF',isScrollable=0):
                click_button_by_text('OFF')
                if search_text('Your phone and personal data'):
                    click_button_by_text('OK')
                    log_test_framework(tag,'Now you can install all 3rd party APKs')
                else:
                    log_test_framework(tag,'Maybe something wrong in apk security setting')
        goback()
        
        
def get_files_in_dir(category='TOOL',type='apk'):
    tag = 'get_files_in_dir()'
    
    osInfo = get_platform_info()
    if(osInfo == 'Linux-Phone' or osInfo == 'Linux-PC'):      sep = '/'
    elif(osInfo == 'Windows'):        sep = '\\'
    source_dir = 'C:'+sep+'NHTworkspace'+sep+'task1_100App'+sep+category+sep
    
    files = os.listdir( source_dir )
    rr = re.compile( "\.%s$" %type , re.I )
    apk_list = []
    for f in files:
        if rr.search(f):
            apk_list.append("%s"%f) 

    dest_dir = os.path.join(source_dir,'new')
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    dest_dir += sep

        
    log_test_framework(tag, "get all %s name in %s"%(type,category))
    return (apk_list,source_dir,dest_dir,sep)
