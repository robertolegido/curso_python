# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:28:06 2018

@author: roberto
3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

21

which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.
"""

i = 0
j = 0
end = 6
for i in range (0, end+1):
    print("El valor de indice es: ", i)
    print("El valor de acumulado es: ", j)
    j = i + j

print(j)