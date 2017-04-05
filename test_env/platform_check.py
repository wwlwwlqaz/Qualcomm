'''
   get platform info

   Because this Qsst python framework can work
   cross platforms , this file help to get the
   platforms' info.

   PC windows will get platform info as 'Windows'
   PC Linux will get platform info as 'Linux-PC'
   Android platform will get platform info as 'Linux-Phone'

   @author: U{binz<binz@qti.qualcomm.com>}
   @author: U{zhibinw<zhibinw@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

'''
import platform

'''can only enable serial on windows currently,
before enable this make sure you have install serial library for python'''
_ENABLE_SERIAL = False

def get_platform_info():
    '''
    get platform infomation.

    PC Windows will return 'Windows'
    PC Linux will return 'Linux-PC'
    Andorid platform will return 'Linux-Phone'

    @return: platform infomation.
    '''
    sysInfo = platform.system()
    platformInfo = platform.platform()

    if(sysInfo =='Windows'):
        return sysInfo
    elif(sysInfo == 'Linux'):
        if(platformInfo.find('arm') >= 0) or (platformInfo.find('arch') >= 0):
            return sysInfo + '-Phone'
        else:
            return sysInfo + '-PC' #modified by huitingn
    else:
        return ''
    '''
    judge whether serial is enabled.
    @return: Ture if enabled, False if not.
    '''
def is_serial_enabled():
    if _ENABLE_SERIAL and get_platform_info() == 'Windows':
        return True
    else:
        return False
