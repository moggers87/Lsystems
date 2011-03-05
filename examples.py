"""
This script will go if someone writes some documention :)
"""

import lsystem
import turtle
import sys

"""
F forward
+ turn clockwise
- turn anticlockwise
| turn around
[ push turtle state onto stack
] pop
"""

start = 'F'
rule = { 'F': 'FF-[-F+F+F]+[+F-F-F]' }
name = 'tree'
angle = 22.5

#start = 'X'
#rule = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' }
#name = 'weed'
#angle = 25

#start = 'F+F+F'
#rule = { 'F' : 'F+F-F-F+F' }
#name = 'sTri'
#angle = 120

#start = 'F'
#rule = { 'F' : 'G-F-G', 'G' : 'F+G+F' }
#name = 'sTri2'
#angle = 60

dist = 10
age = 5
name = name + '-gen' + str(age) + '-ang' + str(angle) + '-len' + str(dist) + '.png'
filetype = 'png'
turt = turtle.TurtlePIL()
tree = lsystem.LSystem( axiom=start , rules=rule  )
action = { \
            'F': [ turt.forward, dist ], \
            'G': [ turt.forward, dist ], \
            '-': [ turt.right, angle ], \
            '+': [ turt.left, angle ], \
            '|': [ turt.right, 180 ], \
            '[': [ turt.push ], \
            ']': [ turt.pop ] \
         }

i = 0
while i < age:
    i = i + 1
    tree.step()

commands = str(tree)
del tree
print 'Releasing lsystem object...'

for term in commands:
    if term in action:
        if len(action[term]) > 1:
            action[term][0](action[term][1])
        else:
            action[term][0]()

turt.draw()
turt.save( name, filetype )
print 'Drawing saved as ' + name
