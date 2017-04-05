import time
import os
import fileinput
import settings.common as SC
from logging_wrapper import DATA_MONITOR_STATUS_PATH,clear_file,file_insert
import sys

DIVIDE=":"
'''prefix tag for normal message in qsst file'''
PREFIX_MSG = "MSG"
'''prefix tag for case in qsst file'''
PREFIX_CASE = "CASE"
SUFFIX_QSST = ".qsst";

LOG_ROOT = sys.argv[1]

def mergeMonitorInfoToQsstFile():
    try:

        #read contents of auto_monitor_end.qsst into list
        monitor_file = open(DATA_MONITOR_STATUS_PATH)
        content = list(monitor_file.readlines())
        monitor_file.close()

        already_insert_line_per_case = 0
        old_suit_name = ""
        old_case_name = ""
        for line in content:
            each_line = line.strip('\n')
            content_list = each_line.split(DIVIDE);
            cycle_time = content_list[0]
            suit_name = content_list[1]
            case_name = content_list[2]
            time_stamp = content_list[3]
            service_type = content_list[4]
            description = content_list[5]
            write_content = PREFIX_MSG + DIVIDE + __format_time(time_stamp) + DIVIDE + service_type + DIVIDE + description

            #Get qsst file root
            if (cycle_time == '.'):
                qsst_root = LOG_ROOT + suit_name + os.sep + suit_name + SUFFIX_QSST
            else:
                qsst_root = LOG_ROOT + cycle_time + os.sep + suit_name + os.sep + suit_name + SUFFIX_QSST

            if not os.path.isfile(qsst_root):
                return

            qsst_file = open(qsst_root,'r')
            qsst_line_no = 1;

            #Open qsst file, and merge monitor info under relevant case.
            while(True):
                line = str(qsst_file.readline())
                qsst_line_no += 1
                #find same current time.
                if(line.startswith(PREFIX_CASE + DIVIDE + suit_name + DIVIDE + case_name)):
                    #write monitor info
                    if(old_suit_name == suit_name and old_case_name == case_name):
                        already_insert_line_per_case = already_insert_line_per_case + 1
                    else:
                        already_insert_line_per_case = 0
                    old_suit_name = suit_name
                    old_case_name = case_name
                    qsst_file.close()
                    file_insert(qsst_root,qsst_line_no+already_insert_line_per_case,write_content)
                    break
                elif(line =='' or line == None):
                    break
    except OSError:
        print "merger monitor info to qsst file failed"
    #After merging, clear auto_monitor.qsst
    print ("mergeMonitorInfoToQsstFile"," clear monitor --- " )
    clear_file(DATA_MONITOR_STATUS_PATH)

def __format_time(time_stamp):
    return time_stamp.replace('_',':')

if __name__ == '__main__':
    mergeMonitorInfoToQsstFile()