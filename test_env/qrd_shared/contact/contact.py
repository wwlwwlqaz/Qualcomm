'''
    add contact record and call it, share for others api:

    The added number and name should be config at setting module.

    @author: U{shijunz<shijunz@qti.qualcomm.com>}
    @version: zhiyangz
    @requires:python 2.7+
    @license:

    @note:
    @attention:
        only current actvity is contact.
    @bug:
    @warning:
'''
'''
    for example:
    def _demo_test_contact_api_()
    if( get_activity_name() != 'com.android.contacts'):
        start_activity('com.android.contacts','.activities.DialtactsActivity')
    if( read_config_setting) :
        add_contact_from_setting_config()
    else:
        add_contact_to_sim_card(_demo_name,_demo_number)

'''
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.case import *
import settings.common as SC


class Contact(Base):
    TAG = 'Contact Module : '
    
    def __init__(self):
        """
        This function init share contact api class.
        @return: none
        """

        self.mode_name = "contact"
        self.tag = 'qrd_share_contact'
        Base.__init__(self, self.mode_name)
        self.debug_print('contact init:%f' % (time.time()))
        
    def go_home(self):
        """
        This function is to go back to contact main entry
        @return: none
        """
        for i in range(10):
            flag1 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Favorites', isScrollable=0, searchFlag=TEXT_MATCHES)
            flag2 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'All contacts', isScrollable=0, searchFlag=TEXT_MATCHES)
            flag3 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Groups', isScrollable=0, searchFlag=TEXT_MATCHES)
            if flag1 & flag2 & flag3 is True: return True
            else: 
                goback()
                sleep(1)
        
        return False
    
    def go_home1(self):
        '''
        @author: min.sheng
        @attention: modify some code for function of go_home(self):
        @note: Suitable for M version
        '''
        for i in range(10):
            flag1 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Favorites', isScrollable=0, searchFlag=TEXT_MATCHES)
            flag2 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'All contacts', isScrollable=0, searchFlag=TEXT_MATCHES)
            if flag1 & flag2  is True: return True
            else: 
                goback()
                sleep(1)
        
        return False
        
        

    def add_contact_to_sim1(self, name, number):#c_caijie
        """
        This function share api for others add contact to simcard.
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: boolean value
        """
        if search_view_by_id('floating_action_button'):
            click_button_by_id('floating_action_button')
            sleep(3)
            if search_text('SIM1', isScrollable=0):
                #click_textview_by_text('SIM1')
                sleep(5)
                entertext_edittext_by_index(0, name)
                sleep(10)
                entertext_edittext_by_index(1, number)
                sleep(10)
                click_textview_by_id('menu_save')
                sleep(5)
                if search_view_by_id('permission_allow_button'):
                    click_button_by_id('permission_allow_button')
                    sleep(5)
                if search_view_by_id('permission_allow_button'):
                    click_button_by_id('permission_allow_button')
                    sleep(5)
                if search_view_by_id('permission_allow_button'):
                    click_button_by_id('permission_allow_button')
                    sleep(5)  
                send_key(KEY_BACK)
                sleep(2)
            else:                
                click_textview_by_text('More Fields')
                sleep(5)
                click_textview_by_id('account_type_selector')
                sleep(5)
                click_textview_by_text('SIM1')
                sleep(5)
                entertext_edittext_by_index(0, name)
                sleep(10)
                entertext_edittext_by_index(1, number)
                sleep(10)        
                click_textview_by_id('menu_save')
                sleep(5)
                if search_view_by_id('permission_allow_button'):
                    click_button_by_id('permission_allow_button')
                    sleep(5)
                if search_view_by_id('permission_allow_button'):
                    click_button_by_id('permission_allow_button')
                    sleep(5)
                if search_view_by_id('permission_allow_button'):
                    click_button_by_id('permission_allow_button')
                    sleep(5)  
                send_key(KEY_BACK)
                sleep(2)
            
        
    def add_contact_to_phone(self, name, number):#c_caijie
        """
        This function share api for others add contact to simcard.
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: none
        """
                       
        
        if search_view_by_id('floating_action_button'):
            click_button_by_id('floating_action_button')
            sleep(3)
            if search_text('Choose a default account for new contacts', isScrollable=0):
                click_textview_by_text('PHONE')
                sleep(5)     
            if search_text("Keep local", isScrollable=0):
                click_button_by_text("Keep local")
                sleep(3)            
        send_key(KEY_BACK)
        sleep(2)
        click_button_by_id('floating_action_button')
        sleep(3)
        entertext_edittext_by_index(0, name)
        sleep(10)
        entertext_edittext_by_index(1, number)
        sleep(10)


        # click btn done
        click_textview_by_id('menu_save')
        sleep(5)
        if search_view_by_id('permission_allow_button'):
                click_button_by_id('permission_allow_button')
                sleep(5)
        if search_view_by_id('permission_allow_button'):
                click_button_by_id('permission_allow_button')
                sleep(5)
        if search_view_by_id('permission_allow_button'):
                click_button_by_id('permission_allow_button')
                sleep(5)                
        #click_imageview_by_desc('Done')
        send_key(KEY_BACK)
        sleep(2)

    def add_email_to_contact(self, name, number, email):#c_caijie
        """
        This function share api for others add contact to simcard.
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: none
        """
                       
        
        if search_view_by_id('floating_action_button'):
            click_button_by_id('floating_action_button')
            sleep(3)
            if search_text('Keep local'):
                click_button_by_text("Keep local")
                sleep(5)
            if search_text('PHONE'):
                click_textview_by_text('PHONE')
                sleep(5)     
        entertext_edittext_by_index(0, name)
        sleep(10)
        entertext_edittext_by_index(1, number)
        sleep(10)
        entertext_edittext_by_index(3, email)
        sleep(10)

        # click btn done
        click_textview_by_id('menu_save')
        sleep(5)
        #click_imageview_by_desc('Done')
        self.go_home()
        sleep(2)
        
    def add_full_contact_to_phone(self, name, number, email, address, company):#c_caijie
        """
        This function share api for others add contact to simcard.
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: none
        """
        click_button_by_id('floating_action_button')
        sleep(3)     
        click_textview_by_text('More Fields')
        sleep(5)
        entertext_edittext_by_index(0, name)
        sleep(10)
        entertext_edittext_by_index(3, number)
        sleep(10)
        entertext_edittext_by_index(5, email)
        sleep(10)
        click_textview_by_text("Address")
        sleep(3)
        entertext_edittext_on_focused(address)
        sleep(10)
        click_textview_by_text("Company")
        sleep(2)       
        entertext_edittext_on_focused(company)
        sleep(10)        
        click_textview_by_id('menu_save')
        sleep(5)
        self.go_home()
        sleep(2)
    
    def add_contact_to_sim(self, name, number, sim_number=1):
        """
        This function share api for others add contact to simcard.
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: boolean value
        """
        sleep(1)
        if search_text("You can synchronize your new contact"):
            log_test_framework(self.TAG, "it indicate you are first time to use contact application")
            click_textview_by_text('SIM')
        elif search_text("You can synchronize your new contact"):
            log_test_framework(self.TAG, "Have not Detect Sim Card configure in contacts app")
            take_screenshot()
        else:
            log_test_framework(self.TAG, "you added contacts once")
        
        click_textview_by_id('account_type')
        sleep(1)
        if sim_number == 1:
            click_textview_by_text('SIM1')
        else:
            click_textview_by_text('SIM2')
       
        entertext_edittext_by_index(0, name)
        entertext_edittext_by_index(1, number)
        
        # click btn done
        click_imageview_by_desc('Done')
        self.go_home()
    
    def add_contact_from_dial(self, number, name):
        """
        This function share api for others add contact to simcard.
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: boolean value
        """
        if not (name):
            log_test_framework(self.TAG, "Cannot find in contacts. Add new from dialer panel")
            start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
            sleep(2)
            waitActivity = lambda:search_text(name)
            if wait_for_fun(waitActivity, True, 10):
                log_test_framework(self.TAG, "Find contact added from dialer")
                return True
            else : 
                log_test_framework(self.TAG, "Cannot find contact. Add contact from dialer failed")
                return False
        else:
            log_test_framework(self.TAG, "Already exist in contact")
            click_textview_by_text('Add to contacts', isScrollable=0)
            click_textview_by_text('Create new contact', isScrollable=0)
            entertext_edittext_by_index(0, name)
            click_imageview_by_desc('Done', isScrollable=0)
            
            start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
            sleep(2)
            click_textview_by_text('All contacts', isScrollable=0)
            waitActivity = lambda:search_text(name)
            if wait_for_fun(waitActivity, True, 10):
                log_test_framework(self.TAG, "Find contact added from dialer")
                return True
            else : 
                log_test_framework(self.TAG, "Cannot find contact. Add contact from dialer failed")
                return False
    
    
    def add_contact_from_calllog(self, name='', number=''):
        """
        This function is to add contact from Call log
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: none
        """
        '''
        call back from history
        '''
        try:
            log_test_framework(self.tag, 'Start to dial time :')
            Phone().go_home()
            click_button_by_id("floating_action_button")
            Phone().phone_call(number, "", 0, float(SC.PRIVATE_PHONE_CALL_TIME))
            #modified by c_yazli
            if search_view_by_id("floating_end_call_action_button"):
                click_button_by_id("floating_end_call_action_button")
        except Exception as e:
            log_test_framework(self.tag, e)
            take_screenshot()
            set_cannot_continue()
        sleep(5)
        click_imageview_by_desc('More options')
        click_textview_by_text('Call History')
        click_textview_by_text('All')
        click_textview_by_id('filter_sub_spinner')
        sleep(1)
        click_textview_by_text('ALL SIMS')
        click_textview_by_id('filter_status_spinner')
        sleep(1)
        click_textview_by_text('ALL CALLS')
        if search_text(number) :
            log_test_framework(self.TAG, "Exist a recorder we wanted")
            click_imageview_by_desc(number)
            func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'menu_edit')))
            if wait_for_fun(func, True, 5):
                click_textview_by_id('menu_edit')
                click_textview_by_text('Create new contact', isScrollable=0)
                click_textview_by_id('account_type')
                sleep(1)
                click_textview_by_text('PHONE')
        
                if name == '':
                    pass
                else:
                    entertext_edittext_by_index(0, name)
                click_imageview_by_desc('Done')
            else:
                take_screenshot()
        else:
            take_screenshot()
    
    def dial_call(self, number, name):
        """
        This function is to make a call from contact
        @type  name: string
        @param name: name
        @type  number: number
        @param number: phone number

        @return: boolean value
        """
        click_imageview_by_id("dialButton")
        sleep(5)
        if search_text('Mobile network not available'):
            return False
        # whether get throught.
        phoneOn = False
        t = 0
        while search_view_by_id("endButton") and t < 10:
            if search_text("0:", searchFlag=TEXT_CONTAINS):
                phoneOn = True
                # click_button_by_id("audioButton")
                # sleep(3)
                break
            sleep(1)
            t = t + 1
        if phoneOn == False:
            return False
        else:
            return True
        
    def edit_contact_phone(self, name, emailaddr_sequence, emailaddr, location_address_sequence, location_address):
        """
        This function is to edit a contact which have been saved in phone
        """
        array_key = {'EMAIL':'Email', 'ADDRESS':'Address'}
        click_textview_by_text(name)
        if is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'menu_edit', isScrollable=0):
            click_textview_by_id('menu_edit')
            
            for key in array_key:
                sleep(2)
                click_button_by_text('Add another field')
                if search_text(key, isScrollable=0):
                    click_textview_by_text(array_key[key])
                    if array_key[key] == 'Email':
                       ime1 = IME()
                       ime1.IME_input(1, emailaddr_sequence, 'p')
                    #if array_key[key] == 'Address':
                    elif array_key[key] == 'Address':
                        ime1.IME_input(1, location_address_sequence, 'p')
                    sleep(2)  
                else:
                    goback()
                    sleep(10)
                    if key == 'EMAIL':
                        entertext_edittext_by_index(5, emailaddr)
                    elif key == 'ADDRESS':
                        entertext_edittext_by_index(6, location_address)
            click_imageview_by_id('save_menu_item')
        sleep(2)
        if search_text(name) and  search_text(emailaddr) and search_text(location_address):
            log_test_framework(self.TAG, "Email field added succeed")
            return True
        else:
            log_test_framework(self.TAG, 'Email field added failed')
            take_screenshot()
            return False
        
    def edit_contact_sim(self, name, emailaddr_sequence, emailaddr):
        """
        This function is to edit a contact which have been saved in sim1
        """
        click_textview_by_text(name)
        if is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'menu_edit', isScrollable=0):
            click_textview_by_id('menu_edit')
            if search_text('EMAIL'):
                log_test_framework(self.TAG, "Directly edit EMAIL String")
                entertext_edittext_by_index(3, emailaddr_sequence)
                # click btn done
                click_imageview_by_id('save_menu_item')
            else :
                if search_text('Add another field'):
                    log_test_framework(self.TAG, "Add email field via press button to add")
                    click_button_by_text('Add another field')
                    click_textview_by_text('Email')
                    ime1 = IME()
                    ime1.IME_input(1, emailaddr_sequence, 'p')
                    click_imageview_by_id('save_menu_item')
        sleep(2)
        if search_text(name) & search_text(emailaddr):
            log_test_framework(self.TAG, "Email field added succeed")
            return True
        else:
            log_test_framework(self.TAG, 'Email field added failed')
            take_screenshot()
            return False       
    
    def share_contact_mms(self, name):
        """
        This function is to share contact via mms
        """
        share_flag = False
        click_textview_by_text(name)
        send_key(KEY_MENU)
        str = 'Share'
        if search_text(str):
            click_textview_by_text(str)
            sleep(1)
            if  search_text('Messaging', isScrollable=1, searchFlag=TEXT_CONTAINS):
                scroll_to_bottom()
                click_textview_by_text('Messaging', waitForView=1, searchFlag=TEXT_MATCHES)
                waitActivity = lambda:get_activity_name().startswith("com.android.mms.ui.ShareVCardActivity")
                if search_text('New message', searchFlag=TEXT_MATCHES):
                    entertext_edittext_by_index(0, '10086')
                    sleep(1)
                    click_textview_by_text('Type message')
                    # ime1.IME_input_english(1, 'share contact vcard via mms', 'c')
                    entertext_edittext_by_index(1, 'share contact vcard via mms')
                    sleep(1)
                    if search_view_by_id('send_button_mms'):
                        print "share_contact_mms: find send_button_mms"
                    else:
                        print "share_contact_mms: cannot find send_button_mms"
                    click_textview_by_id('send_button_mms')
                    start_time = int(time.time())
                    while int(time.time()) - start_time < 30:
                        if search_text('Sent') | search_text('SENDING') :
                            log_test_framework(self.TAG, 'VCard have sharing/shared out via MMS')
                            share_flag = True
                            break
                        sleep(0.5)
                    
            else:
                log_test_framework(self.TAG, 'Share option have not include message choice')
                
        else :
            log_test_framework(self.TAG, 'Contact father view menu have not include share choice')
                
        return share_flag
    
    def export_contact_to_sim1(self):#c_caijie
        """
        This function is to export phone contact to sim1
        """
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Import/export')
        sleep(3)
        click_textview_by_text('Export to SIM card')
        sleep(3)
        click_checkbox_by_id('selection_menu')
        sleep(5)
        click_textview_by_text("Select all")
        sleep(3)
        click_textview_by_text("Ok")
        sleep(180)

    

    def call_after_add_one_contact(self):
        """
        This function try call after add one.
        @return: none
        """

        # log_test_case(self.name, 'call_from_contact')
        click_textview_by_id('primary_action_view')
        return

    #def add_contact_from_setting_config(self):
        """
        This function try add one from setting config xml.
        the setting module can create common.py from config.xml
        and then using the common.py
        @return: none
        """

        #name = SC.PRIVATE_CONTACT_NAME
        #number = SC.PRIVATE_CONTACT_NUMBER
        #self.add_contact_to_sim_card(name, number)
        #return
    
    def add_contact_into_phone(self, name, number):
        """
        This function try add one from setting config xml.
        the setting module can create common.py from config.xml
        and then using the common.py
        @return: none
        """
        return self.add_contact_to_phone(name, number)
    
    def add_contact_into_sim(self, name, number, sim_number):
        """
        This function try add one from setting config xml.
        the setting module can create common.py from config.xml
        and then using the common.py
        @return: none
        """
        return self.add_contact_to_sim(name, number, sim_number)
    '''
    def edit_contact_phone(self,name,emailaddr):
        """
        This function try add one from setting config xml.
        the setting module can create common.py from config.xml
        and then using the common.py
        @return: none
        """
        return self.edit_contact_phone(name,emailaddr)
    '''
    
    def del_one_contact(self, contact_name):#c_caijie
        """
        This function del one contact record
        @return:  none
        """
        if search_text(contact_name):
            click_textview_by_text(contact_name)
            sleep(3)
            click_imageview_by_desc('More options')
            sleep(3)
            click_textview_by_text("Delete")
            sleep(3)
            if search_text("OK"):
                click_button_by_text("OK")
                sleep(5)
            if search_view_by_id("button1"):
                click_button_by_id("button1")
                sleep(5)    
            return True
        else:
            return False
        
    def del_all_contact(self):#c_caijie
        """
        This function del all contact records
        @return:  none
        """
        click_textview_by_text('deall',clickType=LONG_CLICK)
        sleep(5)
        click_button_by_id('selection_menu')
        sleep(5)
        click_textview_by_text('Select all')
        sleep(5)
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Delete')
        sleep(5)
        click_button_by_text('OK')
        sleep(180)

        
    # added by zhiyangz  
    def clear_contact(self):
        """
        This function del all contact records
        @return:  none
        """
        
        if search_text('No contacts'):
            log_test_framework(self.TAG, "Empty contact")
            return True
               
        send_key(KEY_MENU)
        delstr = 'Delete'
        if search_text(delstr):
            click_textview_by_text(delstr)
            click_checkbox_by_id('select_all_check')
            click_button_by_text('OK')
            click_button_by_text('OK')
            if wait_for_fun(lambda:search_text('Set up my profile'), True, 20):
                    return True
            else:
                return False
        else:
            return False
      
    def call_contact(self, name):
        """
        This function share api for make call from contact
        """
        click_textview_by_text(name)
        log_test_framework(self.TAG, "call to " + name)
        click_textview_by_id('header')
        
        sleep(2)
        if search_view_by_id('floating_end_call_action_button'):
            click_imageview_by_desc('End')
            return True
        else:
            take_screenshot()
            if is_view_enabled_by_text(VIEW_BUTTON, 'OK', isScrollable=0):click_button_by_text('OK')
            return False
        
    def add_contact_from_sms(self, name):
        """
        This function share api for others add contact from sms.
        @type  name: string
        @param name: name
      
        @return: none
        """
        add__contact_result = False
        
        #click_textview_by_id('create_new_contact')
        click_textview_by_text('Create new contact')
        sleep(5)
        if search_text('PHONE'):
            click_textview_by_text('PHONE')
            sleep(5)

        
        # click btn done
        click_textview_by_id('menu_save')
        sleep(2)
        if search_text('10086'):
            log_test_framework(self.TAG, "Add contact success. Find in the phone")
            return True
        else:
            log_test_framework(self.TAG, "Add contact failed. Cannot find")
            return False
      
    
    def contact_to_display(self, type='All contacts'):
        """
        This function is to display contact which you wanted type
        @return:  none
        """
        send_key(KEY_MENU)
        sleep(2)
        click_textview_by_text('Contacts to display')
        if search_text(type):
            log_test_framework(self.TAG, str(type))
            click_textview_by_text(type)
        else:
            log_test_framework(self.TAG, "can not find " + str(type) + " in this options choise")
        sleep(1)
        
    def contact_memory_status(self):
        """
        This function is to display contact which you wanted type
        @return:  none
        """
        send_key(KEY_MENU)
        sleep(1)
        click_textview_by_text('Memory status')
        
    def copy_contact_to_sim1(self, contact_name): #c_caijie
        if search_text(contact_name):
            click_textview_by_text(contact_name)
            sleep(3)
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text("Copy to SIM1")
        sleep(3)
        send_key(KEY_BACK)    
        sleep(3) 
        
        
    def copy_contact_to_sim2(self, contact_name): #c_caijie
        if search_text(contact_name):
            click_textview_by_text(contact_name)
            sleep(3)
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text("Copy to SIM2")
        sleep(3)
        send_key(KEY_BACK)    
        sleep(3)    
        
    def import_contact_from_sim1(self):#c_caijie
        """
        This function is to import  contact from sim1 
        """
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Import/export')
        sleep(3)
        click_textview_by_text('Import from SIM card')
        sleep(3)
        if search_text('PHONE'):
            click_textview_by_text('PHONE')
            sleep(5)     
        click_button_by_id('selection_menu')
        sleep(5)
        click_textview_by_text("Select all")
        sleep(5)
        click_textview_by_text("Ok")
        sleep(3)
        click_button_by_text("OK")
        sleep(180)  
        

    def export_contact_to_sim2(self):#c_caijie
        """
        This function is to export phone contact to sim1
        """
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Import/export')
        sleep(3)
        click_textview_by_text('Export to SIM card')
        sleep(3)
        click_textview_by_text('Export to SIM card: SIM2')
        sleep(3)
        click_button_by_text("OK")
        sleep(5)
        click_checkbox_by_id('select_all_check')
        sleep(5)
        click_button_by_text("OK")
        sleep(120)        
               
    def import_contact_from_sim2(self):#c_caijie
        """
        This function is to import  contact from sim1 
        """
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Import/export')
        sleep(3)
        click_textview_by_text('Import from SIM card')
        sleep(3)
        click_textview_by_text('Import from SIM card: SIM2')
        sleep(3)
        click_button_by_text("OK")
        sleep(5)     
        click_checkbox_by_id('select_all_check')
        sleep(5)
        click_button_by_text("OK")
        sleep(5)
        click_button_by_text("OK")
        sleep(120)   
        
    def search_and_delete(self, contact_name):#c_caijie
        click_textview_by_id("menu_search")
        sleep(2)
        entertext_edittext_on_focused(contact_name)
        sleep(5)
        click_textview_by_id("cliv_name_textview")
        sleep(2)
        click_imageview_by_desc("More options")
        sleep(2)
        click_textview_by_text("Delete")
        sleep(3)
        if search_text("OK"):
            click_textview_by_text("OK")
        send_key(KEY_BACK)
        sleep(2)      
        
        
    def share_visible_contacts(self):#c_caijie
        click_imageview_by_desc("More options")
        sleep(2)
        click_textview_by_text("Import/export")
        sleep(3)
        click_textview_by_text("Share visible contacts")
        sleep(3)
        click_checkbox_by_id("select_all_check")
        sleep(3)
        click_button_by_id("btn_ok")
        sleep(3)
     
     
    def add_contact_to_family_group(self):
        click_textview_by_text("GROUPS")
        sleep(3)
        click_textview_by_text("Family")
        sleep(3)
        click_imageview_by_desc("More options")
        sleep(2)
        click_textview_by_text("Edit")
        sleep(3)
        click_imageview_by_id("addGroupMember")
        sleep(2)
        click_button_by_id("selection_menu")
        sleep(2)
        click_textview_by_text("Select all")
        sleep(3)
        click_textview_by_id("btn_ok")
        if wait_for_fun(lambda:search_view_by_id("save_menu_item"), True, 10):
            click_imageview_by_id("save_menu_item") 
            
            
    def set_contact_photo_take_photo(self,contact_name):
        click_textview_by_text(contact_name)
        if wait_for_fun(lambda:search_view_by_id("menu_edit"), True, 5):
            click_textview_by_id("menu_edit")
            sleep(2)
            click_imageview_by_id("photo_icon")
            sleep(2)
            click_textview_by_text("Take photo")
            if wait_for_fun(lambda:search_view_by_id("shutter_button"), True, 10):
                click_imageview_by_id("shutter_button")
                if wait_for_fun(lambda:search_view_by_id("btn_done"), True, 5):
                    click_imageview_by_id("btn_done")
                    if wait_for_fun(lambda:search_view_by_id("filtershow_done"), True, 5):
                        click_textview_by_id("filtershow_done")
                        if wait_for_fun(lambda:search_view_by_id("menu_save"), True, 5):
                            click_textview_by_id("menu_save")
                            sleep(2)
                            
    def add_contact_to_coworkers_group(self):
        click_textview_by_text("GROUPS")
        sleep(3)
        click_textview_by_text("Coworkers")
        sleep(3)
        click_imageview_by_desc("More options")
        sleep(2)
        click_textview_by_text("Edit")
        sleep(3)
        click_imageview_by_id("addGroupMember")
        sleep(2)
        click_button_by_id("selection_menu")
        sleep(2)
        click_textview_by_text("Select all")
        sleep(3)
        click_textview_by_id("btn_ok")
        if wait_for_fun(lambda:search_view_by_id("save_menu_item"), True, 10):
            click_imageview_by_desc("More options")
            sleep(2)
            click_textview_by_text("Discard changes")
            sleep(3)
            click_button_by_text("OK")   
            
    def delete_contact_all_info(self,contact_name):
        click_textview_by_text(contact_name)
        if wait_for_fun(lambda:search_view_by_id("menu_edit"), True, 5):
            click_textview_by_id("menu_edit")
            sleep(2)
            click_imageview_by_id("delete_button")
            sleep(2)
            clear_edittext_by_index(0)
            sleep(2)
            click_textview_by_id("menu_save")
            sleep(2)                                                                             