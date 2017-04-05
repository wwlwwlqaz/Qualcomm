import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

def email5(context):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        launcher.launch_from_launcher('email')
        #login email
        if(get_activity_name().endswith("AccountSetupBasics")):
            goback()
            goback()
            local_assert(email.add_email_account(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_EMAIL_EMAIL_PASSWORD_SEQUENCE),True)
            launcher.launch_from_launcher('email')
        # write an new email
        sleep(2)
        click_imageview_by_id("compose",1,0)
        sleep(2)

        subject = "email.sample"

        click_textview_by_id("to",1,0)
        ime.IME_input(1,SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE)

        #input subject
        click_textview_by_id("subject")
        ime.IME_input_english(1,subject)

        #input content
        ime.IME_input_english(1,"test.email")
        ime.IME_input(1,'ceshi ','c')
        ime.IME_input_number(1,'12345','c')
        sepcial_character = ['num_sign','sign_1','sign_2','sign_3','num_sign']
        ime.IME_input(1,sepcial_character,'e')
        #send mail
        click_imageview_by_id("send")

        case_results.append((context.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
