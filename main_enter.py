from change_md5 import fileAppend
from md5 import GetFileMd5
from video_edition import edition
from utils import log


def video(filepath):
    for filename in filepath:
        MD5_0 = GetFileMd5(filename)
        log('file_MD5: {0}'.format(MD5_0))
        MD5_changed = fileAppend(filename)
        if MD5_0 != MD5_changed:
            log('MD5_0: {0}'.format(MD5_0))
            log('MD5_changed: {0}'.format(MD5_changed))
            return edition(filename)

if __name__ == "__main__":
    filepath = ['ass.mp4', ]
    video(filepath)