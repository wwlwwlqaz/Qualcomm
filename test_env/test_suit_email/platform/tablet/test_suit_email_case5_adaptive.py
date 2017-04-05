import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import *
from test_case_base import TestCaseBase
from qrd_shared.case import *

def email5(context):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        launcher.launch_from_launcher('email')
        sleep(2)
        #login email
        if(get_activity_name().endswith("AccountSetupBasics")):
            goback()
            goback()
            if not email.add_email_account(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_EMAIL_EMAIL_PASSWORD_SEQUENCE):
                qsst_log_case_status(STATUS_FAILED, "add email account failed.", SEVERITY_HIGH)
                return False
            launcher.launch_from_launcher('email')
        # write an new email
        sleep(2)
        click_imageview_by_id("compose",1,0)
        sleep(2)

        subject = "email.sample"

        click_textview_by_id("to",1,0)
        ime.IME_input(1,SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, input_type="b")

        #input subject
        click_textview_by_id("subject")
        ime.IME_input_english(1,subject)

        #input content
        ime.IME_input_english(1,"test.email", input_type="b")
        #send mail
        click_imageview_by_id("send")

        qsst_log_case_status(STATUS_SUCCESS, "send email account success.", SEVERITY_HIGH)
        return True
