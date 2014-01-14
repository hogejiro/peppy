#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
10001st prime
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%207
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))
from prime import Prime

def main():
    P = Prime()
    primes = P.get_n_primes(10001)
    print primes[-1]

if __name__ == '__main__':
    main()

# 104743
