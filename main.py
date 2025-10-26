def isOdd(value):
    """
    判断输入是否为奇整数    
    参数:
    value - 任意类型的输入值    
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    # 首先排除布尔类型（因为bool是int的子类），再检查是否为整数
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        # 若为整数，判断是否为奇数
        return value % 2 != 0
    # 非整数类型直接返回False
    return False
