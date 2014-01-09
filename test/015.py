#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 15 "Lattice Paths" のテスト
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2015
"""

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../module/' ))
from util import Lattice

l1 = Lattice(2,2)
test = l1.count_lattice_paths()
assert test == 6

