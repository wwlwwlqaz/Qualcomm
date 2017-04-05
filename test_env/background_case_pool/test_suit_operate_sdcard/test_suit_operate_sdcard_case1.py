#coding=utf-8

import os
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log
from background_case_pool.bg_test_case_base import BgTestCaseBase
from qrd_shared.case import *

class test_suit_operate_sdcard_case1(BgTestCaseBase):
    def test_case_main(self):
        log_test_framework('test_suit_operate_sdcard_case1 start', '-----------')
        while True:
            sleep(3)
            if os.path.exists('/sdcard') == True:
                log_test_framework('test_suit_operate_sdcard_case1 ', 'had sdcard')
                file = open("/sdcard/QSST_BG.txt",'wb')
                for i in range(102400):
                        file.write("back ground case"+str(i)+"\n")
                file.close()
                os.remove("/sdcard/QSST_BG.txt")
            log_test_framework('test_suit_operate_sdcard_case1', 'successful')