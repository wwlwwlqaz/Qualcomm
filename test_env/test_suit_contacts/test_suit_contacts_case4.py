'''
    file level unit test qrdshare api for others:

    if anyone want to using the qrdshare api,
    please see the case example.

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:

    @see: L{test_loader <test_loader>}
    @see: L{test_case_base<test_case_base>}
    @see: L{test_suit_base<test_suit_base>}

    @note:
    @attention:
    @bug:
    @precondition:
    @warning:

'''

from logging_wrapper import log_test_case
from test_case_base import TestCaseBase
from  qrd_shared.case import *

class test_suit_contacts_case4(TestCaseBase):
    def test_case_main(self, case_results):
        """
        main function ,unit test the qrdshare contact API
        @return:  none
        """

        log_test_case(self.name, 'for example,add_contact_from_setting_config api')
        contact.add_contact_from_setting_config()
        contact.call_after_add_one_contact()
        return
