from qrd_shared.language.language import Language
import time
############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    the base class of the reuse library
############################################
class Base(object):
    _debug = False
    def __init__(self,mode_name):
        self.mode_name = mode_name
        self.language = Language(self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))

    #get value from the model language resource
    def get_value(self,key):
        result = self.language.get_value(key);
        return result

    def getValByCurRunTarget(self,key):
        result = self.language.getValByCurRunTarget(key);
        return result

    #print the log is the value of the debug variable is true
    def debug_print(self,log):
        if self._debug:
            print(self.mode_name, log)