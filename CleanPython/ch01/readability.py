# !/usr/bin/python
# -*- coding: utf-8 -*-

# 关于代码可读性
# 对嵌套字典进行排序

#1-9
from multiprocessing.sharedctypes import Value

users = [{"first_name": "Halen", "age": 39}, {"first_name": "Buck", "age": 10}, {"first_name": "anni", "age": 9}]
print(users)
users = sorted(users, key=lambda user: user["first_name"].lower())
print(users)


# 以函数形式对字典记性排序
def get_user_name(users):
    """
    get name of the user in lower case 

    Args:
        users (_type_): _description_
    """
    return users["first_name"].lower()


def get_sorted_dictionary(users):
    """ 
    sort the nested dictionary
    """
    if not isinstance(users, dict):
        raise ValueError("Not a correct dictionary")
    if not len(users):
        raise ValueError("Empty dcitionary")

    users_by_name = sorted(users, key=get_user_name)
    return users_by_name