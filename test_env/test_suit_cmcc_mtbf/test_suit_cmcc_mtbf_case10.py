import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper
from test_suit_cmcc_mtbf_case7 import receive_inbox_email,receive_email,empty_mailbox
############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    send 10 times mails with attachments to check whether send successfully or not.
#precondition:
#    1.the network normal
#    2.terminal has a 139 account mailbox
#    3.mailbox is empty
#steps:
#    1. open the E-mail application.
#    2. empty mailbox.
#    3. edit the message, enter the recipient's address, message subject, content and insert an attachment (picture).
#    4. confirm the address of the recipient, the message subject, and add an attachment.
#    5. edited messages stored in the Drafts.
#    6. enter the Drafts to open the message.
#    7. confirm that the e-mail address, subject, contents and attachments are correct and return to Drafts.
#    8. empty the mailbox mailbox.
#    9. to exit the E-mail application.
############################################

class test_suit_cmcc_mtbf_case10(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case10 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case10"
        cmccMTBF.launch_app_by_name("email")

        sleep(2)

        #receive inbox
        receive_inbox_email()

        to_address = "auto_test_email@163.com"
        subject = "email.sample"
        body = "test email for CMCC MTBF"

        #empty Draft messages
        if(receive_email(cmccMTBF.get_value("email_drafts")) == True):
            empty_drafts()

        sleep(2)
        #edit the message and send e-mail.
        click_imageview_by_id("compose")
        sleep(1)

        cmccMTBF.email_write_email(to_address, subject , body, True, False)
        click_menuitem_by_text(cmccMTBF.get_value("email_save_draft"))
        goback()
        goback()
        goback()
        goback()
        goback()

        for i in range(0,2):#10
            click_imageview_by_id("show_all_mailboxes")
            click_textview_by_text(cmccMTBF.get_value("email_drafts"))
            click_in_list_by_index(0)

            #confirm that the e-mail address, subject, contents and attachments are correct and return to Drafts.
            confirm_to = get_view_text_by_id(VIEW_TEXT_VIEW,"to")
            confirm_subject = get_view_text_by_id(VIEW_TEXT_VIEW,"subject")
            confirm_body = get_view_text_by_id(VIEW_TEXT_VIEW,"body_text")

            if( str(confirm_to).find(str(to_address)) == -1 or str(confirm_subject).find(str(subject)) == -1 or str(confirm_body).find(str(body)) == -1):
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'confirm drafts failed')
                set_cannot_continue()
                qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'confirm drafts failed', logging_wrapper.SEVERITY_HIGH)

            goback()
            goback()

        #empty Draft messages
        if(receive_email(cmccMTBF.get_value("email_drafts")) == True):
            empty_drafts()

        #exit
        goback()
        goback()
        goback()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'open emails successfully', logging_wrapper.SEVERITY_HIGH)

def empty_drafts():
    scroll_to_top()
    for i in range(0,999):
        if (search_text(cmccMTBF.get_value("email_no_messages")) == False):
            click_in_list_by_index(0)
            sleep(1)
            click_menuitem_by_text(cmccMTBF.get_value("email_discard"))
            click_imageview_by_id("button1")
        else:
            break;
