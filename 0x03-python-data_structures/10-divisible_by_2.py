#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_of_2 = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            mul_of_2.append(True)
        else:
            mul_of_2.append(False)

    return mul_of_2
