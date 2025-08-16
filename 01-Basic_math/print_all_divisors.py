class Solution:
    def print_divisors(self, N):
        import math
        divisor = set()
        for i in range(1 , int(math.sqrt(N)) + 1):
            if N % i == 0:
                divisor.add(i)
                divisor.add(N//i)
        divisor = sorted(divisor)
        print(*divisor, end= ' ')