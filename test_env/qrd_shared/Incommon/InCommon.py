#coding=utf-8
#需要import的一些模块


'''
   shared library to record video.The purpose is to make debug easier

   @author: U{c_yazli<c_yazli@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see:
   @note:
   @attention:
   @bug:
   @warning:

'''
from case_utility import *
from qrd_shared.Base import Base
from qrd_shared.ime.IME import IME
import settings.common as SC
from logging_wrapper import log_test_case
import time
import re

#这里可以写一些common的方法，给suit里面的case调用
class InCommon(Base):
    def __init__(self):
        self.mode_name = "InCommon"
        Base.__init__(self,self.mode_name)
        self.debug_print( 'Base init:%f' %(time.time()))
        
    def record_video(self):
        self.adb_pipe = subprocess.Popen('adb shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
        while ( re.match( r'^[$#]', self.adb_pipe.stdout.readline(1), re.M|re.I) == None ):
            pass
        pid = self.exe_command(self.adb_pipe,'screenrecord --verbose /storage/sdcard0/Record.mp4 &\n')        
        apid=pid.strip('\r\n').split(' ')
        self.dog = apid[1]
        
    def exe_command(self,pipe, command=""):
        ret_val = ""
        #print "exec command:", command

        #if no command arg, it means reading output only
        if ( command != "" ):
            pipe.stdin.write(command)
            pipe.stdin.flush()
            pipe.stdout.readline() #this will read the command itself
            #print "command itself:", str

        #this will read the command output
        ch = pipe.stdout.readline(1)
        one_line = ''
        while ( re.match(r'^[$#]', ch, re.M|re.I) == None ):
            #print "ch:", ch
            if ( ch != '\r'): one_line = one_line + ch #\n is for newline
            #add the line
            if ( ch == '\n' ):
                ret_val = ret_val + one_line
                one_line = ""
            ch = pipe.stdout.readline(1)

        #print "command output:", ret_val
        return ret_val
    
    def stop_video_record(self,casename):
        self.exe_command(self.adb_pipe,'kill -2 %s\n'%self.dog)
        time.sleep(6)
        os.system('adb pull /storage/sdcard0/Record.mp4 C:/QSST_RECORD/%s.mp4' %casename)
        self.adb_pipe.kill()