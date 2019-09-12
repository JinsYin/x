import string
import random


def rand_string(length=8):
    """
    生成随机的数字字符串

    params:
        length: 字符串长度
    """
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def rand_number(length=8):
    """
    随机生成一个字符串数字 300000 ~ 400000
    """
    times = 10**(length - 1)  # 倍数
    return random.randint(3 * times, 4 * times)
