from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#     The signal icon shows right on UI
############################################

class test_suit_launcher_case4(TestCaseBase):
    def test_case_main(self,case_results):
        call("test_suit_camera", "test_suit_camera_case9")
        notificationBar.clear_all()
        notificationBar.drag_down()
        if not search_view_by_id('carrier_label'):
            set_cannot_continue()
            self.dealwith_result(case_results)
            return
        if search_text(launcher.get_value('no_service'), searchFlag=TEXT_CONTAINS):
            set_cannot_continue()
            self.dealwith_result(case_results)
            return
        if search_text(launcher.get_value('no_sim'), searchFlag=TEXT_CONTAINS):
            set_cannot_continue()
            self.dealwith_result(case_results)
            return
        if search_text(launcher.get_value('sim_deactivated'), searchFlag=TEXT_CONTAINS):
            set_cannot_continue()
            self.dealwith_result(case_results)
            return

    def dealwith_result(self,case_results):
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
