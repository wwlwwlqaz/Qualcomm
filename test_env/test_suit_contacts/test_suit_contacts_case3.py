'''
    file level export and import contact:

    1.export or impport contact
    2.if you want you may export/import all records.
    3.if you want you might choose simcard1 or simcard2

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @see: L{test_loader <test_loader>}
    @see: L{test_case_base<test_case_base>}
    @see: L{test_suit_base<test_suit_base>}
    @note:  support dsds
    @attention:
    @bug:
    @warning:

'''

# notificationBar.check_miss_call()
#

import fs_wrapper
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_contacts_case3(TestCaseBase):
    def import_from_storage(self):
        """
        This function import from storage.
        @return:  none
        """

        send_key(KEY_MENU)
        #import/export
        #click_in_list_by_index(2)
        log_test_case(self.name, 'sometime cant find the ui,so wait for 1 s.')
        sleep(1)

        str_menu_import_export = contact.get_value('menu_import_export')
        log_test_case(self.name, str_menu_import_export)
        click_in_list_by_index(2)

        str_import_from_sdcard = contact.get_value('import_from_sdcard')
        log_test_case(self.name, str_import_from_sdcard)
        if not search_text(str_import_from_sdcard):
            click_textview_by_text(str_menu_import_export)

        #click_in_list_by_index(2)
        str_import_from_sdcard = contact.get_value('import_from_sdcard')
        click_textview_by_text(str_import_from_sdcard)

        strphone = contact.get_value('add_phone')
        if search_text(strphone):
            click_textview_by_text(strphone)

        # search need time, wait for at most 15s
        str_import_all_vcard_string = contact.get_value('import_all_vcard_string')

        count = 0
        while not search_text(str_import_all_vcard_string, 1, 0) :
            sleep(1)
            count = count + 1
            if count > 30:
                log_test_case(self.name, 'can not find vcard')
                set_cannot_continue()
                goback()
                return


        #select import all vcard files
        #click_textview_by_text(str_import_all_vcard_string)

        #default select the first only import the first for save test time
        click_button_by_index(1)

        #click ok
        click_button_by_index(1)

        #wait for at leart 5 sec
        sleep(3)
        return


    def import_from_simcard(self):
        """
        This function import from simcard.
        @return:  none
        """

        send_key(KEY_MENU)
        #import/export
        #click_in_list_by_index(2)
        log_test_case(self.name, 'sometime cant find the ui,so wait for 1 s.')
        sleep(1)

        str_menu_import_export = contact.get_value('menu_import_export')
        log_test_case(self.name, str_menu_import_export)
        click_in_list_by_index(2)

        log_test_case(self.name, 'import from simcard')
        click_in_list_by_index(0)

        str_import_from_sim = contact.get_value('import_from_sim')
        if search_text(str_import_from_sim):
            click_button_by_index(0)
            #click_button_by_id('btn_ok')

        log_test_case(self.name, ' to phone')
        click_in_list_by_index(0)

        log_test_case(self.name, 'only select first')
        click_in_list_by_index(0)

        log_test_case(self.name, ' ok')
        click_button_by_id('btn_ok')

        #click ok
        click_button_by_index(1)

        log_test_case(self.name, ' wait for at least 4s')
        sleep(4)
        return

    def export_to_storage(self):
        """
        This function export to storage.
        @return:  none
        """

        send_key(KEY_MENU)
        log_test_case(self.name, 'sometime cant find the ui,so wait for 1 s.')
        sleep(1)

        log_test_case(self.name, 'export or import')
        click_in_list_by_index(2)

        log_test_case(self.name, 'export to storage')
        click_in_list_by_index(3)

        log_test_case(self.name, ' ok')
        click_button_by_index(1)

        #wait for at leart 5 sec
        sleep(3)

        return

    def export_to_simcard(self):
        """
        This function export to simcard.
        @return:  none
        """

        send_key(KEY_MENU)
        #import/export
        #click_in_list_by_index(2)
        log_test_case(self.name, 'sometime cant find the ui,so wait for 1 s.')
        sleep(1)

        log_test_case(self.name, 'export or import')
        click_in_list_by_index(2)

        log_test_case(self.name, 'export to simcard')
        click_in_list_by_index(2)

        str_export_to_sim = contact.get_value('export_to_sim')
        if search_text(str_export_to_sim):
            click_button_by_index(0)
            #click_button_by_id('btn_ok')

        log_test_case(self.name, 'select first')
        click_in_list_by_index(0)

        log_test_case(self.name, ' ok')
        click_button_by_id('btn_ok')

        log_test_case(self.name, ' wait for at least 4s')
        sleep(5)

        return

    def test_case_main(self, case_results):
        """
        main function ,entry export or import feature
        @return:  none
        """

        self.export_to_simcard()
        self.export_to_storage()
        self.import_from_simcard()
        self.import_from_storage()

        #notificationBar.check_miss_call()
        #notificationBar.check_email()
        #notificationBar.new_message()
        notificationBar.clear_all()

        return
