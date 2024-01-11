class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.times = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.times += 1
        if self.count == self.times:
            raise StopIteration

        return self.times * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
