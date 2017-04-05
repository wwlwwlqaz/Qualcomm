'''
   provide some interface of google play store application.

   This class will provide operations api of google play store application.

   1.Developer can directly call those api to perform some operation.

   2.Developer can add some new api.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
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
import time
class PlayStore(Base):
    '''
    PlayStore is a class for operating google play store application.

    @see: L{Base <Base>}
    '''
    TAG = "PlayStore"
    '''@var TAG: tag of PlayStore'''
    def __init__(self):
        '''
        init function.
        '''
        self.mode_name = "playstore"
        Base.__init__(self,self.mode_name)
        self.ime = IME()
        self.debug_print( 'PlayStore init:%f' %(time.time()))

    def download(self, name, description):
        '''
        download a application according to the application name and description.

        @type name: string
        @param name: application's name
        @type description: string
        @param description: applicaiton's description that is company name in most situations.
        @return: true-if the application download success,false-if the application download failed.
        '''
        click_button_by_id("search_button")
        #entertext_edittext_on_focused(name)
        click_textview_by_id("search_src_text")
        self.ime.IME_input_english(1, name)
        send_key(KEY_ENTER)
        sleep(20)
        click_textview_by_text(description)
        sleep(20)
        if search_text(self.get_value("uninstall")):
            log_test_framework(self.TAG, "find uninstall button," + name + " has been installed.")
            return True
        if search_text(self.get_value("install")):
            click_button_by_id("buy_button")
            click_button_by_id("acquire_button")
            click_imageview_by_id("home")
            pre_time = time.time()
            running = True
            while running:
                if search_text(self.get_value("uninstall")):
                    running = False
                    log_test_framework(self.TAG, "download " + name + " successed.")
                    return True
                if time.time() - pre_time > 10*60:
                    running = False
                    log_test_framework(self.TAG, "download " + name + " time out.")
                    click_button_by_id(self.TAG, "cancel_download")
                    log_test_framework(self.TAG, "cancel download " + name)
                    return False
        else:
            log_test_framework(self.TAG, "error in find install button interface, download " + name + " error.")
            return False