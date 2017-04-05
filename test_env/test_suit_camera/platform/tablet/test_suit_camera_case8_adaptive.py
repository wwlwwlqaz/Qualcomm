import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

def camera8(context):
    if not camera.take_picture():
        log_test_case(context.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'take picture failed')
        qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'take picture failed', logging_wrapper.SEVERITY_HIGH)
        set_cannot_continue()
        return
    click_imageview_by_desc("Most recent photo")