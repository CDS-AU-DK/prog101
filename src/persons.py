"""
Add description of classes and sub-classes in script ...

"""

class Person:
    """ A person class
    Input:
        name: str variable
        age: int, numerical variable
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def says_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
    
    def lie_about_age(self, liefactor = 0.8):
        print(f"Hello, my name is {self.name} and I am {int(self.age * liefactor)} years old")

class Researcher(Person):
    def __init__(self, title=None, area=None, **kwargs):
        super(Researcher, self).__init__(**kwargs)
        self.title = title
        self.area = area
        # print(kwargs)
    
    def talks_research(self):
        print(f"Hello, {self.title} {self.name} likes {self.area}")
        
if __name__=="__main__":
    pass