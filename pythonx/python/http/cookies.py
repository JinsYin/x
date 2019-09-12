from http.cookies import SimpleCookie


def str2dict(rawcookie):
    """
    将 Cookie 字符串转换为字典
    """
    cookies = {}
    sc = SimpleCookie()
    sc.load(rawcookie)
    for key, morsel in sc.items():
        cookies[key] = morsel.value


def get(rawcookie, key):
    """
    cookie 中键的值，可能抛出 KeyError 异常
    """
    return str2dict(rawcookie)[key]


def set(rawcookie, key):
    """
    修改 cookie 中某个键的值
    """
    pass
