import math


def area(r):
    a = 3.1412 * math.pow(r, 2)
    return a


def print1(a):
    print('The area of circle with radius', '{:.2f}'.format(n), 'is', '{:.2f}'.format(a))


n = float(input("Enter the radius: "))
print1(area(n))
