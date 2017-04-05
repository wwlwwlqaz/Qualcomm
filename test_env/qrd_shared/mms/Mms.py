# coding=utf-8
'''
   provide some interface of mms application.

   This class will provide operations api of mms application.

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
from __builtin__ import True
from pickle import TRUE
class Mms(Base):
    '''
    Mms is a class for operating Mms application.

    @see: L{Base <Base>}
    '''
    TAG = "Mms"
    '''@var TAG: tag of Mms'''
    def __init__(self):
        '''
        init function.
        '''
        self.mode_name = "mms"
        self.ime = IME()
        Base.__init__(self, self.mode_name)
        self.debug_print('Mms init:%f' % (time.time()))

    def click_home_icon(self):
        '''
        click home icon.

        @return: true-if click success.false-if click failed.
        '''
        if wait_for_fun(lambda:search_view_by_id("home"), True, 10):
            click_imageview_by_id("home")
            return True
        log_test_framework(self.TAG, "Can't search view 'home'.")
        return False
    
    def go_home(self):
        for i in range(10):
            flag1 = is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Messaging', isScrollable=0, searchFlag=TEXT_MATCHES)
            '''
            @attention: modify by min.sheng , change content of flag2
            '''
            #flag2 = search_view_by_id("list")
            #flag3 = search_view_by_id("empty")
            #flag2 = is_view_enabled_by_id(VIEW_BUTTON, 'floating_action_button', isScrollable=0)
            flag2 = is_view_enabled_by_id(VIEW_BUTTON, 'action_compose_new', isScrollable=0)
            '''try:scroll_to_bottom()
            except:pass'''
            
            if flag1 & flag2 : 
                return True
            else: 
                log_test_framework(self.TAG, "not find message home flag")
                goback()
            sleep(1)
        
        return False
        

    def delete_all_threads(self):#c_caijie
        '''
        delete all threads.
        '''
        click_textview_by_id('from',clickType=LONG_CLICK)
        sleep(2)
        click_button_by_id('selection_menu')
        sleep(5)
        click_textview_by_text('Select all')
        sleep(5)
        click_textview_by_id('delete')
        sleep(5)
        click_button_by_index(1)
        sleep(60)

    def send_sms(self, number, content):#c_caijie
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(5)         
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_by_id('recipients_editor',number)
        sleep(5)
        send_key(KEY_ENTER)
        sleep(5)        
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',content)
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)


    
    
    def clear(self, clearType):
        tag = 'clear(%s)' % clearType
        
        if clearType is 'draft':
            while is_view_enabled_by_text(VIEW_TEXT_VIEW, 'Draft', searchFlag=TEXT_CONTAINS):
                log_test_framework(tag, 'have draft.clearing...')
                click_textview_by_text('Draft', searchFlag=TEXT_CONTAINS)                
                # click_menuitem_by_text('Discard',isScrollable=0)
                try:click_menuitem_by_text('Discard', isScrollable=0)
                except:
                    goback()
                    try:clear_edittext_by_id('embedded_text_editor', isScrollable=0)
                    except:pass
                    try:click_button_by_id('remove_image_button', isScrollable=0, waitForView=1)
                    except:pass
                    try:click_button_by_id('remove_slideshow_button', isScrollable=0)
                    except:pass
                    try:clear_edittext_by_id('subject', isScrollable=0)
                    except:pass
                    try:click_textview_by_id('recipients_editor', isScrollable=0)
                    except:pass

                
        elif clearType is 'error':
            while is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'error', isScrollable=1):
                log_test_framework(tag, 'have error.clearing...')
                click_imageview_by_id('error', isScrollable=0)
                click_menuitem_by_text('Discard', isScrollable=0)
                
                goback()
                
        else:
            log_test_framework(tag, 'cannot clear...clearType is wrong')
            pass
        
        
    def exist(self, msgType=''):
        tag = 'exist(%s)' % msgType
        
        if search_text('No conversations', isScrollable=0):
            log_test_framework(tag, 'no conversations')
            return False
        elif msgType is '':return True
        elif msgType is 'mms':
            pass
            return True

    def number(self, thread=''):
        tag = 'number(%s)' % thread
        
        drag_by_param(50, 30, 50, 80, 20)
        
        if '' == thread:
            head = get_view_text_by_id(VIEW_TEXT_VIEW, 'from', isScrollable=0).decode('utf-8')
        
        else:
            drag_by_param(50, 20, 50, 80, 10)
            thread = str(thread)
            left = '.*' + thread[0:3] + '\s?' + thread[3:7] + '\s?' + thread[7:11] + '.*'
            head = get_text(left, isScrollable=1, searchFlag=TEXT_MATCHES_REGEX)
            if head is '':
                log_test_framework(tag, 'cannot find thread = ' + thread)
                n = 0
                return (n, thread, left)  # left should be 'NULL'??
    
        import re
        if re.search(u'\xa0', head):
            [left, right] = head.split(u'\xa0')
            n = re.search('\d+', right).group()
            n = int(n)
        else:
            left = head
            # thread = s
            n = 1  # n = '1'
            
        thread = left.replace(u' ', u'')  # remove all space
        thread = thread.replace(u'+86', u'')
        
        log_test_framework(tag, 'thread = ' + thread)
        log_test_framework(tag, 'n = ' + str(n))
    
        # n = int(n)
        log_test_framework(tag, 'end')
        return (n, thread, left)
            
    #added by c_yazli
    def attach_capture_video(self,videotime,size_flag=0):
        click_imageview_by_desc('Attach')
        sleep(3)
        click_textview_by_text('Capture video')
        sleep(5)
        'add if '
        if search_text("JUST ONCE"):
            click_textview_by_text("JUST ONCE")
            sleep(2)
        drag_by_param(538, 57, 538, 1457, 200)
        sleep(2)
        click_imageview_by_desc('Shutter')
        sleep(videotime)
        func_shutter = lambda:search_view_by_id('shutter_button')
        if wait_for_fun(func_shutter, True, 10):   
            click_imageview_by_id('shutter_button')
        sleep(2)
        #if search_view_by_id('btn_done'):
        if search_view_by_id('btn_done'):
            click_imageview_by_id('btn_done')
            sleep(1)
            log_test_framework(self.TAG, "attach captured video successfully")
            return True
        elif search_view_by_id('done_button'):
            click_imageview_by_id('done_button')
            sleep(1)
            log_test_framework(self.TAG, "attach captured video successfully")
            return True
        else:
            log_test_framework(self.TAG, "Fail to attach captured video ")
            return False
        
    def attach_capture_video_oversize(self,videotime=20,size_flag=0):
        click_imageview_by_desc('Attach')
        sleep(3)
        click_textview_by_text('Capture video')
        sleep(5)
        'add if '
        if search_text("JUST ONCE"):
            click_textview_by_text("JUST ONCE")
            sleep(2)
        drag_by_param(538, 57, 538, 1457, 200)
        sleep(2)
        for i in range(0, 10):
            click_imageview_by_desc('Shutter')
            sleep(videotime)
            if not (search_view_by_id('btn_done') or search_view_by_id('done_button')):
                log_test_framework(self.TAG, "File does not exceed the size")
                click_imageview_by_desc('Shutter')
                sleep(2)
                if search_view_by_id('btn_done'):
                    click_imageview_by_id('btn_done')
                    sleep(2)
                elif search_view_by_id('done_button'):
                    click_imageview_by_id('done_button')
                    sleep(2)
                click_imageview_by_desc('Attach')
                sleep(3)
                click_textview_by_text('Capture video')
                sleep(5)
                if search_text("JUST ONCE"):
                    click_textview_by_text("JUST ONCE")
                    sleep(2)
                drag_by_param(538, 57, 538, 1457, 200)
                sleep(2)
                continue
            else:
                log_test_framework(self.TAG, "File is  exceed the size ")
                return True
        
    def attach_audio(self,audioname):
        click_imageview_by_desc('attach')
        click_textview_by_text('Audio')
        click_textview_by_text('System audio')
        #if search_view_by_desc('Media Storage'):
        if search_text('Media Storage'):
            click_textview_by_text('Media Storage')
            
        if search_text('JUST ONCE'):
            sleep(2)
            click_textview_by_text('JUST ONCE')
        sleep(1)
        click_textview_by_text(audioname) 
        sleep(1)
        if search_text("OK"):
            click_textview_by_text("OK")
            sleep(1)
            log_test_framework(self.TAG, "attach audio successfully")
            return True
        else:
            log_test_framework(self.TAG, "Fail to attach system audio ")
            return False
        
    def attach_record_audio(self,audiotime):#c_caijie
        click_imageview_by_desc('attach')
        click_textview_by_text('Record audio')
        sleep(1)        
        click_button_by_id('recordButton')
        sleep(1)
        if search_view_by_id('permission_allow_button'):
            click_button_by_id('permission_allow_button')
            sleep(5)
            if search_view_by_id('permission_allow_button'):                
                click_button_by_id('permission_allow_button') 
                sleep(5)                
        click_button_by_id('stopButton')
        sleep(3)
        click_button_by_id('acceptButton')
        sleep(3)
        if search_view_by_id('permission_allow_button'):
            click_button_by_id('permission_allow_button')
            sleep(5)
            if search_view_by_id('permission_allow_button'):                
                click_button_by_id('permission_allow_button') 
                sleep(5) 
        if search_view_by_id('button1'):
            click_button_by_id('button1')
            sleep(2)
            log_test_framework(self.TAG, "attach record_audio successfully")
            return True
        else:
            log_test_framework(self.TAG, "Fail to attach record_audio ")
            return False
    
    def add_picture(self):#c_caijie
        '''
        add picture from storage
        @author: min.sheng
        '''
        click_imageview_by_desc('Attach')
        sleep(3)
        click_textview_by_text("Capture Picture")
        if wait_for_fun(lambda:search_view_by_id("permission_allow_button"), True, 8):
            click_button_by_id('permission_allow_button')
        if wait_for_fun(lambda:search_text("OK"), True, 5):
            click_textview_by_text("OK")          
        if wait_for_fun(lambda:search_view_by_id('shutter_button'), True, 10):
            click_button_by_id('shutter_button')
            sleep(3)
            if wait_for_fun(lambda:search_view_by_desc("Review done"), True, 10):
                click_imageview_by_desc("Review done")
            elif wait_for_fun(lambda:search_view_by_id('btn_done'), True, 10):
                click_imageview_by_id("btn_done")
            #click_textview_by_id("menu_list")
            #sleep(3)
            #click_textview_by_text("temp.jpg", searchFlag=TEXT_CONTAINS)
            #sleep(2)

    def add_subject(self,subjectString):
        send_key(KEY_MENU)
        sleep(1)
        click_textview_by_text("Add subject")
        sleep(1)
        click_textview_by_text("Subject")
        sleep(1)
        self.ime.IME_input(1, subjectString)
        sleep(1)
    
    def add_content(self): 
        click_textview_by_text("Type message")
        entertext_edittext_on_focused("DEVCI test")
        #self.ime.IME_input_english(1, "DEVCI test")
        sleep(1) 
         
    def add_recipient(self,recipientname):#c_caijie
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_on_focused(recipientname)
        sleep(5)
        send_key(KEY_ENTER)
        sleep(3)
    '''
    @attention: add by min.sheng 
    check the mms app
    '''
    def check_default_mms_app(self):
        if search_view_by_id("banner_sms_promo_title"):
           log_test_framework(self.TAG, "need to choose mms app") 
           send_key(KEY_MENU)
           click_textview_by_text("Settings")
           sleep(1)
           click_textview_by_text("SMS Disabled")
           click_button_by_text("Yes")
        else:
            pass
        
    def save_draft(self):#c_caijie
        '''
        use slot1 or slot2 to send a sms to a specific phone number,then check whether send success.

        @type send_slot_number: number
        @param send_slot_number: send slot,1-slot1,2-slot2, 3-default
        @type recive_phone_number: number
        @param recive_phone_number: the phone nunber that recive the message.
        @type content: string
        @param content: text message.
        @return: true-if send success,false-if send failed.
        '''
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(5)         
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_by_id('recipients_editor','18721465130')
        sleep(8)
        send_key(KEY_ENTER)
        sleep(5)        
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor','nosend187')
        sleep(5)
        send_key(KEY_BACK)
        sleep(5)
        send_key(KEY_BACK)
        sleep(5)
        
        
    def search_sms(self, content): #c_caijie        
        click_textview_by_id("search")
        sleep(3)
        entertext_edittext_by_id('search_view',content)
        sleep(8)        
        #click_textview_by_desc('Search')
        #sleep(8)
        
    def sms_signature(self, signature):   #c_caijie      
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text("Text (SMS) messages settings")
        sleep(3)        
        click_textview_by_text("SMS signature disabled")
        sleep(3)
        click_textview_by_text('Edit SMS signature')
        sleep(3)
        entertext_edittext_by_id("edit",signature)
        sleep(5)
        click_button_by_id('button1')
        sleep(3)
        send_key(KEY_BACK)
        sleep(3)   
        send_key(KEY_BACK)
        sleep(3)
        
    def delivery_report(self):      #c_caijie   
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text("Text (SMS) messages settings")
        sleep(3)
        click_textview_by_text('Delivery reports')
        sleep(3)  
        send_key(KEY_BACK)
        sleep(2)
        send_key(KEY_BACK)
        sleep(2)  
          
    def preferred_storage(self, storage):  #c_caijie       
        click_imageview_by_desc('More options')
        if wait_for_fun(lambda:search_text("Settings"), True, 5):
            click_textview_by_text('Settings')
        if wait_for_fun(lambda:search_text("Text (SMS) messages settings"), True, 8):
            click_textview_by_text("Text (SMS) messages settings")
        if wait_for_fun(lambda:search_text("Preferred storage"), True, 5):
            click_textview_by_text('Preferred storage')
            sleep(3)
        click_textview_by_text(storage)
        sleep(5) 
        send_key(KEY_BACK)
        sleep(3)
        send_key(KEY_BACK)
        sleep(3)
  
        
    def set_text_message_limit(self, number): #c_caijie        
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text('Text message limit')
        sleep(5)
        entertext_edittext_by_id("numberpicker_input",number)
        sleep(5)
        click_button_by_id('button1')
        sleep(3)
        send_key(KEY_BACK)
        sleep(3)
        
#     def send_text_message_limit(self):#c_caijie
#         self.send_sms("18721465135", "one")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "two")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "three")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "four")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "five")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "six")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "seven")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "eight")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "nine")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "ten")
#         send_key(KEY_BACK)
#         sleep(3)
#         send_key(KEY_BACK)
#         sleep(3)
#         self.send_sms("18721465135", "eleven")  

    def send_text_message_limit(self):#c_caijie
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(5)         
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_by_id('recipients_editor',"13636583073")
        sleep(5)
        send_key(KEY_ENTER)
        sleep(5)        
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"one")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"two")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"three")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)  
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"four")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"five")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"six")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"seven")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"eight")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"nine")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"ten")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor',"eleven")
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)
                
        
    def restore_default_settings(self):   #c_caijie      
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Restore default settings')
        sleep(8) 
        
    def manage_SIM1_card_message(self):     #c_caijie    
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text("Text (SMS) messages settings")
        sleep(3)
        click_textview_by_text('Manage SIM card messages')
        sleep(3)
   
        
    def send_import_template(self, number):   #c_caijie      
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(5)         
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_by_id('recipients_editor',number)
        send_key(KEY_ENTER)
        sleep(5)
        click_button_by_id("add_attachment_first")
        sleep(3)
        click_imageview_by_id("pager_indicator_second")
        sleep(3)
        if search_text("Import Template", isVerticalList=0, searchFlag=TEXT_CONTAINS): 
            click_textview_by_text("Import Template")
            sleep(2)         
        click_textview_by_text('Please call me later')
        sleep(5)
        click_imageview_by_id('send_button_sms')
        sleep(3)  
        
    def send_add_subject(self, number):    #c_caijie     
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(5)         
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_by_id('recipients_editor',number)
        sleep(8)
        send_key(KEY_ENTER)
        sleep(5)
        click_textview_by_id('embedded_text_editor')
        sleep(3)
        entertext_edittext_by_id('embedded_text_editor','subject')
        sleep(5)        
        click_imageview_by_desc('Attach')
        sleep(3)
        click_textview_by_text('Subject')
        sleep(5)
        click_textview_by_text('Subject')
        sleep(3)
        entertext_edittext_on_focused('subject')
        sleep(10)
        send_key(KEY_ENTER)
        sleep(5)        
        click_imageview_by_id('send_button_sms')
        sleep(3)   
        
    def discard_sms(self, number, content):    #c_caijie     
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(5)         
        click_textview_by_id("recipients_editor")
        sleep(3)
        entertext_edittext_by_id('recipients_editor',number)
        sleep(8)
        send_key(KEY_ENTER)
        sleep(5)
        click_textview_by_id('embedded_text_editor')
        sleep(3)        
        entertext_edittext_by_id('embedded_text_editor',content)
        sleep(8)
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Discard')
        sleep(8)    

    def delivery_report_mms(self):      #c_caijie   
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text("Multimedia (MMS) messages settings")
        sleep(3)
        click_textview_by_text("Delivery reports", searchFlag=TEXT_MATCHES)
        sleep(5)
        send_key(KEY_BACK)
        sleep(2)
        send_key(KEY_BACK)
        sleep(2) 
        
    def add_audio(self,filename):#c_caijie
        click_imageview_by_desc('Attach')
        sleep(3)
        click_textview_by_text("Audio")
        sleep(2)
        click_textview_by_text("External audio")
        sleep(3)
        click_textview_by_text(filename, searchFlag=TEXT_CONTAINS)
        sleep(2)
        click_button_by_text("OK")
        sleep(3)   
        
    def auto_retrieve_mms(self):
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text("Multimedia (MMS) messages settings")
        sleep(3)
        click_textview_by_text('Auto-retrieve')
        sleep(3) 
        send_key(KEY_BACK)
        sleep(2) 
        send_key(KEY_BACK)
        sleep(2)
        
    def forward_sms_saved_in_sim_card(self,phonenumber):#c_caijie
        click_imageview_by_desc('More options')
        sleep(3)
        click_textview_by_text('Settings')
        sleep(3)
        click_textview_by_text("Text (SMS) messages settings")
        sleep(3)
        click_textview_by_text('Manage SIM card messages')
        if wait_for_fun(lambda:search_text("From: 10086"), True, 60):
            #click_textview_by_id("sim_message_address", clickType=LONG_CLICK)
            click_textview_by_text("From: 10086", clickType=LONG_CLICK)
            sleep(3)
        click_textview_by_id("forward")
        sleep(5)
        entertext_edittext_by_id("recipients_editor", phonenumber)
        sleep(3)
        send_key(KEY_ENTER)
        sleep(2)
        click_imageview_by_id('send_button_sms')
        sleep(2) 
        
        
        
    def send_sms_to_multi_recipient(self,content):
        if search_view_by_id('create'):
            click_button_by_id('create')
            sleep(5)
        if  search_view_by_id('action_compose_new'):
            click_button_by_id('action_compose_new') 
            sleep(3)  
        click_button_by_id("recipients_picker")
        if wait_for_fun(lambda:search_view_by_id("selection_menu"), True, 5):
            click_button_by_id("selection_menu")
            if wait_for_fun(lambda:search_text("Select all"), True, 5):
                click_textview_by_text("Select all")
                if wait_for_fun(lambda:search_text("Ok"), True, 5):
                    click_textview_by_id("btn_ok")
                    if wait_for_fun(lambda:search_view_by_id("embedded_text_editor"), True, 10):
                        click_textview_by_id('embedded_text_editor')
                        sleep(3)        
                        entertext_edittext_by_id('embedded_text_editor',content)
                        sleep(5)
                        send_key(KEY_ENTER)
                        sleep(2)
                        click_imageview_by_id('send_button_sms')
                        sleep(2)                                                                                                          