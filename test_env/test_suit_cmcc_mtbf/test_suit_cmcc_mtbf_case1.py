import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

class test_suit_cmcc_mtbf_case1(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case11 is a class for cmcc_mtbf case Add and remove contacts .

1, open the Address Book.
2 empty contact.
3, create a new contact.
4 confirm contacts newly added successfully.
5, delete the contact.
6 confirm contacts deleted successfully.
7, exit contacts."

repeat --- 20 
"3, create a new contact.
4 confirm contacts newly added successfully.
5, delete the contact.
6 confirm contacts deleted successfully."



"1, Add contacts successfully or not.
2, Delete contacts successfully or not."


    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def add_and_delete_one_record(self):
        click_imageview_by_id('menu_add_contact')
        if search_text(contact.get_value('accounts'), isScrollable = 0, searchFlag = TEXT_CONTAINS):
            click_in_list_by_index(0)
        click_textview_by_id('account_type')
        click_textview_by_text('PHONE')
        time_string = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        entertext_edittext_by_index(0, 'zhangfei' + time_string)
        entertext_edittext_by_index(1, 'yide')
        entertext_edittext_by_index(2, '13901000000')
        #click btn done
        click_imageview_by_id('icon')
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'save record' + time_string)
        sleep(1)
        if search_text(time_string, 0, 0, TEXT_CONTAINS):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'found record' + time_string)
            #click_textview_by_text(time_string, 0, 0, TEXT_CONTAINS)
            send_key(KEY_MENU)
            #delete
            click_in_list_by_index(2)
            #ok0
            #click_button_by_text('ok')
            click_button_by_id('button1')
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'delete record' + time_string)
            sleep(1)

    def test_case_main(self, case_results):
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Add and remove contacts')
        TAG = "test_suit_cmcc_mtbf_case1"
        cmccMTBF.launch_app_by_name("people")
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'Add and remove contacts')

        click_imageview_by_index(1)
        for i in range(20):
            log_test_case(TAG , 'repeat contact ' + str(i))
            self.add_and_delete_one_record()

        case_flag = True
        if case_flag :
            qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'Add and remove contacts success', logging_wrapper.SEVERITY_HIGH)
