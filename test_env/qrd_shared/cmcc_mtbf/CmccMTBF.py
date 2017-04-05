#coding=utf-8
'''
   This class was create for cmcc mtbf.

   @author:
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{Base <Base>}
   @note:
   @attention:
   @bug:
   @warning:

'''

from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.ime.IME import IME
from logging_wrapper import log_test_framework
from qrd_shared.launcher.Launcher import Launcher
class CmccMTBF(Base):
    '''
    CmccMTBF is a class for cmcc mtbf.

    @see: L{Base <Base>}
    '''
    TAG = "CmccMTBF"
    '''@var TAG: tag of CmccMTBF'''
    FOLDER_NAME = "cmcc_mtbf"
    IMAGE_NAME = "image"
    AUDIO_NAME = "audio"
    VIDEO_NAME = "video"
    def __init__(self):
        '''
        init function.
        '''
        self.mode_name = "cmcc_mtbf"
        self.ime = IME()
        self.launcher = Launcher()
        Base.__init__(self, self.mode_name)
        self.debug_print('cmcc_mtbf init:%f' % (time.time()))

    def launch_app_by_name(self, name):
        self.launcher.launch_from_launcher(name)

    def messaging_delete_all_threads(self):
        '''
        delete all threads.
        '''
        send_key(KEY_MENU)
        delete_all_threads = self.get_value("messaging_delete_all_threads")
        if search_text(delete_all_threads):
            click_textview_by_text(delete_all_threads)
            click_button_by_index(1)
            wait_for_fun(lambda:search_text(self.get_value("messaging_no_conversations")), True, 5)
        else:
            goback()

    def messaging_click_home_icon(self):
        '''
        click home icon.

        @return: true-if click success.false-if click failed.
        '''
        if wait_for_fun(lambda:search_view_by_id("home"), True, 10):
            click_imageview_by_id("home")
            return True
        log_test_framework(self.TAG, "Can't search view 'home'.")
        return False

    def messaging_send_sms(self, send_slot_number, recive_phone_number, content):
        '''
        use slot1 or slot2 to send a sms to a specific phone number,then check whether send success.

        @type send_slot_number: string
        @param send_slot_number: send slot,1-slot1,2-slot2
        @type recive_phone_number: number
        @param recive_phone_number: the phone nunber that recive the message.
        @type content: string
        @param content: text message.
        @return: true-if send success,false-if send failed.
        '''
        num = recive_phone_number
        mms_text = content
        click_imageview_by_id('action_compose_new')
        click_textview_by_id("recipients_editor")
        #self.ime.IME_input_number(1, num, "c")
        entertext_edittext_by_id('recipients_editor', num)
        click_textview_by_text(self.get_value("messaging_type_message"))
        #self.ime.IME_input_english(1, mms_text)
        entertext_edittext_by_id('embedded_text_editor', mms_text)
        click_imageview_by_id('send_button_sms')
        #click_button_by_index(send_slot_number - 1)
        return self.messaging_check_send_success()

    def messaging_check_draft_function(self, recive_phone_number, content):
        '''
        use slot1 or slot2 to send a sms to a specific phone number,then check whether send success.

        @type recive_phone_number: string
        @param recive_phone_number: the phone nunber that recive the message.
        @type content: string
        @param content: text message.
        @return: true-if send success,false-if send failed.
        '''
        num = recive_phone_number
        mms_text = content
        click_imageview_by_id('action_compose_new')
        click_textview_by_id("recipients_editor")
        #self.ime.IME_input_number(1, num, "c")
        entertext_edittext_by_id('recipients_editor', num)
        click_textview_by_text(self.get_value("messaging_type_message"))
        #self.ime.IME_input_english(1, mms_text, input_type='t')
        entertext_edittext_by_id('embedded_text_editor', mms_text)
        self.messaging_click_home_icon()
        click_textview_by_text(self.get_value("messaging_draft"), searchFlag = TEXT_CONTAINS)
        phone_number = self.messaging_format_phone_number(recive_phone_number)
        b_number = search_text(phone_number)
        b_msg = search_text(content)
        self.messaging_click_home_icon()
        return (b_number and b_msg)

    def messaging_check_draft_function_with_attch(self, recive_phone_number, content, type):
        '''
        use slot1 or slot2 to send a sms to a specific phone number,then check whether send success.

        @type recive_phone_number: string
        @param recive_phone_number: the phone nunber that recive the message.
        @type content: string
        @param content: text message.
        @type content: string
        @param content: attach type.
        @return: true-if send success,false-if send failed.
        '''
        num = recive_phone_number
        click_textview_by_text(self.get_value("messaging_draft"), searchFlag = TEXT_CONTAINS)
        phone_number = self.messaging_format_phone_number(recive_phone_number)
        b_number = search_text(phone_number)
        b_msg = search_text(content)

        if type == self.IMAGE_NAME:
            click_button_by_text(self.get_value("messaging_view"))
            b_attach = search_text(self.get_value("messaging_gallery"))
            goback()
        elif type == self.AUDIO_NAME:
            b_attach = search_text(self.get_value("messaging_play"))
        elif type == self.VIDEO_NAME:
            click_button_by_text(self.get_value("messaging_view"))
            b_attach = search_text(self.get_value("messaging_video"))
            goback()
        self.messaging_click_home_icon()
        return (b_number and b_msg and b_attach)

    def messaging_send_mms_with_attachment(self, recive_phone_number, content, attachment, send):
        '''
        use slot1 or slot2 to send a sms to a specific phone number,then check whether send success.

        @type recive_phone_number: string
        @param recive_phone_number: the phone nunber that recive the message.
        @type content: string
        @param content: text message.
        @type content: boolean
        @param content: whether send this mms.
        @return: true-if send success,false-if send failed.
        '''
        num = recive_phone_number
        mms_text = content
        click_imageview_by_id('action_compose_new')
        click_textview_by_id("recipients_editor")
        #self.ime.IME_input_number(1, num, "c")
        entertext_edittext_by_id('recipients_editor', num)
        click_textview_by_text(self.get_value("messaging_type_message"))
        #self.ime.IME_input_english(1, mms_text, input_type='t')
        entertext_edittext_by_id('embedded_text_editor', mms_text)
        if attachment == self.IMAGE_NAME:
            self.messaging_add_attach(self.IMAGE_NAME, self.get_value("messaging_gallery"))
        elif attachment == self.AUDIO_NAME:
            self.messaging_add_audio_attch()
        elif attachment == self.VIDEO_NAME:
            self.messaging_add_attach(self.VIDEO_NAME, self.get_value("messaging_video"))
        if send:
            click_textview_by_desc(self.get_value("messaging_send_mms"))
            return self.messaging_check_send_success()
        self.messaging_click_home_icon()
        return True

    def messaging_add_attach(self, name, open_app):
        click_textview_by_desc(self.get_value("messaging_attach"))
        if name == self.IMAGE_NAME:
            click_textview_by_text(self.get_value("messaging_pictures"))
        elif name == self.VIDEO_NAME:
            click_textview_by_text(self.get_value("messaging_videos"))
        click_textview_by_text(self.get_value("messaging_file_explorer"))
        click_textview_by_text(self.get_value("messaging_folder"))
        click_textview_by_text(self.get_value("messaging_phone_storage"))
        click_textview_by_text(self.FOLDER_NAME)
        click_textview_by_text(name)
        #if serach_text(open_app):
        #    click_textview_by_text(open_app)

    def messaging_add_audio_attch(self):
        click_textview_by_desc(self.get_value("messaging_attach"))
        click_textview_by_text(self.get_value("messaging_audio"))
        click_textview_by_text(self.get_value("messaging_system_audio"))
        click_textview_by_text("Andromeda")
        click_textview_by_text("ok")

    def messaging_check_send_success(self):
        func = lambda:search_text(self.get_value("messaging_sent"), searchFlag = TEXT_CONTAINS)
        if wait_for_fun(func, True, 30):
            return self.messaging_click_home_icon()
        self.messaging_click_home_icon()
        return False

    def messaging_format_phone_number(self, num):
        '''
        format phone number,for example:format "12345678901" to "123 4567 8901"

        @type num: string
        @param num: phone number that need format
        @return: a phone number which have formated
        '''
        s = self.messaging_insert(num, ' ', 3)
        return self.messaging_insert(s, ' ', 8)

    def messaging_insert(self, original, new, pos):
        '''
        insert a new string into a tuple.

        @type original: string
        @param original: original string
        @type new: string
        @param new: a string that need insert.
        @type pos: number
        @param pos: position that need insert.
        @return: a new string.
        '''
        return original[:pos] + new + original[pos:]

    def browser_clear_browser_history_cookie(self):
        send_key(KEY_MENU)
        click_textview_by_text(self.get_value("browser_settings"))
        click_textview_by_text(self.get_value("browser_privacy"))

        if is_view_enabled_by_text(VIEW_TEXT_VIEW, self.get_value("browser_clear_cache")):
            click_textview_by_text(self.get_value("browser_clear_cache"))
            click_textview_by_text(self.get_value("browser_ok"))

        if is_view_enabled_by_text(VIEW_TEXT_VIEW, self.get_value("browser_clear_history")):
            click_textview_by_text(self.get_value("browser_clear_history"))
            click_textview_by_text(self.get_value("browser_ok"))
        if is_view_enabled_by_text(VIEW_TEXT_VIEW, self.get_value("browser_clear_all_cookie_data")):
            click_textview_by_text(self.get_value("browser_clear_all_cookie_data"))
            click_textview_by_text(self.get_value("browser_ok"))
        goback()
        goback()

    def browser_access_browser(self, url_address, check_value):
        scroll_down()
        time.sleep(1)
        click_textview_by_id("url")
        send_key(KEY_DEL)
        entertext_edittext_by_id("url", url_address)
        send_key(KEY_ENTER)

        start_time = int(time.time())
        while int(time.time()) - start_time < 60:
            scroll_down()
            time.sleep(1)
            if search_view_by_id("favicon"):
                click_button_by_id("favicon")
                if search_text(self.get_value("browser_loading")):
                    click_textview_by_text(self.get_value("browser_ok"))
                    continue
                if search_text(unicode(check_value), searchFlag = TEXT_CONTAINS):
                    click_textview_by_text(self.get_value("browser_ok"))
                    return True
                if search_text("WWW。SINA。COM"):
                    click_textview_by_text(self.get_value("browser_ok"))
                    return True
        return False

    def browser_exit_browser(self):
        send_key(KEY_MENU)
        click_textview_by_text(self.get_value("browser_exit"))

    def _download_and_delete_files(self, url_address, wait_time):

        #addressing config web address
        click_textview_by_id("url")
        sleep(1)
        entertext_edittext_on_focused(url_address)

        #go
        send_key(KEY_ENTER)
        sleep(1)

        # download or play, select download
        wait_fun = lambda: search_view_by_id("alertTitle")
        wait_result = wait_for_fun(wait_fun, True, wait_time)
        if wait_result == True:
            #download button id is button1
            click_button_by_id("button1")

        #rename download filename using current time.
        time_string = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

        sleep(2)
        if search_view_by_id("download_filename_edit"):
            entertext_edittext_by_id("download_filename_edit", time_string)

        sleep(1)
        click_textview_by_id("download_start")

        for i in range(1000):
            sleep(5)
            download_status_text = get_view_text_by_id(VIEW_TEXT_VIEW, "status_text")
            in_find = download_status_text.find("progress")
            if -1 == in_find:
                break

        log_test_case(self.mode_name, 'The downloaded filename ' + time_string)

        #no progress bar, downloading is completed, play or open
        if -1 == in_find :
            #play or open the file
            sleep(1)
            if search_view_by_id("download_icon"):
                click_imageview_by_id("download_icon")
                sleep(5)
                activity_name = get_activity_name()
                if -1 == activity_name.find("Download"):
                    goback()

        sleep(1)
        #delete select the download item
        if search_view_by_id("download_checkbox"):
            click_textview_by_id("download_checkbox")
        # should be menu item, but no find interface ,so replace imageview it.
        click_imageview_by_id("delete_download")

        log_test_case(self.mode_name, time_string + ' file was deleted!')

        #from download activity back to browser
        goback()

    def download_url_browser(self, url_address, wait_time, is_checked = True):
        '''
        check whether access url successfully

        @type url_address: string
        @param url_address: url address.
        @type check_value: string
        @param check_value: when need check whether access successfully, this is the check value.
        @type wait_time: number
        @param wait_time: when check access , the wait time.
        @type is_checked: boolean
        @param is_checked: whether check to access successfully.
        @return: True: access successful; False: no.
        '''

        if is_checked == True:
            #clear the browser cache
            #self.clear_cache()
            #self.clear_cache_history_cookie_data()
            self.browser_clear_browser_history_cookie()

        for i in range(5):
            log_test_case(self.mode_name, 'repeat ' + str(i))
            self._download_and_delete_files(url_address, wait_time)

        #quit brower
        goback()
        #minimize or quit, quit id is == button1
        if search_view_by_id("alertTitle"):
            click_button_by_id("button1")

        return True

    def file_explorer_check_file_exist(self):
        '''
        check whether there is file in a directory
        @return: trur-if there is some files, false-if there is no file
        '''
        send_key(KEY_MENU)
        click_textview_by_text(self.get_value('file_explorer_delete'))
        if not  is_view_enabled_by_index(VIEW_CHECKBOX,0):
            goback()
            return False
        goback()
        return True

    def file_explorer_delete_file(self):
        '''
        delete the first file in the list
        '''
        send_key(KEY_MENU)
        click_textview_by_text(self.get_value('file_explorer_delete'))
        if is_view_enabled_by_index(VIEW_CHECKBOX,0):
            click_checkbox_by_index(0)
        click_button_by_text(self.get_value('file_explorer_ok'))
        click_button_by_text(self.get_value('file_explorer_confirm'))
        sleep(1)

    def calendar_add_google_account(self, user_name, user_pwd):
        '''
        add google account.

        @type user_name: string
        @param user_name: google account name
        @type user_pwd: tuple
        @param user_pwd: google account password
        @return: whether add google account success
        '''
        click_textview_by_text(self.get_value("setting_add_account"))
        click_textview_by_text("Google")
        click_button_by_id("next_button")
        #entertext_edittext_by_id("username_edit", user_name)
        click_textview_by_id("username_edit")
        self.ime.IME_input(1, user_name)
        #entertext_edittext_by_id("password_edit", user_pwd)
        click_textview_by_id("password_edit")
        self.ime.IME_input(1, user_pwd)
        if search_text(self.get_value("setting_keep_me_up"), searchFlag=TEXT_CONTAINS):
            click_button_by_id("button1")
        if search_text(self.get_value("setting_account_exsits"), searchFlag=TEXT_CONTAINS):
            log_test_framework(self.TAG, "Account already exists.")
            click_button_by_id("next_button")
            start_activity("com.android.settings", ".Settings")
            return True
        #click_button_by_id("next_button")
        if not self.re_sign_in():
            log_test_framework(self.TAG, "Couldn't sign in.")
            return False
        if search_text(self.get_value("setting_entertainment"), searchFlag=TEXT_CONTAINS):
            click_button_by_id("skip_button")
        click_button_by_id("done_button")
        return True

    def calendar_delete_calendar_event(self):
        click_textview_by_id('top_button_date', 1, 0)
        click_textview_by_text(self.getValByCurRunTarget("calendar_agenda"))
        while search_view_by_id('agenda_item_color') == True:
            click_textview_by_id('agenda_item_color')
            click_textview_by_desc(self.getValByCurRunTarget("calendar_delete"))
            click_textview_by_text(self.getValByCurRunTarget("calendar_ok"))
        click_textview_by_id('top_button_date', 1, 0)
        click_textview_by_text(self.getValByCurRunTarget("calendar_day"))

    #MO by one slot
    #parameter:
    #    phoneNumber: the whole call phone number
    #    slot: 0--slot1, 1--slot2 2-- default slot can use for emergency call
    #Return:
    #    True: get through.
    #    False: no
    def phone_phone_call(self, phoneNumber):
        '''
        MO by one slot

        @type phoneNumber: string
        @param phoneNumber: the whole call phone number.
        @type slot: number
        '''
        #dial
        click_imageview_by_id("deleteButton",1,0,0,LONG_CLICK)
        for i in range(0, len(phoneNumber)):
            click_imageview_by_id(str(self.PREDEFINED_NUMBERS[phoneNumber[i]]))
        click_imageview_by_id("dialButton")

        sleep(1)
        if search_text(self.get_value("phone_network_not_available")):
            return False
        #whether get throught.
        phoneOn = False
        t = 0
        while search_view_by_id("endButton") and t < 10:
            if search_text("0:",searchFlag=TEXT_CONTAINS):
                phoneOn = True
                break
            sleep(1)
            t = t+1
        if phoneOn == False:
            return False
        else:
            return True

    #send an e-mail.
    def email_write_email(self, to_address, subject, body, attachment=False, sendFlag=True):
        '''
        send an e-mail.

        @type to_address: string
        @param to_address: destination address.
        @type subject: string
        @param subject: email subject.
        @type body: string
        @param body: email body text.
        @type attachment: boolean
        @param attachment: whether send email with attachment. If true, the attachment will be a picture.
        @return: True: send successfully. False: send failed.
        '''
        if (attachment):
            click_menuitem_by_text(self.get_value("email_add_attachment"))
            click_textview_by_text(self.get_value("email_file_explorer"))
            click_textview_by_text("Image")
            click_in_list_by_index(0, clickType=LONG_CLICK)
            sleep(1)
            click_textview_by_text(self.get_value("email_share"))
            click_textview_by_text(self.get_value("email_app"))
            click_textview_by_text(self.get_value("email_just_once"))
        sleep(1)

        click_textview_by_id("to")
        entertext_edittext_by_id("to",to_address)
        sleep(1)
        click_textview_by_id("subject")
        entertext_edittext_by_id("subject",subject)
        sleep(1)
        click_textview_by_id("body_text")
        entertext_edittext_by_id("body_text",body)
        sleep(1)

        if (sendFlag == True):
            click_imageview_by_id("send")

            if (attachment):
                goback()
                goback()
                goback()

            #check whether send successfully.
            sleep(2)
            click_imageview_by_id("show_all_mailboxes")
            click_textview_by_text(self.get_value("email_outbox"))
            click_imageview_by_id("refresh",1,0)
            outbox_loading_fun = lambda:search_text(self.get_value("email_no_messages"),1,1)
            fun_result = wait_for_fun(outbox_loading_fun,True,30)
            #When load long time, you can go back and enter again.
            if fun_result == False:
                goback()
                click_textview_by_text(self.get_value("email_outbox"))
                click_imageview_by_id("refresh",1,0)
                outbox_loading_fun = lambda:search_text(self.get_value("email_no_messages"),1,1)
                wait_for_fun(outbox_loading_fun,True,60)

            result = False
            count = get_view_text_by_id(VIEW_TEXT_VIEW,"spinner_count")
            if str(count) == "":
                result = True
            goback()
            return result