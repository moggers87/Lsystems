"""
Copyright (C) 2011 Matt 'moggers87' Molyneaux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import re
from random import choice


class LSystem(object):
    """LSystem is iterable and string-like. It is good."""

    def __init__(self, axiom, rules):
        """Set initial string and compile rules

        rules must be a dict of strings"""

        self.string = axiom
        self.rules = rules
        self.regex = re.compile("|".join(map(re.escape, rules)))

    def step(self):
        """Generate the next generation"""
        self.string = self.regex.sub( self.match, self.string )

    def match(self, match):
        """Override this method if you want to change behaviour on matching symbol"""
        return self.rules[match.group(0)]

    def __len__(self):
        return len(self.string)

    def __str__(self):
        return self.string

    def __getitem__(self, index):
        return self.string[index]


class StochasticLSystem(LSystem):
    """Non-deterministic version of LSystem"""

    def __init__(self, axiom, rules):
        """Set initial string and compile rules

        rules must be a dict of non-empty lists. Each list must contain strings
        or Nones, the number of items affecting the probability of that
        replacement being chosen. If a None is chosen, no replacement is made."""
        super(StochasticLSystem, self).__init__(axiom, rules)

    def match(self, match):
        """Override this method if you want to change behaviour on matching symbol"""
        replacement = choice(self.rules[match.group(0)])

        if replacement is None:
            replacement = match.group(0)

        return replacement
