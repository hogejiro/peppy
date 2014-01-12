#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Largest palindrome product
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%204
"""

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../module/'))
from palindrome import Palindrome

def main():
    P = Palindrome()
    ans = P.get_largest_palindrome_by_digit(3)
    print ans

if __name__ == '__main__':
    main()

# 906609
