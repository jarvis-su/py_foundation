import math
import random

def bacis_number():
    n1 = 123 + 222
    n2 = 1.5 * 4
    n3 = 2**100
    n4 = len(str(n3))
    print(n1)
    print(n2)
    print(n3)
    print(n4)

def basic_math():
    print(math.pi)
    print(math.sqrt(87))

def basic_random():
    n1 = random.random()*100
    n2 = random.choice([1,2,3,4,5,6,7,8,9,0])
    print(n1)
    print(n2)

if __name__ == "__main__":
    bacis_number()
    basic_math()
    basic_random()
