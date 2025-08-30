# sum of n natural numbers
def sum_N(i):
    if i == 0:
        return 0
    return i + sum_N(i-1)
i = int(input())
s= sum_N(i)
print(s)

#factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
n = int(input())
result = fact(n)
print(result) 

# swap an array
a = [1,3,5,4,2, 7]
n = len(a)
def swap(i):
    if i>= n/2:
        return
    a[i], a[n-i-1] = a[n-i-1], a[i]
    swap(i+1)
swap(0)
print(a)


