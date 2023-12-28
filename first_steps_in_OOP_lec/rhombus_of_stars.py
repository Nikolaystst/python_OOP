def pyramid(range_1):
    for i in range(1, range_1 + 1):
        print(" " * (range_1 - i), end="")
        print("* " * i)


def reversed_pyramid(range_1):
    for i in range(range_1 - 1, 0, -1):
        print(" " * (range_1 - i), end="")
        print("* " * i)


def full_pyramid(range_1):
    pyramid(range_1)
    reversed_pyramid(range_1)


num = int(input())
full_pyramid(num)
