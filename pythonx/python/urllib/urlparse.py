import urllib


def param2dict(url):
    """将 URL 参数转换为字典
    """
    pass


def getparam(url, param):
    """获取某个 URL 参数的值
    """
    parsed_url = urllib.parse.urlparse(url)
    qs = urllib.parse.parse_qs(parsed_url)
    return qs[param]


def setparam(url, param):
    """修改某个 URL 参数的值
    """
    return url
