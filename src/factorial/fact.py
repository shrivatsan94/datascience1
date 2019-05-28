'''
Created on 28-May-2019

@author: Owner
'''
import sys

def fact(n):
    """
    Factorial function

    :arg n: Number
    :returns: factorial of n

    """
    if n == 0:
        return 1
    return n * fact(n -1)

def div(n):
    """
    Just divide
    """
    res = 10 / n
    return res


def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    main(5)
