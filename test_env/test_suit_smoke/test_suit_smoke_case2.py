import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    smoke test case
############################################

class test_suit_smoke_case2(TestCaseBase):
    def test_case_main(self,case_results):
        goToSleepMode(4);
        sleep(2)
        goToSleepMode()
        sleep(2)
        wakeUpDevice()
        call("test_suit_weibo", "test_suit_weibo_case1")
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))