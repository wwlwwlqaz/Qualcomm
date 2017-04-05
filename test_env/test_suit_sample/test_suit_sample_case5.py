#coding=utf-8

#需要import的一些模块
from test_case_base import TestCaseBase
from logging_wrapper import *
from qrd_shared.case import *
from fs_wrapper import *
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher

#本条case是演示重启手机继续跑。
class test_suit_sample_case5(TestCaseBase):
    def test_case_main(self, case_results):
        #查看reboot标记，是否有被标记为reboot
        reboot = get_reboot_status("test_suit_sample", "test_suit_sample_case5")
        #如果没有被标记为reboot
        if not reboot:
            #标记为reboot，第一个参数为suit名字，第二个参数为case名字。
            save_reboot_status("test_suit_sample", "test_suit_sample_case5")
            #reboot the DUT
            #重启设备
            reboot_phone()
            pause_python_process()
        else:
            #恢复到重启时候的状态
            restore_reboot_status()
            launcher.launch_from_launcher('gallery')
        qsst_log_case_status(STATUS_SUCCESS, 'reboot success', SEVERITY_HIGH)