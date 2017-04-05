import sys
l = len('/qsst_backup/backup_qsst.py')
cur_loc = sys.argv[0][0:-l]
where = sys.argv[1]
t = sys.argv[2]
sys.path.append(cur_loc)

import fs_wrapper
import time
import os
import shutil
import zipfile
from os.path import join

QSST_BACKUP = "qsst_backup"
PREFIX = "qsst_backup_"
BACKGROUND_CASE_POOL = 'background_case_pool'
curTime = t

def backup_to_local():
    work_dir = cur_loc + "/" + QSST_BACKUP + "/" + PREFIX + curTime
    makedirs(work_dir)
    makedirs(work_dir + "/settings")
    copy(cur_loc + "/settings/config.xml", work_dir + "/settings")
    suit_list = fs_wrapper.get_suit_name_list(cur_loc + "/")
    for suit in suit_list:
        makedirs(work_dir + "/" + suit)
        copy(cur_loc + "/" + suit + "/" + suit + ".xml", work_dir + "/" + suit)
        case_list = fs_wrapper.get_all_cases_py_module_name(suit, False)
        for case in case_list:
            copy(cur_loc + "/" + suit + "/" + case[1] + ".xml", work_dir + "/" + suit)

    bg_suit_list = fs_wrapper.get_suit_name_list(cur_loc + "/" + BACKGROUND_CASE_POOL + "/")
    for bg_suit in bg_suit_list:
        makedirs(work_dir + "/" + BACKGROUND_CASE_POOL + "/" + bg_suit)
        copy(cur_loc + "/" + BACKGROUND_CASE_POOL + "/"+ bg_suit + "/" + bg_suit + ".xml", work_dir + "/" + BACKGROUND_CASE_POOL +"/" + bg_suit)
        bg_case_list = fs_wrapper.get_all_cases_py_module_name(bg_suit, True)
        for bg_case in bg_case_list:
            copy(cur_loc + "/" + BACKGROUND_CASE_POOL + "/"+ bg_suit + "/" + bg_case[1] + ".xml", work_dir + "/" + BACKGROUND_CASE_POOL +"/" + bg_suit)

def backup_to_sdcard():
    backup_to_local()
    src = QSST_BACKUP + "/" + PREFIX + curTime
    print src + " generate."
    dst = PREFIX + curTime + ".zip"
    zip_dir(src, dst)
    print dst + " generate."
    copy(dst, "/sdcard/")
    if os.path.exists(src):
        shutil.rmtree(src)
        print src + " deleted."
    if os.path.exists(dst):
        os.remove(dst)
        print dst + " deleted."

def makedirs(dir):
    print "mkdir " + dir
    if not os.path.exists(dir):
         os.makedirs(dir)

def copy(src_file, dst_dir):
    print "cp " + src_file + " " + dst_dir
    shutil.copy(src_file, dst_dir)

def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()

if __name__ == '__main__':
    if where == "local":
        backup_to_local()
    else:
        backup_to_sdcard()