import random

max_digit = 6

def twentyOneSum(maxDigit):
    equal_21 = False
    while not equal_21:
        int_list = []
        for i in range(4):  # Change the range to 4
            n = random.randint(1, maxDigit)
            int_list.append(n)

        if sum(int_list) == 21:
            equal_21 = True
            s = map(str, int_list)
            number = int(''.join(map(str, int_list)))
            print(number)
            

twentyOneSum(max_digit)
