#!/usr/bin/python
import sys
_, arg1, arg2, arg3 = sys.argv
print("First number is", arg1)
print("Second number is", arg2)
print("Third number is", arg3)
print("The biggest of three numbers is", max(arg1, arg2, arg3))
