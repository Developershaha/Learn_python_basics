"""
learn loop in python
we have differnet type of 
1) foor looop 

syntax 

for varible_name in sequence

---- range funtion used for sequnce -- three type of range fucntiona are available 

range(stop) -- last index excluse 

range(start,stop) 

"""


#print number from 0 to 10 

# for number in range(11):
#     print(number)




#print only even number from 1 o 20
# for number in range(1,20):
#     if number%2!=0:
#         print("event numbers ",number)
#     else:
#         print(number)    


#print odd number from 1 to 20 


# for number in range(1,20):


# take one variable age if age is greateer then 18 or euql to then that person is elible for vote and if less then 18 if age goes behong 

# age 18 to 100less then or equal 
# age=0
# age_limit=100
# age_minimum=10

# if age>=age_minimum and age<=age_limit:
#     print("you are eliligible for vite ")
# elif age<=age_minimum and age>=0:
#     print("not eligible for vote because its age less then 18 ")    

# else:
#     print("please enter valid age ") 



#continue and break 
# for number in range(1,11):
#     if number >5:
#         break
#     print(number)


# print("after break rest of the code got excute ")



# print number from 1 to 10 dont print 5 and 7 
# count=0
# for number in range(1,11):
#     if number==5 or number==7:
#         continue
#     count=count+1;
#     print(number)

# print("count si ",count);    


#print loop from 10 to 1
# for number in range(10,0,-1):
#     print(number)

#while loop 

number=1

while number<=10:
    print(number)
    number+=1;