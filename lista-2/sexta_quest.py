class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def reflect_x(self):
        self.y *= -1
        return self

    def slope_from_origin(self):
        return (self.y*1.0)/self.x


print(Point(4, 10).slope_from_origin())
