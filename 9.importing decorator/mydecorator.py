def decorator_with_args(function):
    def wrapper(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function(*args)
    return wrapper