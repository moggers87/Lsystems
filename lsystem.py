import re

class LSystem(object):
    """LSystem is iterable and string-like. It is good."""

    def __init__( self, axiom, rules ):
        """Set initial string and compile rules"""

        self.string = axiom
        self.rules = rules
        self.regex = re.compile( "|".join( map( re.escape, rules ) ) )

    def step( self ):
        """Generate the next generation"""
        self.string = self.regex.sub( self.__match, self.string )

    def __match( self, match ):
        return self.rules[ match.group( 0 ) ]

    def __len__( self ):
        return len( self.string )

    def __str__( self ):
        return self.string

    def __getitem__( self, index ):
        return self.string[ index ]

