'''
   shared library of gmail module.

   This class will provide operations api for gmail application.

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

class Gmail(Base):
    '''
    Gmail is a class for operating Gmail application.

    @see: L{Base <Base>}
    '''
    def __init__(self):
        '''
        init function.

        @see: L{Base <Base>}
        '''
        self.mode_name = "gmail"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))
        
        

        
            
