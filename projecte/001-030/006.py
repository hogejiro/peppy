#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sum square difference
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%206
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))

def main():
    limit_number = 100
    sum_of_square = sum([x ** 2 for x in range(limit_number + 1)])
    square_of_sum = sum([x for x in range(limit_number + 1)]) ** 2
    print square_of_sum - sum_of_square

if __name__ == '__main__':
    main()

# 25164150
