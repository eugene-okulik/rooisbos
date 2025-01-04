def finish_me(func):
    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper
