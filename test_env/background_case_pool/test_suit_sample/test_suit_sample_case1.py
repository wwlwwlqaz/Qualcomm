#coding=utf-8

#以下是case需要的一些package根据需要import
import os
import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log
from qrd_shared.case import *
#必须import的package，表明这个是后台case
from background_case_pool.bg_test_case_base import BgTestCaseBase

#下面传入的参数必须是BgTestCaseBase，和前台case的TestCaseBase不一样一定要注意
class test_suit_sample_case1(BgTestCaseBase):
    def test_case_main(self):
        #后台case中的log只能用log_test_framework这个API显示。建议在开头和结尾都打上以便查看。
        log_test_framework('test_suit_sample_case1 start', '-----------')
        #因为是后台case所以我这里做了死循环，可以根据需要自己调整
        while True:
            #下面就是case的逻辑了
            sleep(3)
            #ping www.baidu.com
            os.system("ping www.baidu.com")
            log_test_framework('ping 百度', 'successful')
            #operate the sdcard
            if os.path.exists('/sdcard') == True:
                log_test_framework('test_suit_operate_sdcard_case1 ', 'had sdcard')
                #new a txt and write some things
                file = open("/sdcard/QSST_BG.txt",'wb')
                for i in range(102400):
                        file.write("back ground case"+str(i)+"\n")
                file.close()
                #delete the txt on the sdcard
                os.remove("/sdcard/QSST_BG.txt")
                #succeed the operate sdcard
                log_test_framework('operate sdcard', 'successful')
            else:
                #failed the operate sdcard
                log_test_framework('operate sdcard', 'failed')