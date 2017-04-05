#coding=utf-8
'''
Test gallery.

This case is main to test gallery. Include take photos ,double click photo, zoom_by_param and so on.

@author: U{c_ywan<c_ywan@qti.qualcomm.com>}
@version: version 1.0.0
@requires: python 2.7+
@license: license

@see: L{test main<test_main>}

@note: none'''

import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import fs_wrapper
from case_utility import *

'''
launch gallery. Take a photo through the camera button which in gallery. After it, scan photo ,double click the photo ,zoom_by_param the photo.
'''

class test_suit_gallery_case1(TestCaseBase):
    def test_case_main(self, case_results):
        #Open camera
        click_textview_by_desc(gallery.get_value("switch_camera"),waitForView=1)
        sleep(1)
        #Choose camera
        if search_text(gallery.get_value("choose_camera")):
            click_textview_by_text(gallery.get_value("choose_camera"), waitForView=1)
            sleep(1)
            click_textview_by_text(gallery.get_value("just_once"), waitForView=1)
            sleep(1)
        else:
            sleep(1)
        #take photo
        click_imageview_by_desc(gallery.get_value("Shutter_button"), waitForView=1)
        sleep(1)
        goback()
        sleep(1)
        if search_view_by_id("home"):
            pass
        else:
            send_key('3')
            sleep(1)
            click_textview_by_desc(gallery.get_value("switch_camera"),waitForView=1)
        if search_text(gallery.get_value("Albums")):
            pass
        else:
            click_textview_by_id("text1", waitForView=1)
            #choose Albums
            click_textview_by_text(gallery.get_value("Albums"), waitForView=1)
            sleep(1)
        a=0
        while True:
            #click
            x1=y1=0
            a=10+a
            drag_by_param(x1+a, y1+a, x1+a, y1+a, 1)
            if not search_text(gallery.get_value("Albums")):break
        while True:
            #click
            x1=y1=0
            a=10+a
            drag_by_param(x1+a, y1+a, x1+a, y1+a, 1)
            if not search_view_by_desc(gallery.get_value("Navigate_up")):break
        #click photo
        double_click(50,50)
        sleep(1)
        drag_by_param(50, 50, 50, 50, 1)
        sleep(1)
        double_click(50,50)
        sleep(1)
        zoom_by_param(ZOOM_DOWN)
        sleep(1)
        zoom_by_param(ZOOM_UP)
