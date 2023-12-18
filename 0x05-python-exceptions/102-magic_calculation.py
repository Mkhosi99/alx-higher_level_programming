#!/usr/bin/python3
def magic_calculation(a, b):
    answer = 0
    for x in range(1, 3):
        try:
            if (x > a):
                raise Exception("Too far")
            else:
                answer += (a ** b) / x
        except:
            answer = b + a
            break
    return (answer)
