#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Multiples of 3 and 5
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%201
"""

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../../module/' ))

def main():
    list = range(1, 1000)
    list_filtered = [l for l in list if l % 3 == 0 or l % 5 == 0]
    print sum(list_filtered)

if __name__ == '__main__':
    main()

# 233168
