import xml.etree.ElementTree as ET
import sys
from platform_check import get_platform_info
import os
from system_capacity import get_property
import re

TAG = 'update'
global FILE_PATH_COMMON
global FILE_PATH_CONFIG

def init_filepath():
    global FILE_PATH_COMMON
    global FILE_PATH_CONFIG
    osInfo = get_platform_info()
    currLocation = os.getcwd()
    if(osInfo == 'Linux-Phone' or osInfo == 'Linux-PC'):
        FILE_PATH_COMMON = currLocation + '/settings/common.py'
        FILE_PATH_CONFIG = currLocation + '/settings/config.xml'
    elif(osInfo == 'Windows'):
        FILE_PATH_COMMON = currLocation + '\\settings\\common.py'
        FILE_PATH_CONFIG = currLocation + '\\settings\\config.xml'

def update():
    init_filepath()
    reload(sys)
    sys.setdefaultencoding("utf-8")
    try:
        output = open(FILE_PATH_COMMON, 'w')
    except IOError:
        print(TAG, 'open common.py error')
    tree = ET.parse(FILE_PATH_CONFIG)
    root = tree.getroot()
    output.write("#coding=utf-8\n")
    #write log path
    output.write("PUBLIC_LOG_PATH = '/sdcard/com.android.qrdtest'" + '\n')
    for child in root.findall('public'):
        if child.get('type') == 'string' or child.get('type') == 'number' or child.get('type') == 'file_path' or child.get('type') == 'simple-select' or child.get('type') == 'multi-select':
            if child.text == None:
                public = "PUBLIC_" + child.get("name").upper() + " = ''\n"
            else:
                public = "PUBLIC_" + child.get("name").upper() + " = '" + child.text + "'\n"
        elif child.get('type') == 'boolean':
            if child.text.lower() == 'true':
                public = "PUBLIC_" + child.get('name').upper() +  " = True\n"
            else:
                public = "PUBLIC_" + child.get('name').upper() +  " = False\n"
        if child.get('type') == 'sequence':
            public = "PUBLIC_" + child.get('name').upper() +  " = " + get_sequence(child) + "\n"
        output.write(public)

    for child in root.findall('private'):
        prefix = 'PRIVATE_' + child.get('name').upper() + "_"
        for item in child.findall('item'):
            if item.get('type') == 'string' or item.get('type') == 'number' or item.get('type') == 'file_path' or item.get('type') == 'simple-select' or item.get('type') == 'multi-select':
                if item.text == None:
                    private = prefix + item.get('name').upper() + " = ''\n"
                else:
                    private = prefix + item.get('name').upper() + " = '" + item.text + "'\n"
            elif item.get('type') == 'boolean':
                if item.text.lower() == 'true':
                    private = prefix + item.get('name').upper() +  " = True\n"
                else:
                    private = prefix + item.get('name').upper() +  " = False\n"
            if item.get('type') == 'sequence':
                private = prefix + item.get('name').upper() + " = " + get_sequence(item) + "\n"
            output.write(private)
    output.close()

def get_sequence(item):

    #write the predefine input seq variable
    seq_input = "["
    input_seq_list = item.text.split(',')
    seq_content = ""

    for i in range(0,len(input_seq_list)):
        if i != 0 :
            seq_content = seq_content + ","
        seq_content = seq_content + "'" + input_seq_list[i] + "'"

    input_seq = seq_input + seq_content + "]"
    return input_seq

def auto_match_platform():
    '''
    This function used to auto write phone software version into common.
    @return: null
    '''
    sw_version = get_property("ro.product.model").strip()

    f = open(FILE_PATH_COMMON, 'rb')
    lines = f.readlines()
    newLines = ''
    for line in lines:
        if line.find("automatch") >= 0:
            line = "PUBLIC_PHONE_PLATFORM_TYPE = '" + sw_version + "'\n"
        newLines += line
    f.close()
    f = open(FILE_PATH_COMMON, 'wb')
    f.write(newLines)
    f.close()


def reset_disable_touchpanle_setting():
    global FILE_PATH_CONFIG
#    init_filepath()
#    root = ET.parse(FILE_PATH_CONFIG)
#    node_find = root.find("public/[@name='disable_TouchPanel']")

    tree=ET.parse(FILE_PATH_CONFIG)
    root=tree.getroot()
    for child in root.findall('public'):
        if child.get('name')=='disable_TouchPanel':
            child.text='false'
    tree.write(FILE_PATH_CONFIG)

