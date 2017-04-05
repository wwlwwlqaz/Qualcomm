'''
   shared library of email module.

   This class will provide operations api for email application.

   1.Developer can directly call those api to perform some operation.Such as:

     from qrd_shared.case import *
     email.add_email_account(SC.PRIVATE_EMAIL_EMAIL_ACCOUNT_SEQUENCE, SC.PRIVATE_EMAIL_EMAIL_PASSWORD_SEQUENCE)

   2.Developer can modify api or add some new api here. Before it, please make sure have been
     familiar with the structure.Modify existed api,please notice it won't affect others caller.


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see:
   @note:
   @attention:
   @bug:
   @warning:



'''
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
import time
from qrd_shared.case import *
from qrd_shared.ime.IME import IME

class Email(Base):
    '''
    Email is a class for operating Email application.

    @see: L{Base <Base>}
    '''
    def __init__(self):
        '''
        init function.

        @see: L{Base <Base>}
        '''
        self.mode_name = "email"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))

    #add an email account
    def add_email_account(self, user_name, user_pwd):
        '''
        add an email account

        @type user_name: string
        @param user_name: email user name.
        @type user_pwd: string
        @param user_pwd: email user password.
        @return: True: login successful; False: no.
        '''
        #Add Email Account
        ime = IME()
        start_activity('com.android.settings','.Settings')

        scroll_to_bottom()
        click_textview_by_text(self.get_value("add_account_label"),1,0)
        click_textview_by_text(self.get_value("app_email"),1,0)

        #input account
        click_textview_by_id("account_email",1,0)
        ime.IME_input(1,user_name)

        #input password
        ime.IME_input(1,user_pwd)
        #entertext_edittext_by_id("account_password",SC.PRIVATE_EMAIL_EMAIL_PASSWORD,1,0)

        sleep(1)
        click_button_by_id("next",1,0)
        click_button_by_id("pop",1,0)

        scroll_to_bottom()
        click_button_by_id("next",1,0)

        if not search_text(self.get_value("account_duplicate_dlg_title"),1,0):
            time = 0

            while (search_text(self.get_value("account_setup_check_settings_check_incoming_msg"),1,0) or search_text(self.get_value("could_not_open_connection"),1,0)) and time < 3:
                sleep(2)
                if search_text(self.get_value("could_not_open_connection"),1,0):
                    goback()
                    time = time + 1
                    click_button_by_id("next",1,0)

            if time == 3:
                return False
            else:
                click_imageview_by_id("account_security_type",1,0)
                click_textview_by_text(self.get_value("ssl_tls"),1,0)
                scroll_to_bottom()
                click_button_by_id("next",1,0)

                time = 0
                while (search_text(self.get_value("account_setup_check_settings_check_outgoing_msg"),1,0) or search_text(self.get_value("could_not_open_connection"),1,0)) and time < 3:
                    sleep(3)
                    if search_text(self.get_value("could_not_open_connection"),1,0):
                        goback()
                        time = time + 1
                        click_button_by_id("next",1,0)
                if time == 3:
                    return False

            fun = lambda:search_view_by_id("next")
            wait_for_fun(fun,True,10)

            click_button_by_id("next",1,0)
            sleep(3)

            click_textview_by_id("account_name",1,0)
            clear_edittext_by_id("account_name",1,0)
            sleep(1)
            ime.IME_input_english(1,"autotest")
            #entertext_edittext_by_id("account_name",SC.PRIVATE_EMAIL_ACCOUNT_NAME,1,0)

            click_button_by_id("next",1,0)
            sleep(1)
            goback()
            goback()
            return True
        else:
            goback()
            goback()
            goback()
            goback()
            goback()
            return False

    #write an email ,only text
    def write_email(self, to_address, subject, content):
        '''
        write an email ,only text

        @type to_address: string
        @param to_address: destination address.
        @type subject: string
        @param subject: email subject.
        @type content: string
        @param content: email content.
        '''
        ime = IME()

        #input to_address
        clear_edittext_by_id("to",1,0)
        ime.IME_input(1,to_address, input_type="b")

        #input subject
        click_textview_by_id("subject")
        ime.IME_input(1,subject)

        #input content
        ime.IME_input(1,content)
        #entertext_edittext_by_id("body_text",content)
        click_imageview_by_id("send")

    def send_email(self, to, subject, compose):#c_caijie
        click_button_by_id('compose_button')
        sleep(10)
        entertext_edittext_by_id("to",to)
        sleep(10)
        click_textview_by_id('subject')
        sleep(3)
        entertext_edittext_by_id("subject",subject)
        sleep(10)
        click_textview_by_id('body')
        sleep(3)
        entertext_edittext_by_id("body",compose)
        sleep(10)
        click_textview_by_id('send')
        sleep(120)
    def add_eamil_account(self):
        click_textview_by_id('account_email')
        sleep(3)
        entertext_edittext_by_id('account_email','comcatcmcc5@hotmail.com')
        sleep(10)
        click_textview_by_id('next')
        sleep(10)
        entertext_edittext_by_id('regular_password','zrf900422')
        if wait_for_fun(lambda:search_view_by_id("next"), True, 60):
            click_textview_by_id('next')
            sleep(60)
        for i in range(5):
                if search_text("Couldn't finish"):
                    click_button_by_text("Edit details")
                    sleep(3)
                    click_textview_by_id('next')
                    sleep(60) 
        click_textview_by_id('next')
        if wait_for_fun(lambda:search_view_by_id("next"), True, 60):
            click_textview_by_id('next')    