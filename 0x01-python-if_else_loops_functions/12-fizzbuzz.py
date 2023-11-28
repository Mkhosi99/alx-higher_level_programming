#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100
    For multiples of three, print Fizz
    For multiples of five, print Buzz
    For multiples of three and five, print FizzBuzz
    """
    for numb in range(1, 101):
        if numb % 3 == 0 and numb % 5 == 0:
            print("FizzBuzz ", end="")
        elif numb % 3 == 0:
            print("Fizz ", end="")
        elif numb % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numb), end="")
