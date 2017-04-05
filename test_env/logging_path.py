import os
import sys
import settings.update as SU
if len(sys.argv) >= 2:
    TEST_ENV_DIR = sys.argv[1]#get test_main.py file location
else:
    # get path 'data/test_env_xxx/' from argument 'data/test_env_xxx/test_main.py'
    l = 'test_main.py'
    TEST_ENV_DIR = sys.argv[0][0:-l]
os.chdir(TEST_ENV_DIR)
SU.update()
import settings.common as SC
print "LOGGING_PATH:"+SC.PUBLIC_LOG_PATH
