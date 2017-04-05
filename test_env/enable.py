import xml.etree.ElementTree as ET
import sys
import os
from os import path
import string
TEST_SUIT_TAG = 'test_suit_'
rootList = os.listdir("./")
TAG = "enable"

'''change suit 0 or 1'''
arg =  sys.argv[1]
if arg == "0":
    value = 'enable="1"'
    value_want = 'enable="0"'
elif arg == "1":
    value = 'enable="0"'
    value_want = 'enable="1"'
else:
    print "arg enter error."


for suitList in rootList:
    if suitList.startswith(TEST_SUIT_TAG) and path.isdir(suitList):
        childList = os.listdir("./"+suitList+"/")
        for list in childList:
            if list.startswith(suitList + ".xml"):
                p = "./" + suitList + "/"+ list
                try:
                    lines = open(p).readlines()
                    s = ""
                    for line in lines:
                        if value in line:
                            s += line.replace(value, value_want)
			    print "value: " + value + " value_want " + value_want
                            print(list + " have changed.")
                        else:
                            s += line
                    f = open(p,'w')
                    f.write(s)
                    f.close()
                except IOError:
                    print(TAG, 'open file error')
            
            '''change case 0 or 1'''
            if len(sys.argv)==3:
                arg = sys.argv[2]
                if arg == "0":
                    value2 = 'enable="1"'
                    value_want2 = 'enable="0"'
                elif arg == "1":
                    value2 = 'enable="0"'
                    value_want2 = 'enable="1"'
                else:
                    print "arg enter error."
                if list.startswith(suitList + '_case') and list.endswith('.xml'):
                    p = './' + suitList + '/' + list
                    try:
                        lines = open(p).readlines()
                        s = ""
                        for line in lines:
                            if value2 in line:
                                s += line.replace(value2, value_want2)
                                print(list + " have changed.")
                            else:
                                s += line
                        f = open(p,'w')
                        f.write(s)
                        f.close()
                    except IOError:
                        print(TAG, 'open file error')

