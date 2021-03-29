#!/usr/bin/python
import sys
arg = list(map(int, sys.argv[1:]))
c = arg[0] + arg[1]
print("\n Addition of two numbers is", c)
c = arg[0] - arg[1]
print("\n Subtraction of two numbers is", c)
c = arg[0] * arg[1]
print("\n Multiplication of two numbers is", c)
c = arg[0] / arg[1]
print("\n Division of two numbers is", c)
c = arg[0] % arg[1]
print("\n modulus of two numbers is", c)
c = arg[0] ** arg[1]
print("\n Exponentiation of two numbers is", c)
c = arg[0] // arg[1]
print("\n Floor division of two numbers is", c)
