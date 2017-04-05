import os
import sys
from performance import html,csv

l = len("performance_report.py")
TEST_ENV_DIR = sys.argv[0][0:-l]
TEST_DATE_PATH = ""
TEST_REPORT_PATH = ""
TEST_REPORT_TYPE = ""
print sys.argv
if len(sys.argv) >= 4:
    TEST_DATE_PATH = sys.argv[1]#get test_main.py file location
    TEST_REPORT_PATH = sys.argv[2]#get the report result
    TEST_REPORT_TYPE = sys.argv[3]#get the report result type
else:
    print >> sys.stderr, "You should give me a path of the KPI data and the path of the report"
    exit(1)
os.chdir(TEST_ENV_DIR)

if TEST_REPORT_TYPE == 'csv':
    csv(TEST_DATE_PATH,TEST_REPORT_PATH)
else:
    html(TEST_DATE_PATH,TEST_REPORT_PATH)
exit(0)