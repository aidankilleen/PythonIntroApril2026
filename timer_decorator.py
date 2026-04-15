# timer_decorator.py

import time


def mytimer(func):
    def wrapper(*args, **kwargs):

        print (f"*args:", end="")
        print (args)
        print (f"**kwargs:", end="")
        print (kwargs)

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (f"duration: {end - start}")
        return result
    return wrapper

@mytimer
def slow_function(n):
    answer = sum(range(100000 * n))
    return answer

a = slow_function(n=50)

print (a)



