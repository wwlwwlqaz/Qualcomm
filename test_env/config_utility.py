#coding=utf-8
'''
   config utility for qsst configuration

   1.The api provided is used to get the configuration values from the comman.py module.

   2.This module also provide for the other application to get the configuration values.
   such as :
       python /data/test_env_xxx/config_utility.py  random_order gmail.gmail_account

   if the configuration item is public,you can only give the key name, such as "random_order".
   but if it is private , need to give a module name and the key name , such as: gmail.gmail_account.

   3.You can give multiple keywords in one-time. And the result like this:
        random_order:False
        gmail.gmail_account:autotest55@gmail.com
   Client need go through each line , and split it with ":",
   the font part is the keywords in the arguments, the latter part is the value of the configuration.

   Notice: a.Client can not identify success or failure via the process return code.
   because, only when client haven`t passed any keyword to this script, the process will return -1 .
   Otherwise always return 0, evan some of the configuration values can not get.
   b.the error message will write to the stderr stream , and the result will write to the sdtout stream.
   so if the client can not find the value of the keyword fromt he sdtout stream, can get the message from the sdterr for analyzing the reason.

   4.If you want to add some common functions for the qsst configuration ,
   you an add here

   @author: U{c_lqiang<c_lqiang@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @note:
   @attention:
   @bug:
   @warning:



'''
import sys
import os
import traceback

def getConfigValue(moduleName,keyName):
    '''
    get the configuration value of the key in the module. moduleName can be empty

    @type moduleName: name of the module
    @param keyName: name of the key
    '''
    #update the setting, make sure the config is the newest
    import settings.update as SU
    SU.update()
    import settings.common
    attrName = ""
    if moduleName==None or moduleName=="":
        attrName = "PUBLIC_"+keyName.upper()
    else:
        attrName = "PRIVATE_"+moduleName.upper()+"_"+keyName.upper()
    try:
        result = getattr(settings.common, attrName)
        return result
    except Exception as e:
        return ""

if __name__ == '__main__':
    argLen = len(sys.argv)
    if argLen >= 2:
        #if the arg is more than 2 .
        l = len("config_utility.py")
        os.chdir(sys.argv[0][0:-l])
        keys = []
        #get the keys in the argvs
        for index in range(1,argLen):
            keys.append(sys.argv[index])
        #go through all the key
        for key in keys:
            moduleName = ""
            keyName = ""
            # get the module name and the key name
            moduleAndKey = key.split('.')
            moduleAndKeyLen = len(moduleAndKey)
            if moduleAndKeyLen == 2:
                moduleName = moduleAndKey[0]
                keyName = moduleAndKey[1]
            else:
                keyName = moduleAndKey[0]
            #check the key name. must have the key name
            if keyName==None or keyName == "":
                sys.stderr.write("'"+key+"' is a invalid key.\n")
                continue
            configValue = getConfigValue(moduleName, keyName)
            #convert to string
            valueStr = str(configValue)
            if valueStr == None or valueStr == "":
                reason = "Can not find "+keyName
                if moduleName !="":
                    reason = reason+" of "+moduleName +" module"
                sys.stderr.write(reason+" in the configure\n")
            else:
                sys.stdout.write(key+":"+valueStr+"\n")
        exit(0)
    else:
        sys.stderr.write("please give me some keys\n")
        exit(-1)

