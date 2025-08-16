def check_prime(num):

    # write your code logic here !!!
    import math
    if num ==1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
            break
    else:
        return True