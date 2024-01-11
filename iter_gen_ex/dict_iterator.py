from typing import Dict


class dictionary_iter:
    def __init__(self, dict_1: Dict):
        self.dict_1 = dict_1
        self.final = [k for k in self.dict_1.items()]
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == len(self.final):
            raise StopIteration
        return self.final[self.count]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
