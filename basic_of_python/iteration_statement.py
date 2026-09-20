"""
in this file we will see 
1) for - ragne function  - used for knows ranges things interation 
2) while - used for unknown ranges 
3) continue 
4) break

"""

fruits=['bannana','apple','mango']
for fruit in fruits:
    print(fruit)

# use range function
for number in range(5):
    if number==1:
        continue
    if number==3:
        break
    print(number)    