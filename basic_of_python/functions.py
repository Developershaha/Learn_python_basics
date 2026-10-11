"""


we will learn python function in python in this file oky 

1) function wihtout argument 
2) function with argument 
3) function with return statement 


we have two type fo function in pyton 
user defined 
inbuild functions



also we have different different type of fucntion that we can use oky 

1)position base argument 
2)keywords argumenet 
3) default arguments 
4) 

"""


def greet(): # def keyword used to define function after that fucntion name  this is no argument function
    print("hey hello from pyton")
greet()   



def add_numbers(num1,num2): #with argummetn i am sending two argument num1 and num2 and that accepting as a parameters 
    sum=num1+num2
    # print(sum)
    return sum;

result=add_numbers(10,20)   

# print(result)


# ## types of function in python 1) position arguments 

# def introduce(name,age):
#     print(f"hey my name is {name} and age is {age}")


# introduce("shahaji",27)    


# ## keyword argument function type oky 

# print("keyword argument function type")

# introduce(age=29,name="akash")


# ## Default arguement type function

# print("default argument type function ")

# def greet(name="shahaji"):
#     print(f"hey good morging {name}")

# greet()    


# greet("akash")

count=1
def globalFun():
    global count
    count+=1
    print(count)

globalFun()

print(count)

