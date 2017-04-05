from case_utility import *
from qrd_shared.case import *
from test_case_base import TestCaseBase
import re,copy
from test_suit_ui_launcher import *
############################################
#author:
#    huitingn@qualcomm.com.cn
#function:
#     Launcher Stress-drag widget
############################################


class test_suit_ui_launcher_case06(TestCaseBase):
    tag = 'ui_launcher_case06'
    def test_case_main(self,case_results):
        case_flag = False
        
        global preWorkFlag
        if preWorkFlag is False:
            [toolsLocation,deviceID]=pre_work()
        
        if can_continue():
            send_key(KEY_HOME)
            basic = 'java -jar %s%sXAgentClientRunner.jar -s %s '%(toolsLocation,os.sep,deviceID)
            
            command = basic+'UICommand.getViewPosition %s equals %s'%('text','"Digital clock"')
            result = copy.copy(os.popen(command).read())
            (leftX,leftY,rightX,rightY) = re.search('(?<=true:)(\d+),(\d+),(\d+),(\d+)', result).group(1,2,3,4)
            
            startX = (leftX+rightX)/2 # the position of widget
            startY = (leftY+rightY)/2
            endX = (startX-120) *int(480.0/getDisplayWidth()) # this is the 'Remove's position
            endY = (startY-150) *int(854.0/getDisplayHeight())
            command = basic+'UICommand.Drag %s %s %s %s'%(startX,startY,endX,endY)
            
        if can_continue():
            command = basic+'UICommand.getViewPosition %s equals %s'%('text','Search')
            result = copy.copy(os.popen(command).read())
            (leftX2,leftY2,rightX2,rightY2) = re.search('(?<=true:)(\d+),(\d+),(\d+),(\d+)', result).group(1,2,3,4)
            
            before = (leftX,leftY,rightX,rightY)
            after = (leftX2,leftY2,rightX2,rightY2)
            if cmp(before,after)==0:
                case_flag = True
        
        
        log_test_case(self.tag, 'case_flag = '+str(case_flag))
        exit_cur_case(self.tag)
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "some widgets are failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
