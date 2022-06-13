
class Person(object) :
    """
        This helps in creating class components
    """
    #class object attribute
    
    level = '300'

    age = 18

    def __init__(self,age:int or None = None,sex = 'male',name = 'Marvellous',) -> None:
        if age != None :
            assert type(age) == int ,' Age has to be integer'
        self.name = name
        self.sex = sex
        print(age,sex)
        

"""samp = Person(sex='female',age=12,name='Tony Stak')

print(samp.name)
print(samp.age)
print(samp.sex)"""

class Circle(object) :

    pi = 3.142
    def __init__(self, radius:int = 1) -> None:
        assert type(radius) == int , 'Radius has to be an integer'
        self.radius = radius
        
        self.perimeter = self.radius * 2 * Circle.pi

    def area(self) : 
        """
        This method allows you to calculate the area of the circle.
        """
        return Circle.pi * (self.radius)**2

    def resetRadius(self,newradius:int):
        """
        This method allows you to reset the radius of the circle
        """
        assert type(newradius) == int , 'Radius has to be an integer'
        self.radius  = newradius


c = Circle(radius=6)
print(c.area())
print(c.perimeter)
