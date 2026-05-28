"""  #store and print values

 name = "mani"
 age =22
 course = "python"

print(name)
 print(age)
print(course)
"""

# # SWAP TWO VARIABLES WITHOUT THIRD VARIABLE
"""
# a =10
# b=15
 
# a,b = b,a 

# print(a,b)

# # DYNAMIC VARIABLE UPDATE 
# score =50
# score +=10
# score -=5
# print(score)

# # MULTIPLE ASSIGNMENTS

# a = b = c=100
# print(a+b+c)
"""

# # strings Count charectors 
# """
# text = "python"
# print(len(text))

# """

# # check palindrome 
# """
# word ="madam"

# if word == word[begin:end:step]:
#     print("palindrome")
# else:
#     print("Not Palindrome")
#     """
    # COUNT VOWELS IN A STRING  """"
"""
string = "manimohan"
count = 0
for i in string:  
    if i in "aeiou":
        count += 1

print(count)
"""

#  remove duplicate eliments
"""
text ="program"
result=""
for i in text:
    if i not in result:
        result += i


print (result)

"""
# PROBLEMS ON NUMBERS 
"""
n =10
m=60
c=80
print(n**2)
print(max(n,m,c))
"""

# reverse number without using inbuilt method 
"""
num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse *10 +digit
    num =num//10
    
print(reverse)
    """
   # booleans
"""  
x= 5
print(x > 6 and x<10 )
print(x < 6 and x<10 )

"""
"""
a = True
b = False
print(not(a and b) or b)
"""

# Type conversion/ coecion
"""
num ="100"

print(int(num)+25)
 
 
price =99.99
print(int(price))
"""
"""
a="5"
b= 2
print(int(a)*b)

"""

# F strings 
"""
a=10
b=15
name ="manimohan"
score =95
print(f"name is {name},\n and  he is score {score}")
print(f"sum ={a+b}")

"""
num =5
print(f"squre of num is {num**2},qube of num is {num**3}")

# String operations

#replace methond
"""
text= " i like java"
print(text.replace("java","python"))

text ="python programing"
print(text.strip().upper().replace("python" ,"developer"))
"""
# Slicing methods 
"""
text ="program"
print(text[:3])
print(text[:-3])

text ="python"
print(text[::-2])
"""
a = int(input(" enter first number :"))
b = int(input(" enter first number :"))

print(f"adition ={a+b}")
print(f"div =  {a/b}")
print(f"mul =  {a*b}")
print(f"sub=  {a-b}")