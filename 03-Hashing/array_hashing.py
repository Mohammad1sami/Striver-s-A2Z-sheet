# Number hashing

n = int(input())
arr = list(map(int, input().split()))
hash_arr = [0] * 13  

for num in arr:
    hash_arr[num] += 1   

q = int(input()) 
for _ in range(q):
    number = int(input())
    print(hash_arr[number]) 



# character hashing
# (if lowercase subtract with "a" or if uppercase subtract with "A" or with both then create an array of 256 size and do not subtract anything)

s = input().strip()
hash_arr = [0] * 26

for ch in s:
    hash_arr[ord(ch) - ord('a')] += 1

q = int(input())
for _ in range(q):
    c = input().strip()
    print(hash_arr[ord(c) - ord('a')])
