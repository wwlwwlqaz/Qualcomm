#coding=utf-8

import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import fs_wrapper
from case_utility import *
from utility_wrapper import *

############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#    share a picture in gallery
#precondition:
#    have 1 photo in gallery at least
#    have SIM in slot1
############################################
import os,re
from test_suit_ui_gallery import *


class test_suit_ui_gallery_case06(TestCaseBase):
    tag = 'ui_gallery_case06'    

    def test_case_main(self, case_results):
        case_flag = False
        
        #
        # STEP 1: need SIM to share photo by MMS
        #
        if 'no available sim card' == get_sim_card_state(SLOT_ONE):
            set_cannot_continue()
            log_test_case(self.tag, "get_sim_card_state(SLOT_ONE):" + 'no available sim card')
        #
        # STEP 2: choose a photo to share
        #
        if can_continue():
            flag = click_photo_in_album()
            if False == flag:
                set_cannot_continue()
                log_test_case(self.tag, "cannot find album or photo, maybe coordinate point is wrong")
        
        #
        # STEP 3: share photo by MMS
        #        
        if can_continue():
            # click 'share' button
            func = lambda:search_view_by_desc('More options') or ( click(300,600) and search_view_by_desc('More options') )
            if not wait_for_fun(func,True,3):
                set_cannot_continue()
                log_test_case(self.tag, "cannot find the 'share'")
            else:
                # click 'Share with''Messaging' button
                try:
                    click_imageview_by_desc('Share with')
                    click_textview_by_text('Messaging')
                except:
                    goback()
                    click_view_by_container_id('activity_chooser_view_content','android.widget.ImageView',1)
                # deal with the annoying permission dialog ,set 'always''allow'
                deal_with_permission()
                
                # write MMS
                send_to_seq = SC.PUBLIC_SLOT1_PHONE_NUMBER_SEQUENCE
                write_mms(send_to_seq)

        #
        # STEP 4: confirm whether sharing is successfully
        #
        if can_continue():
           
            # get the number to send MMS
            # send_to_num == 'num_sign13636591260'
            send_to_num = ''.join(send_to_seq)
            try:
                # send_to_num == '13636591260'
                send_to_num = re.findall('\d{11}',send_to_num)[0]
                send_to_num = send_to_num[0:3]+' '+send_to_num[3:7]+' '+send_to_num[7:]
            except:
                set_cannot_continue()
                log_test_case(self.tag, "the format of PHONE_NUMBER_SEQUENCE in SC maybe wrong")
            
            # confirm the MMS sending state
            if can_continue():
                case_flag = send_state(send_to_num)
                
        #
        # STEP 4: exit
        #
        exit_cur_case(self.tag)
            
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "share photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))


def click_photo_in_album():
    tag = 'click_photo_in_album()'
    flag = False
    N_album = len(ALBUM_LOCATION)
    n = 0
    func = lambda:search_view_by_id('up')
    while(n<N_album and False==flag):   # click album
        click(ALBUM_LOCATION[n][0],ALBUM_LOCATION[n][1])
        if wait_for_fun(func,True,timeout = 2):  # now click photo
            N_photo = len(PHOTO_LOCATION)
            n = 0
            func = lambda:search_view_by_id('photopage_bottom_control_edit')
            while(n<N_photo and False==flag):
                click(PHOTO_LOCATION[n][0],PHOTO_LOCATION[n][1])
                if wait_for_fun(func,True,timeout = 2):
                    flag = True
                n += 1
        n += 1
    
    return flag


def write_mms(send_to_seq):
    tag = 'write_mms()'
    click_textview_by_text('To')
    # PUBLIC_SLOT1_PHONE_NUMBER_SEQUENCE = ['num_sign', '1', '3', '6', '3', '6', '5', '9', '1', '2', '6', '0']

    ime.IME_input(ime_type=1, content_seq=send_to_seq)
    func = lambda:is_view_enabled_by_id(VIEW_TEXT_VIEW, 'send_button_mms', isVerticalList=1, isScrollable=0)
    if not wait_for_fun(func,True,3):
        set_cannot_continue()
        log_test_case(TAG, "'send'button is not enabled, maybe no SIM in phone")
    else:
        # send MMS
        click_textview_by_id('send_button_mms')
        sleep(2)
        goback()
        goback()
        goback()


def send_state(receiver_num):
    tag = 'send_state(receiver_num)'
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


