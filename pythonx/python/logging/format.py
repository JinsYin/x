'''
定义一些常用的日志格式
'''

# NGINX 日志格式
NGINX_FMT = '%(asctime)s - [%(levelname)s] - %(user)s[%(ip)s] - %(message)s'

# Traceback 格式
TRACE_FMT = '%(asctime)s - [%(levelname)s] - %(pathname)s::%(funcName)s()::L%(lineno)d - %(message)s'
