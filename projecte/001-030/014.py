#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 14 "Longest Collatz sequence" の解法
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2014
"""

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../../module/' ))
from util import Collatz

def main():
    max = 1000000 # one million

    C = Collatz()
    for i in range(1, max + 1):
        this_collatz_seq = C.get_collatz_sequence(i)
        C.store_collatz_lengths(this_collatz_seq)

    # C.collatz_lengths_stored を value で整列して出力
    for start_num, collatz_length in sorted(C._collatz_lengths_stored.items(), key=lambda x:x[1]):
        sys.stdout.write("start number: %s, collatz sequence length: %s\n" %(start_num, collatz_length))

if __name__ == '__main__':
    main()

