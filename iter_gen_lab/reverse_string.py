def reverse_text(text: str):
    final = list(text)
    while final:
        n = final.pop()
        yield n


for char in reverse_text("step"):
    print(char, end='')
