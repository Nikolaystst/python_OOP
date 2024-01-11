class sequence_repeat:
    def __init__(self, txt: str, times: int):
        self.txt = txt
        self.times = times
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.times:
            self.count = -1
            raise StopIteration
        return self.txt[self.count % len(self.txt)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
