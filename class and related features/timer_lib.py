import time
reps = 1000
replist = range(reps)

def timer (func, *args, **kwargs):
    start = time.clock()
    for i in replist:
        ret = func(*args, **kwargs)
    elapsed = time.clock() - start
    return (elapsed, ret)

timer()