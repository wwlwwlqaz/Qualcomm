#coding=utf-8

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log
from background_case_pool.bg_test_case_base import BgTestCaseBase
from qrd_shared.case import *

class test_suit_network_case1(BgTestCaseBase):
    def test_case_main(self):
        log_test_framework('test_suit_network_case1 start', '-----------')
        while True:
            sleep(3)
            os.system("ping www.baidu.com")