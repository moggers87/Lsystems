"""
This script will go if someone writes some documention :)
"""
from __future__ import print_function

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

Systems = namedtuple('Systems', 'axiom, rules, angle, initial_angle, dist, age, lsystem, turtle, filetype')

examples = {
    'tree': Systems(
        axiom='F',
        rules={'F': 'FF-[-F+F+F]+[+F-F-F]'},
        angle=22.5,
        initial_angle=-90,
        dist=10,
        age=5,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.LSystem,
        filetype='png',
    ),
    'weed': Systems(
        axiom='X',
        rules={'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF'},
        angle=25,
        initial_angle=-90,
        dist=10,
        age=5,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.LSystem,
        filetype='png',
    ),
    'sTri': Systems(
        axiom='F+F+F',
        rules={'F': 'F+F-F-F+F'},
        angle=120,
        initial_angle=0,
        dist=10,
        age=7,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.LSystem,
        filetype='png',
    ),

    'sTri2': Systems(
        axiom='F',
        rules={'F': 'G-F-G', 'G': 'F+G+F'},
        angle=60,
        initial_angle=-60,
        dist=10,
        age=7,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.LSystem,
        filetype='png',
    ),
    'stoch-weed': Systems(
        axiom='X',
        rules={'X': ['F-[[X]+X]+F[+FX]-X', 'F-[[X]+X]+F[+FX]-X', None], 'F': ['FF', 'FF', None]},
        angle=25,
        initial_angle=-90,
        dist=10,
        age=5,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.StochasticLSystem,
        filetype='png',
    ),
    'stoch-symtree': Systems(
        axiom='F',
        rules={'F': ['FF-[-F+F+F]+[+F-F-F]', 'FF+[+F-F-F]-[-F+F+F]']},
        angle=22.5,
        initial_angle=-90,
        dist=10,
        age=5,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.StochasticLSystem,
        filetype='png',
    ),
    'stoch-example': Systems(
        axiom='F',
        rules={'F': ['F[+F]F[-F]F', 'F[+F]F', 'F[-F]F']},
        angle=22.5,
        initial_angle=-90,
        dist=10,
        age=5,
        turtle=turtle.TurtlePIL,
        lsystem=lsystem.StochasticLSystem,
        filetype='png',
    )
}


def generator(name, item):
    print(name + "...")

    name = "{0}-gen{1}-ang{2}len{3}.{4}".format(name, str(item.age), str(item.angle), str(item.dist), item.filetype)
    turt = item.turtle(initial_angle=item.initial_angle)
    tree = item.lsystem(axiom=item.axiom, rules=item.rules)

    action_map = {
            'F': [turt.forward, item.dist],
            'G': [turt.forward, item.dist],
            '-': [turt.right, item.angle],
            '+': [turt.left, item.angle],
            '|': [turt.right, 180],
            '[': [turt.push],
            ']': [turt.pop]
         }
    noop_action = [lambda: None]

    for _ in range(item.age):
        tree.step()

    commands = str(tree)
    del tree
    print('Releasing lsystem object...')

    for term in commands:
        action = action_map.get(term, noop_action)
        action[0](*action[1:])

    turt.draw()
    turt.save(name, item.filetype)
    print('Drawing saved as {0}'.format(name))


#run all examples if not imported
if __name__== '__main__':
    for name, system in examples.items():
        generator(name, system)
