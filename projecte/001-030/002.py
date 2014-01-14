#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Even Fibonacci numbers
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%202
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))
from fibonacci import Fibonacci

def main():
    F = Fibonacci()
    ans = F.get_fibs_by_upper_limit(4000000)
    print sum([l for l in ans if l % 2 == 0])

if __name__ == '__main__':
    main()

# 4613732
