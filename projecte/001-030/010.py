#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Summation of primes
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2010
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))
from prime import Prime

def main():
    P = Prime()
    print sum(P.get_primes_by_upper_limit(2000000))

if __name__ == '__main__':
    main()

# 142913828922
