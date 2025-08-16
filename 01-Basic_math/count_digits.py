# count the number of digits
n = 12544 #sample input
digit = 0
if n == 0:
    digit = 1
while(n>0):
    n = n//10
    digit  += 1
print(digit)
        #  or
import math
digits = int(math.log10(n)+1)
print(digits)