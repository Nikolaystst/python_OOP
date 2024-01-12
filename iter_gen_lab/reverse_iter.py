from typing import List


class reverse_iter:
    def __init__(self, lst: List[int]):
        self.lst = lst
        self.start = len(self.lst)
        self.end = 0
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.current -= 1
            if self.current < self.end:
                self.current = self.start
                raise StopIteration
            return self.lst[self.current]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
