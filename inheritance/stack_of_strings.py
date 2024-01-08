from typing import List


class Stack1:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self) -> bool:
        return True if self.data == [] else False


class Stack11(Stack1):
    def push(self, element: str) -> None:
        self.data.append(element)


class Stack2(Stack11):
    def pop(self) -> str:
        return self.data.pop()


class Stack3(Stack2):
    def top(self) -> str:
        return self.data[-1]


class Stack(Stack3):
    def __str__(self) -> str:
        return f"[{', '.join(self.data[::-1])}]"
