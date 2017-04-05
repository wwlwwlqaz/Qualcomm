from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
import time
from qrd_shared.launcher import Launcher

############################################
#author:
#    yileiwan@cienet.com.cn
#function:
#    Open gallery.
#doc:
############################################

class Gallery(Base):
    def __init__(self):
        self.mode_name = "gallery"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))
        
#added by c_yazli
    def go_home(self):
        for i in range(10):
            if search_text("Albums"):
                log_test_framework("Gallery", "Enter gallery successfully")
                break
            else:
                send_key(KEY_BACK)
        sleep(1)

    def share_with_messaging(self):
        #click_imageview_by_desc('More options')
        #click_imageview_by_index(1)
        #sleep(3)
        #click_textview_by_text('Select item')
        #sleep(5)
        long_click(176,631)
        if wait_for_fun(lambda:search_view_by_id("action_share"), True, 3):
            click_textview_by_id('action_share')
        if wait_for_fun(lambda:search_text("Messaging"), True, 60):
            click_textview_by_text('Messaging')
            sleep(3)
            
    def edit_with_vintage(self):
        #click_imageview_by_desc('More options')
        #click_imageview_by_index(1)
        #sleep(3)
        #click_textview_by_text('Select item')
        #sleep(5)
        long_click(176,631)
        sleep(3)
        click_imageview_by_index(2)
        sleep(3)
        click_textview_by_text('Edit')
        sleep(3)
        if search_text('Gallery'):
            click_textview_by_text('Gallery')
            sleep(5)
        if search_view_by_id('filtershow_done'):
            click(609, 1582)
            sleep(3)
#         if search_view_by_desc("Vintage"):
#             click_imageview_by_desc("Vintage")
#             sleep(3)
        if search_view_by_id('filtershow_done'):
            click_textview_by_id('filtershow_done')
            sleep(8)
        if search_view_by_id('imgDone'):
            click_textview_by_id('imgDone')
            sleep(8)
    
    def edit_sharpness(self):
        click_imageview_by_index(1)
        sleep(3)
        click_textview_by_text('Select item')
        sleep(5)
        click(176, 631)
        sleep(3)
        click_imageview_by_index(2)
        sleep(3)
        click_textview_by_text('Edit')
        if wait_for_fun(lambda:search_view_by_id("colorsButton"), True, 5):
            click_imageview_by_index(3)
            sleep(2)
            if wait_for_fun(lambda:search_view_by_desc("Sharpness"), True, 5):
                click(1022, 1587)
                if wait_for_fun(lambda:search_view_by_id("slider_save"), True, 5):
                    click_button_by_id("slider_save")
                    if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                        click_textview_by_id("filtershow_done")  
                        
                        
    def gallery_widget(self):
        send_key(KEY_HOME)
        sleep(1)
        long_click(587,1042)
        if wait_for_fun(lambda:search_text("WIDGETS"), True, 5):
            click_textview_by_id("widget_button")
            sleep(2)            
            drag_by_param(50, 90, 50, 10, 10)
            sleep(2)
            drag_by_param(50, 90, 50, 10, 10)
            sleep(2)
            drag_by_param(50, 90, 50, 10, 10)
            sleep(2)
            long_click(246,1737)
            sleep(2)
#             if wait_for_fun(lambda:is_view_enabled_by_text(VIEW_TEXT_VIEW, "Snapdragon Gallery"), True, 5):
#                 long_click(246,1737)
            if wait_for_fun(lambda:search_text("Choose an image"), True, 5):
                click_button_by_text("Choose an image")
                sleep(2)
                click(290,539)
                sleep(2)
                click(187,392)
                if wait_for_fun(lambda:search_text("SAVE"), True, 5):
                    click_textview_by_text("SAVE")
                                            