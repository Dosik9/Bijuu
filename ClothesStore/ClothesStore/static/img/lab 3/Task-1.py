#Task1
#List
    #a
Numbers=list(range(22,33))
print(Numbers)

    #b
cubes_numbers=list(i**3 for i in range(1,7))
print(cubes_numbers, end=' ')
    #c
even_num=list(range(2,13,2))
for i in even_num:
    even_sqr=[i**2]
    print(even_sqr, end=" ")
    #d
even_or_odd=["Even" if i%2==0 else "Odd" for i in range (1,21)]
print(even_or_odd, end=" ")
    #e
characters_numbers=[i for i in range(1,21) if i%2==0 if i%3!=0]
print(characters_numbers)
#     #f
from random import randint
matrix=[randint(10,99) for i in range(3) for j in range (3)]
print(matrix)


#Set
    #a
a=(range(0,15))
b=[]
for i in a:
    if i%2==0:
        continue
    else:
        b.append(i)
b=set(b)
print(b)
    #b
s_e_t_2={(i,j) for i in range(5) for j in range(5) if i != j}
print(s_e_t_2)


#Dictionary
    #a
dict1={i:i**2 for i in range(1,10)}
print(dict1)
    #b
dict2={i:[j**2 for j in range(i,i+i)] for i in range(7,9)}
print(dict2)
    #c
dict3={i:'Even' if i%2==0 else "Odd" for i in range(10) }
print(dict3)


#Lambda functions
    #a
calculate_power=(lambda x:x**2)(4)
print(calculate_power)
    #b
compare1=(lambda a, b, c:max(a, b, c))(1, 8, 7)
print(compare1)
    #c
# compare2=(lambda x, y, z: !max(x,y,z)and !min(x,y,z))(1,8,7)
# # print(compare2)
    #d
import math
sqrt_number=[(lambda x: math.sqrt(x))(x)for x in range(9,3,-1)]
print(sqrt_number)
#     #e
# with_condition=[(lambda x:x if x%3==0)(x)for x in range(0,31,2)]
# print(with_condition)


#map
    #a
def sqr(x):
    return x*x
list1=list(range(10,15))
print(list(map(sqr, list1)))
    #b
def formula(x, y):
    return (x+y)*(abs(x-y))
list_x=list(range(2,12))
list_y=list(range(10,20))
print (list(map(formula,list_x,list_y)))


#filter
    #a
a=list(range(2,19))
b=list(filter(lambda x: x%2==0,a))
print(b)
    #b
list2=list(range(100))
def condition(x):
    if(x%3==0 and x%5!=0):
        return x
print(list(filter(condition,list2)))
