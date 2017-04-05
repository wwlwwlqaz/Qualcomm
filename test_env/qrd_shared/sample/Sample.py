#coding=utf-8
#需要import的一些模块
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.ime.IME import IME
import settings.common as SC
from logging_wrapper import log_test_case
import time

#这里可以写一些common的方法，给suit里面的case调用
class Sample(Base):
    def __init__(self):
        self.mode_name = "Sample"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))
