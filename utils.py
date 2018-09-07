import time
import random


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    time_format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(time_format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)

def random_str():
    STR = "qwertyuiop[]\`1234567890-=asdfghjkl;'zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()_+"
    ran_str = ''.join(random.sample(STR, 64))
    return ran_str