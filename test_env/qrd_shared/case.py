import fs_wrapper
import traceback
from logging_wrapper import *
from utility_wrapper import can_continue
from platform_check import is_serial_enabled
from test_case_base import CASE_BE_CALLED

from qrd_shared.camera.Camera import Camera
from qrd_shared.weibo.Weibo import Weibo
from qrd_shared.renren.Renren import Renren
from qrd_shared.settings.Settings import Settings
from qrd_shared.playstore.PlayStore import PlayStore
from qrd_shared.launcher.Launcher import Launcher
from qrd_shared.phone.Phone import Phone
from qrd_shared.browser.Browser import Browser
from qrd_shared.email.Email import Email
from qrd_shared.doubanfm.Doubanfm import Doubanfm
from qrd_shared.NotificationBar.NotificationBar import NotificationBar
from qrd_shared.mms.Mms import Mms
from qrd_shared.gmail.Gmail import Gmail
from qrd_shared.ime.IME import IME
from qrd_shared.contact.contact import Contact
from qrd_shared.shieldbox.ShieldBox import ShieldBox
from qrd_shared.gallery.Gallery import Gallery
from qrd_shared.cmcc_mtbf.CmccMTBF import CmccMTBF
from qrd_shared.sample.Sample import Sample
from qrd_shared.Incommon.InCommon import InCommon

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    the qrd share lib.
#doc:
#   juts need you to add : import your_model as alias
############################################

# init a instance of the mode
notificationBar = NotificationBar()
camera = Camera()
weibo = Weibo()
renren = Renren()
settings = Settings()
playstore = PlayStore()
launcher = Launcher()
phone = Phone()
browser = Browser()
email = Email()
doubanfm = Doubanfm()
mms = Mms()
gmail = Gmail()
ime = IME()
contact = Contact()
gallery = Gallery()
cmccMTBF = CmccMTBF()
sample = Sample()
incommon =InCommon()

if is_serial_enabled():
    shieldbox = ShieldBox()

LOG_TAG = 'qrd_share_case'

#create a instance
def createInstance(class_name, *args, **kwargs):
    (module_name, class_name) = class_name.rsplit('.', 1)
    module_meta = __import__(module_name, globals(), locals(), [class_name])
    class_meta = getattr(module_meta, class_name)
    o = class_meta(*args, **kwargs)
    return o


#call a case, will return the suit result
def call(suit_name,case_name,config_file_name='all_suit_config'):
    log_test_framework(LOG_TAG,  "begin call ... ")
    suit_names = fs_wrapper.get_suit_name_list("./")
    test_config_map = fs_wrapper.get_test_config(config_file_name)
    for suit in suit_names:
        if suit ==suit_name:
            #continue
            suit_py_module_name = fs_wrapper.get_suit_py_module_name(suit_name)
            if len(suit_py_module_name) == 0:
                continue
            # load the suit config
            suit_config_map = fs_wrapper.get_test_suit_config(suit_name)
            #check the suit whether is enable
            #if suit_config_map.get(fs_wrapper.SUIT_ENABLE_ATTR) != '1':
            #    log_test_framework(LOG_TAG, "the suit is disable")
            #    return
            #create the suit//suit_module_name + fs_wrapper.DOT_TAG + suit_name
            suit_info = test_config_map.get(suit_name)
            test_suit = createInstance(suit_py_module_name + fs_wrapper.DOT_TAG + suit_name, suit_name,suit_info)
            if suit_config_map.get(fs_wrapper.SUIT_RUNNER_ATTR) != None:
                test_suit.runner = suit_config_map.get(fs_wrapper.SUIT_RUNNER_ATTR)
            if suit_config_map.get(fs_wrapper.SUIT_APP_NAME) != None:
                app_name =  suit_config_map.get(fs_wrapper.SUIT_APP_NAME)
            # load test cases for test suit.
            # It will aggregate all the relative suit info for this test suit, too.
            case_names = fs_wrapper.get_all_cases_py_module_name(test_suit.name)
            for case in case_names:
                case_config_map = fs_wrapper.get_test_case_config(case[1], test_suit.name)
                case_app_name = case_config_map.get(fs_wrapper.CASE_APP_NAME)
                if case_app_name == None or case_app_name == "":
                    case_app_name = app_name
                #if case_config_map.get(fs_wrapper.CASE_ENABLE_ATTR) == '1':
                test_case = createInstance(case[0] + fs_wrapper.DOT_TAG + case[1], case[1], suit_name, case_app_name)
                test_case.case_config_map = case_config_map
                test_case.original_ClassName=''
                test_case.runReason=CASE_BE_CALLED
                test_suit.addCase(test_case)
            case_results = []
            for case in test_suit.test_cases:
                if case_name == "" or case.name == case_name:
                    set_ignore_status(True)
                    #save the current case name
                    pre_case_name = get_cur_case_name()
                    success = case.test_case_run(case_results)
                    #checkout the current case name
                    set_cur_case_name(pre_case_name)
                    set_ignore_status(False)
                    if success == None:
                        return True
                    return success
            log_test_framework(LOG_TAG,  "can not find the case name:"+case_name)
            return False
    log_test_framework(LOG_TAG,  "can not find the suit name:"+suit_name)
    return False
