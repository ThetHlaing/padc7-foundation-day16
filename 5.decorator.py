##Create a split string decorator and apply to say hi function

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return "hello there"

print(say_hi())