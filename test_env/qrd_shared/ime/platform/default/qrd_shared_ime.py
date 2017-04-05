from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
from qrd_shared.case import *
from platform_check import get_platform_info

def click_default(context):
    click_textview_by_text(context.get_value("default"))

def googleime(context):
    click_textview_by_text(context.get_value("google_pinyin_settings"))
    sleep(1)
    if is_checkbox_checked_by_index(2) == True:
        click_textview_by_text(context.get_value("auto_capitalization"))
    goback()

def out(context):
    sleep(1)