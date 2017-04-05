'''
Configurate QSST in remote control.

``qsstconfig4rc`` provides an interface with blocking features for users to configurate QSST by modifying config.xml in remote control.

@author: U{shibom<shibom@qti.qualcomm.com>}
@version: version 1.0.0
@requires: python 2.7+

here are three examples:
    test case item:
        config_qsst("test_suit_camera.test_suit_camera_case1", 1) # enable test_suit_camera_case1
        config_qsst("test_suit_camera.*", 1)  # enable all cases under the given test_suit_camera
        config_qsst("*.*", 0)  # disable all case under test_env
    public item:
        config_qsst("public.slot2_phone_number_sequence", "num_sign,1,5,6,1,8,7,1,8,1,5,9")

    private item:
        config_qsst("private.browser.address_url", "www.tuzei.net")
'''
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import settings.update as SU
import sys

PUBLIC_ITEM_PREFIX = 'public'
PRIVATE_ITEM_PREFIX = 'private'
FAILED = -1
SUCCEED = 0

import os
ROOT_DIR = os.getcwd()
TEST_SUIT_PREFIX = "test_suit_"
TEST_CASE_TAG = "_case"
XML_SUFFIX = ".xml"
RELATIVE_SUITS_TAG = "relative_suits"
STATUS = {"ENABLE":"1", "DISABLE":"0"}
ALL_SIGN = '*'
ENABLE_TAG = "enable"

# set case status by modifying the case config file.
def set_case_status(filepath, status):
    res = FAILED
    tree = ET.parse(filepath)
    root = tree.getroot()
    _status = root.get(ENABLE_TAG)
    if not _status:
        return res
    if status != _status:
        root.set(ENABLE_TAG, status)
        tree.write(filepath)
    res = SUCCEED
    return res

# get status of the given case
def get_case_status(case_path):
    tree = ET.parse(case_path)
    root = tree.getroot()
    return root.get(ENABLE_TAG)

# get path of the given suit.
def get_suit_path(suitname, root=ROOT_DIR):
    return os.path.join(root, suitname)

# set status of all cases
def traverse_cases(status, root=ROOT_DIR):
    for _file in os.listdir(root):
        _path = os.path.join(root, _file)
        if os.path.isdir(_path) and _file.startswith(TEST_SUIT_PREFIX):
             traverse_cases(status, _path)
        else:
            if _file.startswith(TEST_SUIT_PREFIX) and _path.endswith(XML_SUFFIX):
                set_case_status(_path, status)

# get status of other cases except the given case
def get_other_cases_status_flag(suit_path, suitname, casename, status):
    if status == STATUS["ENABLE"]:
        return False
    for _file in os.listdir(suit_path):
        if _file.startswith(TEST_SUIT_PREFIX) and _file.endswith(XML_SUFFIX) and _file != (casename + XML_SUFFIX) and _file != (suitname + XML_SUFFIX):
            _path = os.path.join(suit_path, _file)
            if get_case_status(_path) == STATUS["ENABLE"]:
                return True
    return False

def change_status(suitname, casename, status):
    res = FAILED
    if suitname == ALL_SIGN and casename == ALL_SIGN:
        traverse_cases(status)
        res = SUCCEED
    elif suitname != ALL_SIGN and casename == ALL_SIGN:
        suit_path = get_suit_path(suitname)
        if os.path.exists(suit_path) and os.path.isdir(suit_path):
            for _file in os.listdir(suit_path):
                if _file.startswith(TEST_SUIT_PREFIX) and _file.endswith(XML_SUFFIX):
                    _file_path = os.path.join(suit_path, _file)
                    res = set_case_status(_file_path, status)
    elif suitname != ALL_SIGN and casename != ALL_SIGN:
        suit_path = get_suit_path(suitname)
        case_path = os.path.join(suit_path, casename+XML_SUFFIX)
        if os.path.exists(case_path):
            if suitname != casename:
                suit_config_file = os.path.join(suit_path, suitname+XML_SUFFIX)
                if get_other_cases_status_flag(suit_path, suitname, casename, status):
                    pass
                else:
                    res = set_case_status(suit_config_file, status)
            res = set_case_status(case_path, status)
    else:
        return res

    return res

def enable_case(suitname, casename):
    return change_status(suitname, casename, STATUS["ENABLE"])

def disable_case(suitname, casename):
    return change_status(suitname, casename, STATUS["DISABLE"])

def config_qsst (raw_key='', value=''):
    """
    @type raw_key: string
    @param raw_key: name of the item that to be set.
    @type value: string
    @param : value of the item .
    """
    res = FAILED
    if not raw_key.startswith(PUBLIC_ITEM_PREFIX) and not raw_key.startswith(PRIVATE_ITEM_PREFIX):
        raw_key_list = raw_key.split(".")
        if len(raw_key_list) != 2:
            return res
        suitname = raw_key_list[0]
        casename = raw_key_list[1]
        status = value
        if status == '1':
            return enable_case(suitname, casename)
        if status == '0':
            return disable_case(suitname, casename)

    SU.init_filepath()
    config_path =  SU.FILE_PATH_CONFIG
    tree = ET.parse(config_path)
    root = tree.getroot();

    if raw_key.startswith(PUBLIC_ITEM_PREFIX):
        raw_key_list = raw_key.split(".")
        if len(raw_key_list) != 2:
            return res
        key = raw_key_list[1]
        for child in root.findall(PUBLIC_ITEM_PREFIX):
            if child.get('name') == key:
                res = SUCCEED
                child.text = value

    if raw_key.startswith(PRIVATE_ITEM_PREFIX):
        raw_key_list = raw_key.split(".")
        if len(raw_key_list) != 3:
            return res
        key = raw_key_list[1:]
        for child in root.findall(PRIVATE_ITEM_PREFIX):
            if child.get('name') == key[0]:
                for item in child.findall('item'):
                    if item.get('name') == key[1]:
                        res = SUCCEED
                        item.text = value
    if res == SUCCEED:
        tree.write(config_path)
        SU.update()
    return res

def main(argv):
    if len(argv) < 3:
        sys.stderr.write("Usage: python %s <params>\n" % (argv[0],))
        return FAILED
    return config_qsst(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    #print config_qsst('*.*', '0')
    #print config_qsst('test_suit_gmail.*', "1")
    #print config_qsst('test_suit_gmail.test_suit_gmail_case2', "0")
    #print config_qsst("public.smart_number", "78")
    #print config_qsst("private.phone.call_time", "18")

