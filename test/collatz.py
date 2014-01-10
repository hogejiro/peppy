#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 14 "Longest Collatz sequence" のテスト
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2014
"""

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../module/' ))
from module.collatz import Collatz

import nose
from nose.tools import *

def test_collatz_sequence():
    C = Collatz()
    start_num = 13
    collatz_seq = C.get_collatz_sequence(start_num)
    eq_( collatz_seq, [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

if __name__ == '__main__':
    main()

