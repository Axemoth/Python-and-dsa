def debug(func):
    def wrappper(*args,**kwargs):
        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}-{v}" for k,v in kwargs.items())
        print(f"args {args} , kwargs {kwargs}")
        result = func(*args,**kwargs)
        return result
    return wrappper









@debug
def namaste(name,  grettings = "jai shree krsna"):
    print(f"{name} - {grettings}")

namaste("rushil",grettings = "hello")
    
