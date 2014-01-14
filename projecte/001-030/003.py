#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Largest prime factor
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%203
"""

import sys,os
sys.path.append(os.path.join( os.path.abspath(os.path.dirname(__file__)), '../../module/' ))
from prime import Prime

def main():
    P = Prime()
    prime_factors = P.get_prime_factors(600851475143)
    print(max(prime_factors.keys()))

if __name__ == '__main__':
    main()

# 6857
