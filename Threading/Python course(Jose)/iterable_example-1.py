class FirstHundredGenerator:
    def __init__(self):
        self.number = 1

    def __next__(self):
        while self.number < 100:
            temp = self.number
            self.number += 1
            return temp
        raise StopIteration()

    def __iter__(self):
        return self

if __name__ == '__main__':
    print(sum(FirstHundredGenerator()))
    for i in FirstHundredGenerator():
        print(i)