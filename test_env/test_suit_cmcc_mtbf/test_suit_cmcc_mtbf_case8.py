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
#    send 5 times mails with attachments to check whether send successfully or not.
#precondition:
#    1.the network normal
#    2.terminal has a 139 account mailbox
#    3.mailbox is empty
#steps:
#    1. open the E-mail application.
#    2. empty mailbox.
#    3. edit the message, enter the recipient's address, message subject, content and insert an attachment (picture) 
#    4. send e-mail.
#    5. confirm that the message is sent successfully.
#    6. delete sent messages on the mailbox. (Step 2 clear function)
#    7. exit the E-mail application.
############################################

class test_suit_cmcc_mtbf_case8(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case8 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case8"
        cmccMTBF.launch_app_by_name("email")

        sleep(2)
        #receive inbox emails
        if(receive_inbox_email() == False):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'long time to receive inbox emails')
            set_cannot_continue()
            qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'send e-mail failed', logging_wrapper.SEVERITY_HIGH)

        #empty Inbox messages
        empty_mailbox()

        #empty Outbox messages
        if(receive_email(cmccMTBF.get_value("email_outbox")) == True):
            empty_mailbox()

        for i in range(0,2):#5
            sleep(2)
            #edit the message and send e-mail.
            click_imageview_by_id("compose")
            sleep(1)

            result = cmccMTBF.email_write_email("auto_test_email@163.com", "email.sample", "test email for CMCC MTBF",True)
            if result == False:
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'send e-mail failed')
                set_cannot_continue()
                qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'send e-mail failed', logging_wrapper.SEVERITY_HIGH)

            goback()

            #empty sent messages
            if (receive_email(cmccMTBF.get_value("email_sentbox")) == False):
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'long time to receive Sent emails')
                set_cannot_continue()
                qsst_log_case_status(logging_wrapper.STATUS_FAILED, 'send e-mail failed', logging_wrapper.SEVERITY_HIGH)
            empty_mailbox()

        #exit
        goback()
        goback()
        goback()
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'send e-mail with attachment successfully', logging_wrapper.SEVERITY_HIGH)
