from mydecorator import decorator_with_args

#@decorator_with_args
def say_hello(message):
    return message

print(say_hello("Hello"))