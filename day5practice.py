"""D5 (Friday)  OOP part 1 | Tour the free LLM playgrounds 
5h learning  +  4h team support 
Python topics 
Class definition, __init__, instance vs class attributes 
Instance methods, self 
__str__ and __repr__ 
Creating and using objects """
#  class is a blueprint for creating objects.it defines a set of attributes 
#init is a special method that is called when an object is created it is used to 
# initialize the attributes of the object

"""class Definition:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Definition(name={self.name}, age={self.age})"
    
obj = Definition("mani", 23)
print(obj)"""

#instance vs class attributes
"""class Example:
    class_attribute = "Iam a class attribute"
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute
obj1 = Example("Iam an instance attribute")
print(obj1.class_attribute)  # """

#Instance methods, self 
#__str__ and __repr__ 
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
person1 = Person("Alice", 30)
print(person1)  
"""
#__str__ and __repr__ 
#Creating and using objects 
class Car:
     def __init__(self,make,model,year):
         self.make=make
         self.model=model
         self.year=year
     def __str__(self):
         return f"Car(make={self.make}, model={self.model}, year={self.year})"
car1 = Car("Toyota", "Camry", 2020)
print(car1)