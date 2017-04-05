#coding=utf-8

import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import fs_wrapper
from case_utility import *
from utility_wrapper import *
from kpi.performance import *

class test_suit_sample_case7(TestCaseBase):
    def test_case_main(self, case_results):
        kpi_log_value("launch_time","camera_001",1000)
        kpi_log_value("launch_time","camera_002",850)
        kpi_log_value("fps","camera_002",110)