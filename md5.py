# coding=gbk

import hashlib
import os
import datetime
from utils import log

def GetFileMd5(filename):
    # 输出文件的md5值以及记录运行时间
    starttime = datetime.datetime.now()
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b:
            log('break')
            break
        myhash.update(b)
    f.close()
    endtime = datetime.datetime.now()
    log('GetFileMd5运行时间：%ds' % ((endtime - starttime).seconds))
    return myhash.hexdigest()







# if __name__ == "__main__":
#     filepath = 'ass.mp4'
#
#     # 输出文件的md5值以及记录运行时间
#     starttime = datetime.datetime.now()
#     print('file_MD5: '+GetFileMd5(filepath))
#     endtime = datetime.datetime.now()
#     print('运行时间：%ds'%((endtime-starttime).seconds))

