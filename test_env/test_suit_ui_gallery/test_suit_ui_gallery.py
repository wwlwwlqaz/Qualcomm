from utility_wrapper import *
import fs_wrapper
from test_suit_base import TestSuitBase
from case_utility import *
from qrd_shared.case import *
import datetime,re



ALBUM_LOCATION = [(269,569),(573,601),(573,920),(573,1185)] # 4,3,2,1
PHOTO_LOCATION = [(134,280),(216,280),(361,280),(361,431),(361,574),(361,713)]

class test_suit_ui_gallery(TestSuitBase):
    pass



def deal_with_permission(permission = True):
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
        #log_test_framework(case_tag, "exit is wrong, may influence the next case")





def take_photo_in_gallery(case_tag,take_photo_num=1):
    tag = ''
    log_test_framework(TAG,'start')

    try:
        click_textview_by_desc(gallery.get_value("switch_camera"),waitForView=1)
    except:
        set_cannot_continue()
        log_test_case(case_tag, "cannot click the 'camera' in gallery")
        log_test_framework(TAG,'end with except')
    else:
        # deal with the annoying permission dialog, set 'always''allow'
        if search_text('Permission'):
            click_checkbox_by_id('permission_remember_choice_checkbox',isScrollable=0)
            click_button_by_text('Allow',isScrollable=0)
        
        if search_text('Complete action using'):
            click_button_by_text('Always')
        
        if search_text('Remember photo locations'):
            click_button_by_text('Yes')
        elif search_text('Tag your photos and videos with the locations'):
            click_button_by_text('NEXT')
        
        # click 'take_photo'
        try:
            for i in range(take_photo_num):
                click_imageview_by_id('shutter_button',isScrollable=0,waitForView=1)
        except:
            log_test_case(case_tag, "Take photo WRONG! click 'shutter_button' in camera")
            log_test_case(case_tag, "want take %s pieces, actually take %s"%(str(take_photo_num),str(i+1)))
            set_cannot_continue()
            log_test_framework(TAG,'end with except')
    
    log_test_framework(TAG,'end')




def get_current_pic_details():
    tag = 'get_current_pic_details()'
    log_test_framework(TAG,'start')

    photo_info_index = {'Title':1,'Time':2, }
    click_menuitem_by_text('Details')
    title = get_view_text_by_index(VIEW_TEXT_VIEW,photo_info_index['Title'])
    time = get_view_text_by_index(VIEW_TEXT_VIEW,photo_info_index['Time'])
    time = re.findall('(?<=Time: ).+M',time)[0]
    time = datetime.datetime.strptime(time,'%b %d, %Y %I:%M:%S %p')
    #goback()
    click_button_by_text('Close')
    
    log_test_framework(TAG,'end')
    return (title,time)
    
    

    
    