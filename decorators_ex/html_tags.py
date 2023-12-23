def tags(str_1):
    def decorator(func):
        def wrapper(*args):
            return f"<{str_1}>{func(*args)}</{str_1}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
