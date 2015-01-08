"""
This script will go if someone writes some documention :)
"""
from __future__ import print_function


import lsystem
import turtle
from collections import namedtuple

axiom = 'A'
rules = { 'A' : 'AB', 'B' : 'A' }
age = 5

tree = lsystem.LSystem( axiom=axiom , rules=rules )

i = 0
while i < age:
    i = i + 1
    print(tree)
    tree.step()

print(tree)
