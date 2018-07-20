from math import sqrt
class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.n = 2

    def __next__(self):
        for i in range(self.n,self.stop):
            for x in range(2, int(sqrt(i)) + 1):
                if i % x == 0:
                    break
            else:
                self.n = i + 1
                return i
        raise StopIteration()


if __name__ == '__main__':
    gen = PrimeGenerator(50)
    for i in range(20):
        print(next(gen))