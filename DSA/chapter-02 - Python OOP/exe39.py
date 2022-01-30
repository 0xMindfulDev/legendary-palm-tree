"""
Develop an inheritance hierarchy based upon a Polygon class that has
abstract methods area( ) and perimeter( ). Implement classes Triangle,
Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
class, with the obvious meanings for the area( ) and perimeter( ) methods.
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectan-
gle, and Square, that have the appropriate inheritance relationships. Fi-
nally, write a simple program that allows users to create polygons of the
various types and input their geometric dimensions, and the program then
outputs their area and perimeter. For extra effort, allow users to input
polygons by specifying their vertex coordinates and be able to test if two
such polygons are similar."""

class Polygon(object):
    """abstract base class represented a generic polygon with n sides"""
    @abstractmethod
    def area(self):
        return NotImplementedError

    @abstractmethod
    def perimeter(self):...


class Triangle(Polygon):
    """Triangle class representing a triangle object. A concrete implementation 
    of polygon class with three sides."""

class Quadrilateral(Polygon):
    """A quadrilateral is a Polygon with four sides"""

class Pentagon(Polygon):
    """A Pentagon is a Polygon with five sides"""

class Hexagon(Polygon):
    """A Hexagon is a Polygon with six sides"""

class Octagon(Polygon):
    """An Octagon is a Polygon with eight sides"""

class IsoscelesTriangle(Triangle):
    """Isosceles triangle is a type of triangle"""

class EquilateralTriangle(Triangle):
    """An Equilateral Triangle is a triangle with three equal sides"""

class Rectangle(Quadrilateral):...

class Square(Polygon):...