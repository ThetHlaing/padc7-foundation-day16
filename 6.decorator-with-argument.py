## create a docorator to handle the parameters

def parameter_decorator(function):
    def wrapper(arg1,arg2):
        print(f"I received {arg1} and {arg2}")
        function(arg1,arg2)
    return wrapper

@parameter_decorator
def hello_world(arg1,arg2):
    print(arg1,arg2)

hello_world("Para1","Para2")
