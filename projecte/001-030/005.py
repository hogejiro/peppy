#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Smallest multiple
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%205
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))

def lcm(x, y):
    import fractions
    return x * y / fractions.gcd(x, y)

def main():
    print reduce(lcm, range(1, 20))

if __name__ == '__main__':
    main()

# 232792560
