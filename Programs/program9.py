#!/usr/bin/python
import sys
arg = list(map(int, sys.argv[1:]))

a = complex(arg[0], arg[1])
b = complex(arg[2], arg[3])
c = a + b
print("\n Addition of two complex numbers is", c)
c = a - b
print("\n Subtraction of two complex numbers is", c)
c = a * b
print("\n Multiplication of two complex numbers is", c)
c = a / b
print("\n Division of two complex numbers is", c)
