#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/10 12:56
@Author  : zichao.li
@Site    : 
@File    : show.py
@Software: PyCharm
"""
import sys


def prt(i):
    """
    这是一个打印方法，输出输入参数
    :return:
    """
    print("start...")
    x = 0
    for j in range(i):
        x += j
    print(x)
    print('end...')


def jianfa(a, b):
    return a - b


def jiafa(a, b):
    return a + b


print('hello quant')
if __name__ == '__main__':
    print('main program')
    pass
