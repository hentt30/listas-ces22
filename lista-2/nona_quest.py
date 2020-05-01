import math

class Shape:
    geometric_type = "Generic Shape"


    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self,ratio,topleft):
        print(f"Plotting at {topleft}, ratio {ratio}.")


class Polygon(Shape,Plotter):
    geometric_type = "Polygon"

class RegularPolygon(Polygon):
    geometric_type = "Regular Polygon"

    def __init__(self,side):
        self.side=side

class Pentagon(RegularPolygon):
    geometric_type = "Pentagon"

    def area(self):
        h = self.side/(2*math.tan(math.pi/5))
        a = (self.side)*h/4
        return 10*a

class Heptagon(RegularPolygon):
    geometric_type = "Heptagon"

    def area(self):
        return (7.0/4)*self.side*self.side*(1.0/math.tan(math.pi/7))


print("###### MRO DO PENTAGONO ######")
print(Pentagon.mro())

print("##### MRO DO HEPTAGONO #######")
print(Heptagon.mro())

