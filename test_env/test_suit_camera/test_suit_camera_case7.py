import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    chuanchunyu@cienet.com.cn
#function:
#    take a picture to share with renren
############################################

class test_suit_camera_case7(TestCaseBase):
    def test_case_main(self,case_results):
        camera.remember_photo_locations(False)
        if not InvokeFuncByCurRunTarget(self,"test_suit_camera","test_suit_camera_case8_adaptive","camera8"):
            return False
        sleep(3)
        qsst_log_msg("share with weibo")
        if not weibo.share_with_weibo(SC.PRIVATE_WEIBO_SHARE_PICTURE_SEQUENCE):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'shared with weibo failed')
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'shared with weibo failed', logging_wrapper.SEVERITY_HIGH)
            set_cannot_continue()
            return False
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'success', logging_wrapper.SEVERITY_HIGH)