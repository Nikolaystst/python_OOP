def fibonacci():
    n_1 = 0
    n_2 = 1
    while True:
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2


generator = fibonacci()
for i in range(5):
    print(next(generator))
