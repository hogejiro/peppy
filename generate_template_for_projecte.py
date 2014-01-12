#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# getdirandfilename(37) returns ("/path/to/peppy/projecte/031-060", 037.py)
def getdirandfilename(problem_number):
    stride = 30
    base  = int(problem_number) / stride
    start = base * stride + 1
    end   = (base + 1) * stride
    digit = 3
    dir = os.path.abspath(os.path.dirname(__file__)) + "/projecte/" + str(start).zfill(digit) + "-" + str(end).zfill(digit)
    filename = problem_number.zfill(digit) + ".py"
    return (dir, filename)

argv = sys.argv
argc = len(argv)

if (argc != 3):
    print "python %s {problem_number} {problem_name}" % __file__
    quit()

problem_number = argv[1]

if problem_number.isdigit() == False or int(problem_number) <= 0:
    print "{problem_number} must be positive number"
    quit()

(dir, filename) = getdirandfilename(problem_number)

if os.path.isdir(dir) == False:
    os.mkdir(dir)

if os.path.exists("%s/%s" % (dir, filename)):
    print "file %s already exists" % filename
    quit()

problem_name = argv[2]
output = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

\"\"\"
{problem_name}
ref: http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%20{problem_number}
\"\"\"

import sys,os
sys.path.append(os.path.join( os.path.dirname(os.path.abspath(__file__)), '../../module/' ))

def main():
    return

if __name__ == '__main__':
    main()

# answer
""".format(problem_name = problem_name, problem_number = problem_number)

fh = open("%s/%s" % (dir, filename), 'w')
fh.write(output)
fh.close()
