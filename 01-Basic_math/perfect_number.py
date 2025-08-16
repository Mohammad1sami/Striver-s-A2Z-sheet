class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        list1 = []
        import math
        if num <= 1:
            return False
        for i in range(1, int(math.sqrt(num))+1):
            if num % i == 0:
                list1.append(i)
                list1.append(num//i)
        total = sum(list1) - num
        if num == total:
            return True
        else:
            return False