from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
# Launch Camera app and then exit.
# Launch Camcorder app and then exit. //no camcorder in our qrd platform
# Launch clock and then exit.
# Launch Calendar and then exit.
# Launch  Gallery and then exit.
# Launch Contact and then exit.
############################################

class test_suit_launcher_case1(TestCaseBase):
    def test_case_main(self,case_results):
        if not launcher.launch_from_launcher("camera"):
            self.dealwith_fail(case_results)
            return
        if not launcher.launch_from_launcher("clock"):
            self.dealwith_fail(case_results)
            return
        if not launcher.launch_from_launcher("calendar"):
            self.dealwith_fail(case_results)
            return
        if not launcher.launch_from_launcher("gallery"):
            self.dealwith_fail(case_results)
            return
        if not launcher.launch_from_launcher("people"):
            self.dealwith_fail(case_results)
            return
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
    def dealwith_fail(self,case_results):
        set_cannot_continue()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
