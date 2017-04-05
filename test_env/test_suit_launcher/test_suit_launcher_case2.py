from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#     1.Home screen, long press blank space.
############################################

class test_suit_launcher_case2(TestCaseBase):
    def test_case_main(self,case_results):
        drag_by_param(90,50,10,50,10)
        drag_by_param(90,50,10,50,10)
        drag_by_param(90,50,10,50,10)
        drag_by_param(90,50,10,50,10)
        long_click(400, 600)
        if not search_text(launcher.get_value("choose_wallpaper")):
            set_cannot_continue();
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
