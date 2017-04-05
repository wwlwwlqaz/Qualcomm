import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase
import logging_wrapper

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    send 5 times mails without attachments to check whether send successfully or not.
#precondition:
#    1.the network normal
#    2.terminal has a 139 account mailbox
#        -- account:18621655020@139.com
#        -- pwd: email123
#    3.mailbox is empty
#steps:
#    1. open the E-mail application.
#    2. empty mailbox.
#    3. edit the message, enter the recipient's address and the message subject and content (see resources page).
#    4. send e-mail.
#    5. confirm that the message is sent successfully.
#    6. delete sent messages on the mailbox. (Step 2 clear function)
#    7. exit the E-mail application.
############################################

class test_suit_cmcc_mtbf_case7(TestCaseBase):
    '''
    test_suit_cmcc_mtbf_case7 is a class for cmcc_mtbf case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self,case_results):
        TAG = "test_suit_cmcc_mtbf_case7"
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

        for i in range(0,5):
            sleep(2)
            #edit the message and send e-mail.
            click_imageview_by_id("compose")
            sleep(1)

            result = cmccMTBF.email_write_email("auto_test_email@163.com", "email.sample", "test email for CMCC MTBF")
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
        qsst_log_case_status(logging_wrapper.STATUS_SUCCESS, 'send e-mail without attachment successfully', logging_wrapper.SEVERITY_HIGH)

def receive_inbox_email():
    '''
    receive inbox email
    '''
    click_imageview_by_id("refresh")
    loading_fun = lambda:search_text(cmccMTBF.get_value("email_status_loading"))
    loading_flag = wait_for_fun(loading_fun,False,30)
    #When load long time, you can go back and enter again. 
    if (loading_flag == False):
        goback()
        start_activity("com.android.email",".activity.EmailActivity")
        click_imageview_by_id("refresh")
        lambda:search_text(cmccMTBF.get_value("email_status_loading"))
        loading_flag = wait_for_fun(loading_fun,False,30)
    return loading_flag

def receive_email(box):
    '''
    receive email of outbox,Sent and etc.
    '''
    click_imageview_by_id("show_all_mailboxes")
    click_textview_by_text(box)
    click_imageview_by_id("refresh")
    loading_fun = lambda:search_text(cmccMTBF.get_value("email_status_loading"))
    loading_flag = wait_for_fun(loading_fun,False,30)
    #When load long time, you can go back and enter again. 
    if (loading_flag == False):
        goback()
        click_textview_by_text(box)
        loading_fun = lambda:search_text(cmccMTBF.get_value("email_status_loading"))
        loading_flag = wait_for_fun(loading_fun,False,30)
    return loading_flag

def empty_mailbox():
    scroll_to_top()
    for a in range(0,999):
        if (search_text(cmccMTBF.get_value("email_no_messages")) == False):
            click_in_list_by_index(0)
            sleep(1)
            for i in range(0,999):
                if(search_view_by_id("delete") == True):
                    click_imageview_by_id("delete")
                    click_imageview_by_id("button1")
                    sleep(1)
                else:
                    break;
        else:
            break;
