#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Multiples of 3 and 5
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%201
"""

list = range(1, 1000)
list_filtered = [l for l in list if l % 3 == 0 or l % 5 == 0]
print sum(list_filtered)
# 233168
