# list =[10,10,15,10,20] -----> 10 -3 , 15-1,20-1 --- key value dictory 


list =[10,10,15,10,20] # defined list 

occurance={} # defiend empty dictionary 

"""
{

"10":3,
"15":1,
"20":1
}

occurance["10] ---- 3
"""

for key in list:
    # print(key)
    if key in occurance: # we have apply if stement her. 10  {"10":3,"15":1}  
        occurance[key]=occurance[key]+1
    else:
        occurance[key]=1     


print(occurance)