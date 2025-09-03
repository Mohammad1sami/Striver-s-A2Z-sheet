# Number Hashing
n = int(input())  
arr = list(map(int, input().split()))

hash_map = {}
for num in arr:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1

q = int(input())
for _ in range(q):
    number = int(input())
    print(hash_map.get(number, 0))   


# Character Hashing
s = input().strip()

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

q = int(input())
for _ in range(q):
    c = input().strip()
    print(freq.get(c, 0))

