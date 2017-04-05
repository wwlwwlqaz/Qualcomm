import sys
l = len('/qsst_backup/backup_qsst.py')
cur_loc = sys.argv[0][0:-l]
where = sys.argv[1]
which = sys.argv[2]
sys.path.append(cur_loc)

import os
import shutil
import zipfile
import os,os.path
from os.path import join

QSST_BACKUP = "qsst_backup"

def copy(src, dest):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        for f in files:
                copy(os.path.join(src, f), os.path.join(dest, f))
    else:
        shutil.copy(src, dest)
    cmd = "chmod -R 777 " + dest
    os.system(cmd)

def unzip_file(zipfilename, unziptodir):
    zipFile = zipfile.ZipFile(zipfilename)
    for file in zipFile.namelist():
        zipFile.extract(file, unziptodir)
    zipFile.close()

def restore_from_local():
    copy(QSST_BACKUP + "/" + which, cur_loc)

def restore_from_sdcard():
    unzip_file("/sdcard/" + which, "/sdcard/" + which[:-4])
    src = "/sdcard/" + which[:-4]
    copy(src, cur_loc)
    if os.path.exists(src):
        os.system("rm -r " + src)
        print src + " deleted."

if __name__ == '__main__':
    if where == "local":
        restore_from_local()
    else:
        restore_from_sdcard()