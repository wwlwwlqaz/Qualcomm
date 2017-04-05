import fs_wrapper
from case_utility import *
import settings.common as SC
from test_case_base import TestCaseBase
from qrd_shared.case import * 
import time

def doubanfm(context):
    loading_fun = lambda:search_text(context.get_value("logining"),1,0)
    if (wait_for_fun(loading_fun,False,30)==False):
        set_cannot_continue()
        log_test_case(context.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'It is seems login failed.')
        return