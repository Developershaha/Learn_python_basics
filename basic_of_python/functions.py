"""


we will learn python function in python in this file oky 

1) function wihtout argument 
2) function with argument 
3) function with return statement 


we have two type fo function in pyton 
user defined 
inbuild functions

"""


def greet(): # def keyword used to define function after that fucntion name  this is no argument function
    print("hey hello from pyton")
greet()   



def add_numbers(num1,num2): #with argummetn i am sending two argument num1 and num2 and that accepting as a parameters 
    sum=num1+num2
    print(sum)
    return sum;

result=add_numbers(10,20)   

print(result)
