'''
    shard library of launcher module

    This part share functions from launcher, well, lots of case will use
    operations about launcher as launch an app from launcher,back to launcher and so on.
    We integrate such functions here ,all cases can use it freely.

    1.How to use it in case:

     >>> from qrd_shared.launcher.Launcher import Launcher
     >>> launcher = Launcher()
     >>> launcher.launch_from_launcher(app_name)

    in order to support multi language, the 'app_name' here is not the app name string itself,
    it is a string id in resource file in launcher/res/values-xx, the string will be located
    dynamically according to current locale.

    2.More shared functions of launcher can be added here,any modification
    here must guarantee the api not change since it may be used by cases not in your scope.

    3.We have met an issue that sometimes launch an app from launcher by click its icon can not starup the app,
    we are sure the click event is done, but the app did not start.This occurs the first time which means if there are
    10 cases to launch mms , only the first case will fail to launch.Root cause isn't clear now.It is not reproduced 100%.


    @author: U{zhibinw<zhibinw@qti.qualcomm.com>}
    @version: version 1.0.0
    @requires:python 2.7+
    @license:


'''
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.language.language import Language
import time
MMS = 'mms'
DIAL = 'phone'
PEOPLE ='people'
EMAIL = 'email'
SETTINGS ='system_settings'
BROWSER = 'browser'
CAMERA = 'camera'
class Launcher(Base):
    '''Launcher class abstract for shared functions from Launcher module.

        Launcher will provide common launcher related functions for all
        cases ,such as launch an app by pass its name and so on.
    '''
    def __init__(self):
        self.mode_name = 'launcher'
        super(Launcher,self).__init__(self.mode_name)
        self._MAX_TRY = 10
        self._MAX_TRY_LAUNCHER = 5
    def launch_from_launcher(self, name):
        '''launch an app from launcher by passing
        its name, this name should be a string id to support multi
        language.

        @type name:string
        @param name: string id of app name.
        @return: True on success,which  means perform click success ,False on did not find the app to click.
        '''
        self.back_to_launcher()
        if (name == None or len(name) <= 0 ):
            return False
        '''base on the Home activity'''
        if self.processMenu(name):
            return True
        click_textview_by_desc(self.get_value('Apps list'))
        sleep(1)
        #click_textview_by_text(self.get_value('apps'))
        app_name = self.get_value(name)
        
        try: click_textview_by_text(app_name, 0, 1, TEXT_MATCHES, waitForView = 1)
        except Exception:
            try: click_textview_by_text(app_name, 1, 1, TEXT_MATCHES, waitForView = 1)
            except Exception:
                pass
                #print_report_line("Launcher: Cannot find QSST icon vertical nor horizonal.")
        return True
        
        for i in range(self._MAX_TRY_LAUNCHER):
            if get_activity_name() == 'com.android.launcher2.Launcher':
                sleep(1)
                click_textview_by_text(app_name, 0, 1, waitForView = 1)
            else:
                return True
        return False

    def back_to_launcher(self) :
        '''
        back to main screen of launcher, currently it will press ok if met an
        Anroid ANR dialog or ForceClose dialog.
        @note:if app itself handle back key and home key specially,this functions may not
        work ,please verify first.
        '''
        '''check force close '''
        if search_text(self.get_value('Unfortunately'),0,0) and search_text(self.get_value('btn_ok'),0,0):
                click_textview_by_text(self.get_value('btn_ok'))
        '''check anr '''
        if search_text(self.get_value('no_response'),0,0,TEXT_CONTAINS) and search_text(self.get_value('btn_ok'),0,0):
                click_textview_by_text(self.get_value('btn_ok'))
        for i in range(self._MAX_TRY):
            if get_activity_name() != 'com.android.launcher2.Launcher':
                sleep(1)
                goback()
            else:
                break
        sleep(1)
        send_key(KEY_HOME)
    def processMenu(self,name):
        '''
        press menu item in launcher as wallpaper ,manager apps, system settings.
        currently can not compatible with extends menus ,if you add other menu item
        in launcher menu, please also update this.

        @type name:string
        @param name:string id of the text on menu.

        '''
        sleep(1)
        if name in ['wallpaper','manage_apps','system_settings']:
        
            click_menuitem_by_text(self.get_value(name))
            return True 
        return  False


