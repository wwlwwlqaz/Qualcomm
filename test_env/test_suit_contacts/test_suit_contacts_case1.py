'''
    file level add contactThis module will provide operations add contact record:

    1.phone/simcard/google account
    2.add name/phone number/address/email/photo.

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @see: L{test_loader <test_loader>}
    @see: L{test_case_base<test_case_base>}
    @see: L{test_suit_base<test_suit_base>}

    @note:
    @attention:
        delete all feature test pass.
        #self.del_contact_all()
    @bug:
    @warning:

'''
import fs_wrapper
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.ime.IME import IME
import settings.common as SC

class test_suit_contacts_case1(TestCaseBase):

    def add_photo(self):
        """
        This function add head photo.
        call camera moudle L{get_picture_by_camera}
        @return:  none
        """
        scroll_to_top()
        click_imageview_by_id('photo')
        # choose photo from gallery
        click_textview_by_index(0)
        camera.get_picture_by_camera()
        sleep(6)
        activityName = get_activity_name()
        if activityName == 'com.android.gallery3d.app.CropImage':
            click_textview_by_id('save')
        sleep(5)
        scroll_to_bottom()
        scroll_to_top()

        return

    def add_contact_to_phone(self, i):
        """
        This function add one record to phone.
        @type  i: number
        @param i: index for record,1,2,...
        @return:  none
        """

        click_textview_by_id('account_type')
        click_textview_by_text('PHONE')


        # fist time , input mothod is not show . show
        entertext_edittext_by_index(index = 0, value = 't')
        clear_edittext_by_index(0)
        #click_textview_by_text('Name')

        self.ime.IME_input_english(1, SC.PRIVATE_JACOB_NAME)
        self.ime.IME_input_english(1, SC.PRIVATE_JACOB_NAME)
        self.ime.IME_input_number(1, SC.PRIVATE_JACOB_NUMBER, 'n')
        self.ime.IME_input(1, SC.PRIVATE_JACOB_EMAIL)
        self.ime.IME_input_english(1, SC.PRIVATE_JACOB_ADDRESS)

        self.add_photo()

        #sometime overlap ok button when after tims run,so next skip the pop diag

        '''
        #add another field
        scroll_to_bottom()
        click_button_by_id('button_add_field')
        if search_text('Group'):
            click_textview_by_text('Group')
            click_button_by_index(0)
            click_in_list_by_index(0)
        else:
            goback()

        scroll_to_bottom()
        click_button_by_id('button_add_field')
        if search_text('Website'):
            click_textview_by_text('Website')
            entertext_edittext_on_focused('www.qualcomm.com')
        else:
            goback()

        scroll_to_bottom()
        click_button_by_id('button_add_field')
        if search_text('Notes'):
            click_textview_by_text('Notes')
            entertext_edittext_on_focused('Notes')
        else:
            goback()

        scroll_to_bottom()
        click_button_by_id('button_add_field')
        if search_text('Nickname'):
            click_textview_by_text('Nickname')
            entertext_edittext_on_focused('Nickname')
        else:
            goback()

        scroll_to_bottom()
        click_button_by_id('button_add_field')
        if search_text('Internet call'):
            click_textview_by_text('Internet call')
            entertext_edittext_on_focused('Internet call')
        else:
            goback()

        scroll_to_bottom()
        click_button_by_id('button_add_field')
        if search_text('IM'):
            click_textview_by_text('IM')
            entertext_edittext_on_focused('Instant message num')
        else:
            goback()
        return
        '''

    def add_contact_to_SIM_Card(self, index):
        """
        This function add one record to sim card.

        @type  index: number
        @param index: index of record.
        @return:  none
        """
        click_textview_by_id('account_type')
        click_textview_by_text('SIM')
        #entertext_edittext_by_index(0, 'hacker'+str(index))
        #entertext_edittext_by_index(1, '918801970004')
        self.ime.IME_input_english(1, SC.PRIVATE_CONTACT_NAME)
        self.ime.IME_input_number(1, "918801970004", 'n')
        return

    def IsfirstAddContact(self):
        """
        This function get the phone status,if first add the record
        for example,what happend is the bollow followings:
            1. restore factory setting
            2. erase user data
            3. reset contact data
        so simply check the whether the pop windows show keyword 'accounts'

        @rtype: boolean
        @return:  first time to add record-true, otherwise-false
        """
        if search_text(contact.get_value('accounts'), isScrollable = 0, searchFlag = TEXT_CONTAINS):
            click_in_list_by_index(0)
            return True
        else:
            return False


    def add_contact_to_google_account(self, i):
        """
        This function add one record to google account.
        call L{add_contact_to_phone}
        @type  i: number
        @param i: index for record,1,2,...
        @return:  none
        """

        self.add_contact_to_phone(i)

    def del_contact_all(self):
        """
        This function del all contact records
        @return:  none
        """

        send_key(KEY_MENU)
        delstr = contact.get_value('contact_delete')
        if search_text(delstr):
            click_textview_by_text(delstr)
            click_checkbox_by_id('select_all_check')
            click_button_by_id('btn_ok')
            click_button_by_index(1)
        else:
            goback()

        sleep(2)  #take a rest to wait view ...


    def test_case_main(self, case_results):
        """
        main function ,entry add feature
        @return:  none
        """
        self.ime = IME()

        click_imageview_by_index(0)
        click_imageview_by_index(2)
        click_imageview_by_index(1)

        # 1 -delete all
        #self.del_contact_all()

        # 2 -add some contact
        for i in range(1, 3):
            click_imageview_by_id('menu_add_contact')

            self.IsfirstAddContact()

            if i % 2:
                self.add_contact_to_phone(i)
            else:
                self.add_contact_to_SIM_Card(i)

            #click btn done
            #click_imageview_by_index(0)
            click_imageview_by_id('icon')
            sleep(1)

            # add favorite
            #click_textview_by_id('menu_star')
            #for ux
            click_textview_by_id('star')
            sleep(1)

            # goback
            click_imageview_by_index(0)
            sleep(3)


            if not can_continue():
                break

