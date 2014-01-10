#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 15 "Lattice Paths" のテスト
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2015
"""

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../module/' ))
from module.lattice import Lattice

import nose
from nose.tools import *

def test_lattice_paths():
    l = Lattice(2,2)
    test = l.count_lattice_paths()
    eq_(test, 6)

