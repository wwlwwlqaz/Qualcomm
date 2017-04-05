import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase

############################################
#author:
#    liqiang@cienet.com.cn
#function:
#    login->skip the nav->operation->post a status
############################################

class test_suit_renren_case1(TestCaseBase):
    def test_case_main(self,case_results):
        waitActivity = lambda:get_activity_name().startswith("com.renren.mobile.android")
        if not wait_for_fun(waitActivity, True, 5):
            start_activity("com.renren.mobile.android","com.renren.mobile.android.ui.WelcomeScreen")
        sleep(3)
        if not renren.is_login():
            if not renren.login():
                set_cannot_continue()
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'It is seems login failed.')
                return

        #skip navigator
        renren.skip_navigator()

        register_update_watcher(launcher.get_value('renren'), VIEW_BUTTON, ID_TYPE_TEXT, renren.get_value("ignore_it"), ACTION_CLICK)

        activityName = get_activity_name()
        if activityName != 'com.renren.mobile.android.desktop.DesktopActivity':
            set_cannot_continue()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'I dont know where i am , did you know?')
            return
        sleep(1)
        #view renren
        drag_by_param(50,80,50,20,10)
        sleep(1)
        drag_by_param(50,80,50,20,10)
        drag_by_param(50,80,50,20,10)
        #click to refresh
        if search_view_by_id('flipper_head_action'):
            click_button_by_id('flipper_head_action')
            waitProgress = lambda:search_view_by_id('progress_bar')
            #wait for the refresh
            wait_for_fun(waitProgress, False, 5)
        click_textview_by_text(renren.get_value('post_status'))
        #enter the message
        renren.share_with_renren_inner(SC.PRIVATE_RENREN_SHARE_CONTENT_SEQUENCE)
#        click_textview_by_id('input_editor', 1, 0)
#        ime.IME_input(1,SC.PRIVATE_RENREN_SHARE_CONTENT_SEQUENCE,'c')
#        #click the delete position button(textView)
#        click_button_by_id('flipper_head_action')
        unregister_update_watcher(launcher.get_value('renren'))
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def exit_app(self):
        set_can_continue()
        renren.exit_reren()
        TestCaseBase.exit_app(self)