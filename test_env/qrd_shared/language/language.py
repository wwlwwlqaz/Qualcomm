from case_utility import *
import xml.etree.ElementTree as ET

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    support the multi-language
#doc:
#   1. if you have set the locael manually, it will not get the system language by socket
############################################
class Language(object):
    _strings = None
    _default_strings = None
    _locale = None
    _is_loaded = False
    _mode_name = None
    _debug = False

    def __init__(self, mode_name):
        self._mode_name = mode_name
        self.debug_print( 'Language init:%f' %(time.time()))

    def debug_print(self,log):
        if self._debug:
            print(self._mode_name, log)

    def get_locale(self):
        return self.__locale

    def set_locale(self,locale):
        if locale == None:
            return
        if self._locale!=None and self._locale != locale:
            #if have _locale values and the _locale is not equal with the locale,
            #reset the resource variable
            self._strings = None
            self._default_strings = None
            self._is_loaded = False
        self._locale = locale

    def __load(self):
        if self._locale == None:
            try:
                self.debug_print( 'get system language')
                self._locale = get_system_language()
            except:
                self.debug_print( 'Warning: Can not get the system language by socket')
                self._locale = 'en'
                #use the default result
        default_path = './qrd_shared/'+self._mode_name+'/res/values/strings.xml'
        default_root_element = self.__parse_file(default_path)
        if default_root_element != None:
            self.debug_print( 'parse _default_strings')
            self._default_strings = default_root_element.findall('string')
        #load the language result
        self._strings = None
        if self._locale != None and self._locale != '':
            lan_path = './qrd_shared/'+self._mode_name+'/res/values_'+self._locale+'/strings.xml'
            root_element = self.__parse_file(lan_path)
            if root_element != None:
                self.debug_print( 'parse _strings')
                self._strings = root_element.findall('string')
        self._is_loaded = True

    #get value from the resource
    def get_value(self,key):
        if key==None or key == '':
            return None
        if not self._is_loaded:
            #load the language to memory
            self.__load()
        if self._strings == None:
            #if the _string is null , will find the key in the default resource
            return self.__find_diff_key(self._default_strings,key)
        result = self.__find_diff_key(self._strings,key)
        if result == None:
            #if can not find the string in the language resource ,
            #will try to find in the detault resource
            self.debug_print('read the resource from the default resrouce')
            return self.__find_diff_key(self._default_strings,key)
        return result

    #fine the key in the specified strings
    def __find_key(self,strings,key):
        if strings == None:
            return None
        for string in strings:
            if string.attrib.get('name') == key:
                return string.text
        return None

    #parse the file to xml document
    def __parse_file(self,path):
        root_element = None
        if os.path.exists(path) == True:
            try:
                tree = ET.parse(path) #open the xml file
                root_element = tree.getroot() #get the root element
            except Exception, e:
                self.debug_print( 'Can not parse the resource file: '+path)
        else:
            self.debug_print( 'not exist:'+path)
        return root_element

    def getValByCurRunTarget(self,key):
        if key==None or key == '':
            return None
        if not self._is_loaded:
            #load the language to memory
            self.__load()
        if self._strings == None:
            #if the _string is null , will find the key in the default resource
            return self.__find_diff_key(self._default_strings,key)
        result = self.__find_diff_key(self._strings,key)
        if result == None:
            #if can not find the string in the language resource ,
            #will try to find in the detault resource
            self.debug_print('read the resource from the default resrouce')
            return self.__find_diff_key(self._default_strings,key)
        return result

    def __find_diff_key(self,strings,key):
        import settings.common as SC
        if strings == None:
            return None
        for string in strings:
            if string.attrib.get('name') == key:
                if string.attrib.get('platform') == SC.PUBLIC_PHONE_PLATFORM_TYPE:
                    return string.text
        if string.text != None:
            for string in strings:
                if string.attrib.get('name') == key:
                    if string.attrib.get('platform') != SC.PUBLIC_PHONE_PLATFORM_TYPE:
                        if string.attrib.get('platform') is None:
                            return string.text
        return None