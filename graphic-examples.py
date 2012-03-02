"""
This script will go if someone writes some documention :)
"""

import lsystem
import turtle
from collections import namedtuple

"""
F forward
+ turn clockwise
- turn anticlockwise
| turn around
[ push turtle state onto stack
] pop
"""

Systems = namedtuple( 'Systems', 'axiom, rules, angle, initial_angle, dist, age, lsystem, turtle, filetype' )

examples = {
    'tree': Systems(
        axiom = 'F',
        rules = { 'F': 'FF-[-F+F+F]+[+F-F-F]' },
        angle = 22.5,
        initial_angle = -90,
        dist = 10,
        age = 5,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),

    'weed': Systems(
        axiom = 'X',
        rules = { 'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF' },
        angle = 25,
        initial_angle = -90,
        dist = 10,
        age = 5,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),

    'sTri': Systems(
        axiom = 'F+F+F',
        rules = { 'F' : 'F+F-F-F+F' },
        angle = 120,
        initial_angle = 0,
        dist = 10,
        age = 7,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),

    'sTri2': Systems(
        axiom = 'F',
        rules = { 'F' : 'G-F-G', 'G' : 'F+G+F' },
        angle = 60,
        initial_angle = -60,
        dist = 10,
        age = 7,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.LSystem,
        filetype = 'png'
    ),

    'stoch-weed': Systems(
        axiom = 'X',
        rules = { 'X' : [ 'F-[[X]+X]+F[+FX]-X', 'F-[[X]+X]+F[+FX]-X', None ] , 'F' : [ 'FF', 'FF', None ] },
        angle = 25,
        initial_angle = -90,
        dist = 10,
        age = 5,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.StochasticLSystem,
        filetype = 'png'
    ),

    'stoch-symtree': Systems(
        axiom = 'F',
        rules = { 'F': [ 'FF-[-F+F+F]+[+F-F-F]', 'FF+[+F-F-F]-[-F+F+F]' ] },
        angle = 22.5,
        initial_angle = -90,
        dist = 10,
        age = 5,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.StochasticLSystem,
        filetype = 'png'
    ),

    'stoch-example': Systems(
        axiom = 'F',
        rules = { 'F': [ 'F[+F]F[-F]F', 'F[+F]F', 'F[-F]F' ] },
        angle = 22.5,
        initial_angle = -90,
        dist = 10,
        age = 5,
        turtle = turtle.TurtlePIL,
        lsystem = lsystem.StochasticLSystem,
        filetype = 'png'
    )
}

def generator ( name, item ):
    print name + '...'

    name = name + '-gen' + str(item.age) + '-ang' + str(item.angle) + '-len' + str(item.dist) + '.' + item.filetype
    turt = item.turtle( initial_angle = item.initial_angle )
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
    print 'Releasing lsystem object...'

    for term in commands:
        if term in action:
            if len(action[term]) > 1:
                action[term][0](action[term][1])
            else:
                action[term][0]()

    turt.draw()
    turt.save( name, item.filetype )
    print 'Drawing saved as ' + name

#run all examples if not imported
if __name__== '__main__':
    for name, system in examples.iteritems():
        generator( name, system )
