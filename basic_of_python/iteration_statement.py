"""
in this file we will see 
1) for - ragne function  - used for knows ranges things interation 
2) while - used for unknown ranges 
3) continue 
4) break
5) switch statement - before 3.10 version of python no swtich statement is available 

"""

fruits=['bannana','apple','mango']
# for fruit in fruits:
    # print(fruit)

# use range function
for number in range(5):
    if number==1:
        continue
    if number==3:
        break
    # print(number)    


lang='javas'

match lang:
    case 'java':
        print("learn java in depth oky")
    case 'javascript':
        print("learn javascript in depth")
    case _:
        print("no match found")        