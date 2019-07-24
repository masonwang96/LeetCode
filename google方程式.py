# -*- coding: utf-8 -*-
from datetime import datetime

"""
 @Author : Mason Wang 
 @E-mail : wangchiyaan@163.com
 @Time : 2019-07-24 15:47 
 @File : google方程式.py 
 @Software: PyCharm

 穷举搜索的例子：Google方程式，详见《算法的乐趣》王晓华 著 (Page 44)
    WWWDOT - GOOGLE = DOTCOM，每个字符代表0-9之间一个数字（不重复），并且首字符不能代表0
    要求找出满足等式的对应关系
"""


class CharItem:
    def __init__(self, c, v, leading):
        self.char = c
        self.value = v
        self.leading = leading


class CharValue:
    def __init__(self, v, used):
        self.value = v
        self.used = used


# 初始化
charItemList = [
    CharItem('W', -1, True), CharItem('D', -1, True), CharItem('O', -1, False), CharItem('T', -1, False),
    CharItem('G', -1, True), CharItem('L', -1, False), CharItem('E', -1, False), CharItem('C', -1, False),
    CharItem('M', -1, False)
]
charValueList = [
    CharValue(0, False), CharValue(1, False), CharValue(2, False), CharValue(3, False), CharValue(4, False),
    CharValue(5, False), CharValue(6, False), CharValue(7, False), CharValue(8, False), CharValue(9, False)
]

MAX_CHAR_INDEX = len(charItemList)


def search_result(char_item_list, char_value_list, index, callback_func, count):
    """
    对于传进来的每一个index位置的charItem，遍历所有数字，查看是否对应
    :param char_item_list:
    :param char_value_list:
    :param index:
    :param callback_func: 检查当前是否完成对应的匹配
    :return:
    """
    # 所有字符都在对应好了，检查是否满足等式
    if index == MAX_CHAR_INDEX:
        callback_func(char_item_list, count)
        return

    for i in range(len(char_value_list)):
        # 对首字符为0的情况进行剪枝
        if is_valid_value(char_item_list[index], char_value_list[i]):
            count += 1
            print('Count:', count)
            char_value_list[i].used = True  # 设置为已使用
            char_item_list[index].value = char_value_list[i].value
            search_result(char_item_list, char_value_list, index + 1, callback_func, count)
            # 搜索不成功，又将其标志位未使用
            char_value_list[i].used = False  # 设置为未使用


def is_valid_value(item, number):
    """
    判断首字符对应的数字是否有效：首字符不能对应0
    :param item: 字符类
    :param number: 数字类
    :return:
    """
    # 如果当前字符是首字符，那么不能对应0
    if item.leading:
        if number.value == 0:
            return False
    # 如果当前数字已使用，则不能再使用
    if number.used:
        return False
    return True


def check(char_item_list, count):
    """
    检查是否满足等式
    """
    a = 'WWWDOT'
    b = 'GOOGLE'
    c = 'DOTCOM'

    a_value = make_value(char_item_list, a)
    b_value = make_value(char_item_list, b)
    c_value = make_value(char_item_list, c)

    if a_value - b_value == c_value:
        print(a_value, '-', b_value, '=', c_value, "\tCount=", count)


def make_value(char_item_list, s):
    """
    根据建立的char_item_list，将s对应的字符串转换为数字
    :param char_item_list: 建立好的表
    :param s: string
    :return: int
    """
    res = ''
    for x in s:
        for item in char_item_list:
            if item.char == x:
                res += str(item.value)
                continue
    return int(res)


if __name__ == '__main__':
    start = datetime.now()
    global count
    count = 0
    search_result(charItemList, charValueList, 0, check, count)
    end = datetime.now()
    print('Cost of time:', format(end - start))
    print('------Done!------')
