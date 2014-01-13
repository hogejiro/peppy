#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Highly divisible triangular number
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2012
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))
from prime import Prime

def get_triangle_number():
    ret = 1
    stride = 2
    while True:
        ret += stride
        yield ret
        stride += 1

def main():
    P = Prime()
    tn_iterator = get_triangle_number()
    while True:
        triangle_number = tn_iterator.next()
        count_of_divisors = P.get_count_of_divisors_by_number(triangle_number)
        if 500 < count_of_divisors:
            break
    print triangle_number

if __name__ == '__main__':
    main()

# 76576500
