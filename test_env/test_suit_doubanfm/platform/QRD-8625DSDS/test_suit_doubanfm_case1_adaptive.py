import fs_wrapper
from case_utility import *
import settings.common as SC
from test_case_base import TestCaseBase
from qrd_shared.case import * 
import time

def doubanfm(context):
    while search_text(context.get_value("logining"),1,0):
        sleep(1)