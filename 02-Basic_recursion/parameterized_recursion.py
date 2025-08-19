#print name n times
def print_name(n):
    name = "sami"
    if n <= 0:
        return
    print(name)
    print_name(n-1)
n = 5
print_name(n)

#print linearly from 1 to n
def print_num(num):
    if num > n:
        return
    print(num)
    print_num(num+1)

num = 1
n = 5
print_num(num)


# print from n to 1
def print_reverse(num):
    if num ==0:
        return
    print(num)
    print_reverse(num-1)
num= 5
print_reverse(num)




# use it when you want to carry forward an answer (like an accumulator).
# No need to combine results after return — the result is ready at the base case.