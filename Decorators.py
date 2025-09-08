def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
    print("Hi!")
    print("Hi!")

say_hi()  # Prints Hi! three times
say_hi()  # Prints Hi! three times
say_hi()  # Prints Hi! three times
say_hi()  # Prints Hi! three times
say_hi()  # Prints Hi! three times
