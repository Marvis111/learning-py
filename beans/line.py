
class Line(object) :
    """
    This allows you to do some cool stuffs with lines and cordinates
    """

    def __init__(self, cord1:tuple = (0,0), cord2 = (0,0)) -> None:
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self) :
        """
        This method calculates the distance between the two points.
        """
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)

    def slope(self) :
        """
        This method calculates the slope of the line joining the cordinates
        """
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (
            (y2 - y1)/(x2 - x1)
        )


li = Line(cord1=(0,0),cord2=(2,1))

print(li.distance())
print(li.slope())