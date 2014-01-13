#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Special Pythagorean triplet
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%209
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))

def main():
    product = [a * b * c for a in range(1, 333) for b in range(a, 500) for c in range(b, 1000) if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2]
    print product[0]

if __name__ == '__main__':
    main()

# 31875000
