import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    use the foreground camera to take a VGA picture
#precondition:
#    there is a mounted sdcard
#steps:
#    open the foreground camera
#    set the VGA picture size
#    take a picture
############################################

class test_suit_weibo_case1(TestCaseBase):
    def test_case_main(self,case_results):
        waitActivity = lambda:get_activity_name().startswith("com.sina.weibo")
        if not wait_for_fun(waitActivity, True, 5):
            start_activity("com.sina.weibo","com.sina.weibo.SplashActivity")
        sleep(3)
        if not weibo.is_login():
            if not weibo.login():
                set_cannot_continue()
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'It is seems login failed.')
                return

        #skip navigator
        weibo.skip_navigator()

        register_update_watcher(launcher.get_value('weibo'), VIEW_TEXT_VIEW, ID_TYPE_TEXT, weibo.get_value("new_version"), ACTION_GO_BACK)

        activityName = get_activity_name()
        if activityName != 'com.sina.weibo.MainTabActivity':
            set_cannot_continue()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'I dont know where i am , did you know?')
            return
        #click the home tab
        click_view_by_container_id('main_radio','android.view.View',0)
        sleep(5)
        #view weibo
        drag_by_param(50,80,50,20,10)
        drag_by_param(50,80,50,20,10)
        drag_by_param(50,80,50,20,10)
        sleep(1)

        #new a post
        drag_by_param(10,10,11,11,1)
        #enter the message
        weibo.share_with_weibo_inner(SC.PRIVATE_WEIBO_SHARE_CONTENT_SEQUENCE)
#        click_textview_by_id('et_mblog', 1, 0)
#        ime.IME_input(1,SC.PRIVATE_WEIBO_SHARE_CONTENT_SEQUENCE,'c')
#        #click the delete position button(textView)
#        click_textview_by_text(weibo.get_value('send'))
        unregister_update_watcher(launcher.get_value('weibo'))
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

