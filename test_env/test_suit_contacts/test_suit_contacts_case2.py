'''
    file level search and make call:

    1.search the special record
    2.if found call him/her.

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @see: L{test_loader <test_loader>}
    @see: L{test_case_base<test_case_base>}
    @see: L{test_suit_base<test_suit_base>}

    @note:
    @attention:
        mms/email/address can enabled if you want
    @bug:
    @precondition: add the special record
    @warning:

'''
#   search and send mms/email/call

import fs_wrapper
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
import settings.common as SC
from qrd_shared.ime.IME import IME
from qrd_shared.case import *

class test_suit_contacts_case2(TestCaseBase):
    def call_from_contact(self):
        """
        This function call from contact.
        @return:  none
        """

        log_test_case(self.name, 'call_from_contact')
        #lick_textview_by_text(SC.PRIVATE_CONTACT_NUMBER)
        click_textview_by_id('primary_action_view')
        sleep(1)
        goback()
        sleep(3)
        return

    def test_case_main(self, case_results):
        """
        main function ,entry search and show contact record
        @return:  none
        """

        log_test_case(self.name, 'drag up and down')
        drag_by_param(95, 50, 95, 85, 1)
        drag_by_param(95, 85, 95, 50, 1)
        sleep(1)
        drag_by_param(95, 50, 95, 85, 1)
        drag_by_param(95, 85, 95, 50, 1)
        sleep(1)
        self.ime = IME()
        click_imageview_by_id('menu_search')
        #entertext_edittext_on_focused('Mi')
        #clear_edittext_by_index(0)
        '''
        PRIVATE_del = ['del']
        self.ime.IME_input(1, PRIVATE_del)
        self.ime.IME_input(1, PRIVATE_del)
        self.ime.IME_input(1, PRIVATE_del)
        '''

        self.ime.IME_input_english(1, 'tes')
        sleep(2)
        if search_text(SC.PRIVATE_CONTACT_NAME):
            log_test_case(self.name, 'search name ok...')
            click_textview_by_text(SC.PRIVATE_CONTACT_NAME)
            #click_in_list_by_index(1)
        else:
            log_test_case(self.name, 'search failed...')
            return

        self.call_from_contact()

        #send sms to mike
        click_textview_by_id('secondary_action_button')
        self.ime.IME_input_english(1, 'send')
        #click_imageview_by_desc("send")
        click_button_by_id('send_button_sms')
        sleep(3)
        goback()

        #click_textview_by_text('binz')
        # show a moment
        sleep(1)

        #send EMAIL
        if search_text('jubao@qunar.com'):
            click_textview_by_text('jubao@qunar.com')

            #
            if search_text('Complete action using'):
                click_textview_by_text('Email')
                click_button_by_id('button_always')
            entertext_edittext_on_focused('email title')

            click_imageview_by_id("send")

        else:
            goback()

        # go address map
        scroll_to_bottom()
        if search_text('ADDRESS'):
            click_textview_by_text('pudong,shanghai,china')
        else:
            goback()
