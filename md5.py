# coding=gbk

import hashlib
import os
import datetime
from utils import log

def GetFileMd5(filename):
    # ����ļ���md5ֵ�Լ���¼����ʱ��
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
    log('GetFileMd5����ʱ�䣺%ds' % ((endtime - starttime).seconds))
    return myhash.hexdigest()







# if __name__ == "__main__":
#     filepath = 'ass.mp4'
#
#     # ����ļ���md5ֵ�Լ���¼����ʱ��
#     starttime = datetime.datetime.now()
#     print('file_MD5: '+GetFileMd5(filepath))
#     endtime = datetime.datetime.now()
#     print('����ʱ�䣺%ds'%((endtime-starttime).seconds))

