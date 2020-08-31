x = 99

def selector():
    import __main__
    print("main", __main__.x)
    x = 88
    print("local", x)

selector()

print('-' * 33)

def saver(v, x=[]):
    x.append(v)
    print(x)

saver(1, [])
saver(2)
saver(3, [])
saver(4)

def saver2(x=[]):
    x.append(99)
    print(x)

print('-' * 33)
saver2([2])
saver2()
saver2([])
saver2()
saver2([3])
saver2()
