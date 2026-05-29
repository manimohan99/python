# if / elif / else, comparison & logical operators 
#Here’s a combined tricky one:

#Input: age and income. Rule: Eligible for a loan if age ≥ 21 and income ≥ 30,000.

#If age < 21 → "Too young".If income < 30,000 but age ≥ 21 → "Insufficient income".

#Else → "Eligible".
"""
personage=int(input("enter age:"))
personincome=int(input("enter income"))
if personage < 21:
    print("too young")
elif personincome > 30000 and personage<21:
    print("in sufficent in come")
else:
    print("elgible for loan")
"""
#Write a program that checks if a number is divisible by both 3 and 5, only 3, only 5, or neither.
"""
num= int(input(" enter a number:\n"))

if num % 3 == 0 and num % 5 == 0:
    print("the number divisibale both")
elif num % 3 ==0:
    print("the number only divisibale by 3")
elif num % 5 ==0:
    print(" the number only divisibale by 5")
else:
    print(" the number not divisable both")
    """
    #Given a temperature value, print "Cold" if it’s below 10, 
    # "Warm" if it’s between 10 and 25, "Hot" if it’s above 25 — but make sure edge cases 
    # like exactly 10 or 25 are handled correctly.
""" 
temparatuer = float(input("Enter temperature: "))

if temparatuer < 10:
    print("Cold")
elif 10 <= temparatuer <= 25:
    print("Warm")
else:
    print("Hot")
    """
    #Write a program that checks if a year is a leap year
    # (divisible by 4, but not by 100 unless also divisible by 400).
"""
leap= int(input())
if leap % 4 == 0 and 100 !=0 or leap % 400:
    print ("it is a leap year")
else:
    print("its not a leap year")
    """
    
# Write a program that prints "Weekend" if today is Saturday or Sunday,
# else "Weekday".
"""
day = input("Enter day: ")

if day.lower() == "saturday" or day.lower() == "sunday":
    print("Weekend")
else:
    print("Weekday")
"""
#  programs on for/while/break continues and pass 
# for loop can be used when you know the iterations and its will be iterable 
# while loop can be used for when you dont know the iterations and 
# while loop will be iterable until given condition is true 
# the continue will be  skip the what if in the control flow 
# break immidiatly ends the loop 

#Write a program that:
#Loops through numbers 1–100.Skips numbers divisible by 2 (continue).
#Stops completely if a number divisible by 13 is found (break).
#For numbers divisible by 5, just put a placeholder (pass) instead of printing.Prints all other numbers.
"""
for i in range (1,100):
    if i %2 ==0:
        continue
    if i % 13==0:
        break 
    if i% 5 ==0:
        pass
    else:
        print(i)
"""
    #Write a program using a while loop that prints numbers from 1 to 10, 
    # but stops if the number is divisible by 7.
"""
num=1 
while num<=10:
    if num % 7 ==0:
        break
    print(num)
    num +=1
    """
# Use a for loop to print the factorial of a given number
# without using built‑in functions.
"""
n=int(input())
fact =1
for i in range(1,1+n):
    fact*=i
    print(fact)
    """
    
    #Generate the Fibonacci sequence up to 50 using a while loop.
"""
a,b =0,1
while a<=50:
     print(a)
     a,b=b,a+b
   """
#Write a program that keeps asking the user for input until they type "exit".
"""
while True:   # infinite loop
    user_input = input("Enter something (type 'exit' to stop): ")
    
    if user_input.lower() == "exit":  
        print("Program stopped.")
        break                          
    
    print("You entered:", user_input) 
"""
#Print all numbers from 1 to 20, but skip multiples of 3.
"""
for i in range(1,20):
    if i%3 ==0 :
        continue   
    print(i)
    """
#Use a for loop to iterate through characters in a string,
# but stop when you encounter a vowel.
"""
str =input(" enter a string:")
for i in str:
    if i.lower() in "aeiou":
        break 
    print(i)
    """ 
    #Defining functions, parameters, return values, 
    # default args Variable scope, docstrings 
    # functions : is reusable a block of code  its have parameters and return defalt values also 
    #Variable scope:  its is declaring a variable either in side the scope and out side the scope 
    #when you declare a varibale out side the scope its call globale variable and its accesed by key
    # Docstring : its generate a documentation inside the code and :__doc__

"""
def greet(name="guest"):
    return f"hello,{name}"

print(greet())
print(greet("python"))
"""
"""
# Function with multiple returns
def checknumber(n):
    if n>0:
        return "it is possitive number"
    elif n<0:
        return "its a negitive number "
    else:
         return 0
print(checknumber(100))

"""
class person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
        
print(person.__doc__)
obj =person("mani",23)
print(obj.name,obj.age)

# What is a Large Language Model? Tokens, training, prediction 
 # LLM :  llm stands for large lanugage model and its trained under massive data. 
 # and its predict next word in a sequence   examples: chagpt,geminiai,like that 
 # and its generate sentences and all those things how humans will generate
  
 # token: it is smallest unit of text 
 # llms are dont see raw sentences and its convert the sentences into tokens
 
 #training: learn to predict the next token given previous ones
  # how its will be trained 
"""
  1.input text broken into tokens
  2.model calculate next probabilites for the next token
  3. compare prediction with actual token
  4.adjust weights via backpropagation
 """
    # prediction
"""
    1.takes a sequence of tokens
    2.predict the most probable next token
    3.appends it to the sequence
    4.repeat until the output is complete 
    """