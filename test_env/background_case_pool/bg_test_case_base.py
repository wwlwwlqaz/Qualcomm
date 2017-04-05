'''
   Base class of all background case.

   This module defines the life cycle of background test case .
   and it is a thread, that is each background case will run in a new owner thread.
   and makes the case subclass just need to care about the test functions.

   1.run() function is the entry which the test suit will call it .
   In this function , it will call test_case_init() to init some information about this case.
   then, init_thrift_client() function will be called, and create local thrift client to interact with server.
   then, test_case_main() function will be called, and subclasses just need to override it,and do itself things.
   then, close_thriftclient() function will be called, and close the local thrift client.
   last, test_case_end() function will be called, and execute to exit this application.

   2.If you want to add some common function for all the background test case ,
   you can add them here.

   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see: L{bg_test_suit_base<bg_test_suit_base>}
   @note:
   @attention:
   @bug:
   @warning:

'''

from logging_wrapper import log_test_framework
import threading
from utility_wrapper import init_thrift_client,close_thriftclient
class BgTestCaseBase(threading.Thread):
    """Base class for background test case"""

    def __init__(self, name, suit_name, enabled=True):
        threading.Thread.__init__(self)
        self.name = name
        self.suit_name = suit_name
        self.enabled = enabled

    def run(self):
        self.test_case_init()
        #create local thrift client
        init_thrift_client()
        self.test_case_main()
        #close local thrift client
        close_thriftclient()
        self.test_case_end()

    @staticmethod
    def createInstance(class_name, *args, **kwargs):
        '''
        give the class name and the args to create a test instance

        @type class_name: string
        @param class_name: class name of this case
        @type args: reference
        @param args: arguments the case needs
        '''
        (module_name, class_name) = class_name.rsplit('.', 1)
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        o = class_meta(*args, **kwargs)
        return o

    def test_case_end(self):
        '''
        end the test case . save some loggoing.
        '''
        log_test_framework(self.name, 'case end')

    def test_case_init(self):
        '''
        end the test case . save some loggoing.
        '''
        log_test_framework(self.name, 'case init...')

    def test_case_main(self):
        '''
        the subclass need to override this function to do itself things
        '''
        log_test_framework(self.name, 'case run....')