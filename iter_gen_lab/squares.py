def squares(num):
    less = 1
    while less <= num:
        yield less * less
        less += 1


print(list(squares(5)))
