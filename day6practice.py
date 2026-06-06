#D6 (Saturday)  OOP inheritance, modules | First Gemini API call  ▣ Weekend 4h learning 
#Python topics Inheritance, super(), method overriding Encapsulation conventions 
#Standard library tour: os, sys, datetime, random, math Building your own modules, __name__ == '__main__' 
#GenAI topics Install Gemini Python SDK: pip install google-generativeai 
#Get a free API key from aistudio.google.com Store the key in environment variables — NEVER commit to Git 
#Make your first generate_content() call. Inspect token usage. 
#Free tools used today 


#  OOP inheritance, modules | First Gemini API call
#Inheritance, super(), method overriding Encapsulation conventions
class Animal:
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
            