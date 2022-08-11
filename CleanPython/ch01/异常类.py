# !/usr/bin/python
# -*- coding: utf-8 -*-

# 创建自己的异常类


class UserNotFoundException(Exception):
    """ 
    Raise the exception when user not found.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


def get_user_from_db(obj):
    """
    Get user information from DB.
    """
    current_user = obj.user
    return current_user


def get_user_info(user_obj):
    """
    Get user information from DB.
    """
    user = get_user_from_db(user_obj)
    if not user:
        raise UserNotFoundException(f"No user found of this id:{user_obj.id}")


print(get_user_info)

# 创建于范围有关的自定义异常类


class ValiditionError(Exception):
    """ 
    Raise the exception whenever validation failed. 
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


# 只处理特定异常
# 处理特定异常有助于调试或诊断问题


def get_even_list(num_list):
    """
    Get list of the odd numnbers form given list.
    """
    return [item for item in num_list if item % 2 == 0]


numbers = None

try:
    get_even_list(numbers)
except NoneType:
    print("None Vslue has been provided.")
except TypeError:
    print("Type error has been raised due to non sequential data type.")
