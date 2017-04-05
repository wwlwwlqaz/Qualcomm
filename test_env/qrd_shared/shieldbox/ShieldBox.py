from case_utility import *
from qrd_shared.Base import Base
import settings.common as SC
import time
from platform_check import is_serial_enabled
if is_serial_enabled():
    import serial
############################################
#author:
#    chunminghu@cienet.com.cn
#function:
#    the shieldbox mode of qrd share lib.
#doc:
############################################
class ShieldBox(Base):
    def __init__(self):
        self.mode_name = "shieldbox"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))

    def open_shield_box(self):
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM' + SC.PUBLIC_SHIELD_BOX_PORT
        ser.open()
        ser.write("open" + '\x0d')
        ser.close()

    def close_shield_box(self):
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM' + SC.PUBLIC_SHIELD_BOX_PORT
        ser.open()
        ser.write("close" + '\x0d')
        ser.close()
