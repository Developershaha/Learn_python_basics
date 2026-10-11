"""
in this file we will learn about the list oky 
1) what is list - order mutiable collection that can store hetrogenoud data 
list allow duplicate element 
list is immutable - mutable means can be change existing data. structure
accessing elemenet usign index base we have circular indexing staring from 0 and ending from -1 
what if we are trying to access index out of range 
array out of range index error we will get IndexError: list index out of range

len() --- > function we can use to get the length of the list 
adding element we can use append function 
"""

names=['shahaji','koknae']


names.append("dipali") # append use to add single element at the last of the list  entire object use as at one index
names.extend(['ram','sham']) # append use to add multiple in the last index oky  --- this is copy and created new 
# print(names[5]) -- get the errro list index out of range error 

names.insert(10,"hey i am new inserted") # insert used at specific index 

names.remove("sham") # used to remvoe first matching element  -- if not get that gives error 
print(names)

