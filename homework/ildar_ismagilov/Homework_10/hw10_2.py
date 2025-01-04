def repeat_me(count):
    def inner_decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)

        return wrapper

    return inner_decorator
