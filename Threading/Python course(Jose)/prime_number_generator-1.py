from math import sqrt


def primeNumberGenerator(number):
    for i in range(2, number + 1):
        for x in range(2, int(sqrt(i)) + 1):
            if i % x == 0:
                break
        else:
            yield i


g = primeNumberGenerator(20)
for i in range(15):
    print(next(g))