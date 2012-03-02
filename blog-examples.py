import lsystem
import turtle
from collections import namedtuple

"""
JUst grabbed stuff from the two example scripts and put it all here
"""

Systems = namedtuple( 'Systems', 'axiom, rules, angle, initial_angle, dist, age, lsystem, turtle, filetype' )

sys_dict = (
    Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 5,
        age = 0,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),
    Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 5,
        age = 1,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),
    Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 5,
        age = 2,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),
    Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 5,
        age = 3,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),
    Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 5,
        age = 4,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),
    Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 5,
        age = 5,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),

)

def generator ( name, item ):
    name = name + '-gen' + str(item.age) + '-ang' + str(item.angle) + '-len' + str(item.dist) + '.' + item.filetype
    turt = item.turtle( initial_angle = item.initial_angle, pen_width=1 )
    tree = item.lsystem( axiom=item.axiom , rules=item.rules )

    action = {
            'F': [ turt.forward, item.dist ],
            'G': [ turt.forward, item.dist ],
            '-': [ turt.right, item.angle ],
            '+': [ turt.left, item.angle ],
            '|': [ turt.right, 180 ],
            '[': [ turt.push ],
            ']': [ turt.pop ]
         }

    i = 0
    while i < item.age:
        i = i + 1
        tree.step()

    commands = str(tree)
    del tree
    for term in commands:
        if term in action:
            if len(action[term]) > 1:
                action[term][0](action[term][1])
            else:
                action[term][0]()

    turt.draw()
    turt.save( name, item.filetype )

for key in sys_dict:
    generator( 'example-weed', key )

axiom = 'A'
rules = { 'A' : 'AB', 'B' : 'A' }
age = 5

tree = lsystem.LSystem( axiom=axiom , rules=rules )

i = 0
while i < age:
    i = i + 1
    print tree
    tree.step()

print tree
