def debug(func):
    def wrappper(*args,**kwargs):
        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}-{v}" for k,v in kwargs.items())
        print(f"Calling {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrappper









@debug
def namaste(name,  grettings = "jai shree krsna"):
    print(f"{name} - {grettings}")

namaste("rushil",grettings = "hello")
    
