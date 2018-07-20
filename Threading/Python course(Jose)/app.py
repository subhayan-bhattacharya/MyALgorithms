class FirstHundredGenerator:
    def __init__(self):
        self.number = 1

    def __next__(self):
        while self.number < 100:
            temp = self.number
            self.number += 1
            return temp
        raise StopIteration()

if __name__ == '__main__':
    gen = FirstHundredGenerator()
    for i in range(100):
        print(next(gen))