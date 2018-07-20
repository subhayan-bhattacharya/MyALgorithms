class AnotherIterable:
    def __init__(self):
        self.cars = ['Octavia', 'Superb', 'Eon']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

if __name__ == '__main__':
    for car in AnotherIterable():
        print(car)
    print(f'Checking length : {len(AnotherIterable())}')