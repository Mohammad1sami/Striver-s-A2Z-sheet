# Fibonacci number
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 4
result = fib(n)
print(result)



# # check whether a string is palindrome
string = "0P"
clean = ''.join(ch for ch in string if ch.isalnum())
new_string = clean.lower()
n = len(clean)
def isPalindrome(i):
    if i >= n//2:
        return True
    if new_string[i] != new_string[n-i-1]:
        return False
    return isPalindrome(i+1)
result = isPalindrome(0)
print(result)

#or

# (leetcode)
s="0P"
def isPalindrome(s):
    new_string = ""
    for c in s:
        if c.isalnum():
            new_string += c.lower()
    return new_string == new_string[::-1]
result = isPalindrome(s)
print(result)