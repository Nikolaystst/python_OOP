class vowels:
    def __init__(self, txt: str):
        self.txt = txt
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.newtxt = [l for l in self.txt if l.lower() in self.vowels]
        self.start = -1
        self.end = len(self.newtxt) - 1
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.current += 1
            if self.current > self.end:
                self.current = self.start
                raise StopIteration
            return self.newtxt[self.current]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
