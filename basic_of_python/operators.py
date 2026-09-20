# learn python operator in this file oky 

"""

we have different different type of operator in python


1) arithmatic 
2) assignment 
3) comparison
4) logical && || ! 
5) membership is and is not 
6) identity operator - check refer to which memory 
7) operator precedancy - follow brodmac rule oky 
"""


# membership operator in and not in 
# check wheather value is present or not in the given sequence
fruits=["apple","bannana"];
# print("mango" not in fruits) #true
# print("apple" in fruits) #true

# identity operator 
# check wheather the two variable refer to the same object or not in the memory 
number=[1,2,3]
number1=number
number2=[1,2,3]

# print(number is number1) # refer to the same memory using is identity operator we can get the value is refering or not
# print(number is not number2) # true content is same but not refering to the same memory oky 

# if we want to check content in the object or reference then use == 

print(number1==number)
print(number==number2)
print(number1==number2)

# all above statement returns true oky 

# precedence operator means which operaton get change first to excute 
