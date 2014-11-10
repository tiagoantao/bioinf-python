#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A silly application mimicking many of the pitfalls with bioinformatics
#  software.

# This application does not have command-line parameters, but that
#   is standard stuff that does not concern us here.

in_file = 'in.params'
f = open(in_file)
n1 = float(f.readline().rstrip())
n2 = float(f.readline().rstrip())
f.close()

print('Please input your extra operation')
print('1: Subtraction')
print('2: Addition')

op = bla

print('The result of the multiplication is: %f' % n1 * n2)
if op == 1:
    res = n1 - n2
else:
    res = n1 + n2

out_file = 'out.results'
w = open(out_file, 'w')
w.write('The configurable result is: %f\n' % res)
w.close()
