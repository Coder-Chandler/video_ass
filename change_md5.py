import os
from utils import random_str
from utils import log

def fileAppend(filename):
    myfile = open(filename,'a')
    random_STR = random_str()
    myfile.write(random_STR)
    myfile.close()
    log("{0} MD5 value changed!".format(filename))
    return



# if __name__ == '__main__':
#     filename = 'ass.mp4'
#     fileAppend(filename)
#     log("{0} MD5 value changed!".format(filename))