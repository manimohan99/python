#D6 (Saturday)  OOP inheritance, modules | First Gemini API call  ▣ Weekend 4h learning 
#Python topics Inheritance, super(), method overriding Encapsulation conventions 
#Standard library tour: os, sys, datetime, random, math Building your own modules, __name__ == '__main__' 
#GenAI topics Install Gemini Python SDK: pip install google-generativeai 
#Get a free API key from aistudio.google.com Store the key in environment variables — NEVER commit to Git 
#Make your first generate_content() call. Inspect token usage. 
#Free tools used today 


#  OOP inheritance, modules | First Gemini API call
#Inheritance, super(), method overriding Encapsulation conventions

# inheritance is a fundamental concept in object-oriented programming (OOP) that allows a 
#ew class (called a child or subclass) to inherit attributes and methods from an existing class

"""class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof!"

object = Dog("Buddy")
print(object.speak())
            """
          #  super(), method overriding Encapsulation conventions 
"""class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Bike(brand={self.brand}, model={self.model})"


class SportBike(Bike):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def __str__(self):
        return f"SportBike(brand={self.brand}, model={self.model}, speed={self.speed})"


sport_bike = SportBike("Yamaha", "R1", 300)
print(sport_bike)
                    """
                    
 #Standard library tour: os, sys, datetime, random, math Building your own modules, __name__ == '__main__' 
 
"""class Calculator:
     def add(self,a,b):
         return a+b
     def subtract(self,a,b):
         return a-b
     def multiply(self,a,b):
         return a*b
     def divide(self,a,b):
         if b!=0:
             return a/b
         else:
             return "cannot divide by zero"
         if __name__=='__main__':
             calc=Calculator()
             print(calc.add(10,5))
             print(calc.subtract(10,5))
             print(calc.multiply(10,5))
             print(calc.divide(10,5))"""
             
             
#GenAI topics Install Gemini Python SDK: pip install google-generativeai 
#Get a free API key from aistudio.google.com Store the key in environment variables — NEVER commit to Git 
#Make your first generate_content() call. Inspect token usage.

#ncapsulation conventions
#encapsulation is the process of hiding the internal details of an object and only exposing a public interface. In Python, we can use name mangling to create private attributes and methods 
class Bankaccount:
    def__init__(self,account_number,balance)
    self.__account_number=account_number
    self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited{amount}.new balance is {self.__balance}")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew {amount}.new balance is {self.__balance}")
        else:
            print("Invalid amount or insufficient funds")
        
