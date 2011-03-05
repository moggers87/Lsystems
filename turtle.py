import math
from PIL import Image, ImageDraw

class Turtle( object ):
    """Turtle base object"""
    def __init__( self, initial_position=( 0, 0 ), initial_angle=0 ):
        self.angle = math.radians(initial_angle)
        self.pen = 1
        self.positions = [ ( initial_position, self.pen ) ]
        self.stack = []

        self.y_max = 0
        self.y_min = 0
        self.x_max = 0
        self.x_min = 0


    def forward( self, length ):
        """Move turtle forward and then append position and pen status to an internal list"""
        x, y = self.positions[ -1 ][ 0 ]
        y = y + math.sin( self.angle ) * length
        x = x + math.cos( self.angle ) * length

        if x > self.x_max:
            self.x_max = x
        elif x < self.x_min:
            self.x_min = x

        if y > self.y_max:
            self.y_max = y
        elif y < self.y_min:
            self.y_min = y

        self.positions.append( ( ( x, y ), self.pen ) )

    def left( self, angle ):
        """Decrease heading by angle in degrees"""
        angle = math.radians( angle )
        self.angle = ( self.angle - angle ) % ( 2.0 * math.pi )

    def right( self, angle ):
        """Increase heading by angle in degrees"""
        angle = math.radians( angle )
        self.angle = ( self.angle + angle ) % ( 2.0 * math.pi )

    def pen_up( self ):
        """Lift pen off canvas"""
        self.pen = 0

    def pen_down( self ):
        """Put pen back on canvas pen"""
        self.pen = 1

    def push( self ):
        """Push position and heading to stack"""
        self.stack.append( ( self.positions[ -1 ][ 0 ], self.angle ) )

    def pop( self ):
        """Pop postion/heading from stack"""
        popped = self.stack.pop()
        self.positions.append( ( popped[0], 0 ) )
        self.angle = popped[1]

    def calc_size( self, border=5 ):
        """Calculate the size of a canvas and add a border"""
        self.border = border
        self.size = ( border * 2 + self.x_max - self.x_min, border * 2 + self.y_max - self.y_min )

class TurtlePIL( Turtle ):
    """PIL version of turtle"""
    def __init__( self, initial_position=( 0, 0 ), initial_angle=0 ):
        super( TurtlePIL, self ).__init__( initial_position, initial_angle )

    def draw( self ):
        """Render lines onto canvas"""
        self.calc_size()
        size = ( math.trunc( math.ceil( self.size[0] ) ), math.trunc( math.ceil( self.size[1] ) ) )
        self.image = Image.new( 'L', size )
        draw = ImageDraw.Draw(self.image)
        prev = None

        for xy, pen in self.positions:
            x = ( xy[0] - self.x_min ) + self.border
            y = ( xy[1] - self.y_min ) + self.border
            if prev is not None and pen is 1:
                draw.line( [ prev[0], ( x, y ) ], 255 )

            prev = ( ( x, y ), pen )

    def save( self, file_name, file_type=None ):
        """Save to a file

        If file_type is not given, it will be determined from file_name
        """
        self.image.save( file_name, file_type )

class TurtleSVG( Turtle ):
    """SVG version of turtle"""
    pass
