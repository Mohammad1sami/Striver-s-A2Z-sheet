def checkArmstrong(n):
    #write your code here !!!!!!!!!
    copy = n
    num_of_digit = len(str(n))
    armstrong_num = 0
    while(n>0):
        digit = n % 10
        cube = digit**num_of_digit
        armstrong_num = armstrong_num + cube
        n = n // 10
    if armstrong_num == copy:
        return True
    else:
        return False


    