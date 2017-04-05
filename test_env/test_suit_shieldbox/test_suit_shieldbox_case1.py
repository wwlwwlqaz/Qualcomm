from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_shieldbox_case1(TestCaseBase):
    def test_case_main(self, case_results):
        for i in range(0,1000):
            call("test_suit_shieldbox", "test_suit_shieldbox_case2")