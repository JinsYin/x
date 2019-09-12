def index(arr, elem):
    """
    获取元素在数组中的第一个索引
    注：List.index() 方法未查找到元素时会抛出 ValueError 异常

    参数：
    * arr[list]
    * elem[any]
    """
    try:
        return arr.index(elem)
    except ValueError:
        return None
