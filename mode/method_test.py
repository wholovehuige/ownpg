from functools import reduce
import time
import functools

def nowTime():
    int2 = functools.partial(int,base=2)
    print(int2("1000000"))
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def log(prefix):
    def log_decorator(f):
        def wrapper(*args,**kwargs):
            print("[%s] %s()... %s" %(prefix,f.__name__,nowTime()))
            return f(*args,**kwargs)
        return wrapper
    return log_decorator


@log("DEBUG")
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

@log("INFO")
def add(x,y):
    return x+y

print(factorial(5))
print(add(1,4))



