'''
    file level operations airplane mode test many times:

    call airplnemode case 2 many times.

'''
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_airplanemode_case1(TestCaseBase):
    def test_case_main(self, case_results):
        """
        This function entry for airplan mode function test
        call many times case2
        @return:  none
        """

        for i in range(0,1):
            call("test_suit_airplanemode", "test_suit_airplanemode_case2")