import time

def gen():
    for i in range(10):
       x = (yield i)
       print("inside function =", x)


def gen_X():
    for i in range(10):
       print("inside function =", i)
    return i

GG=(x**2 for x in range(10))   #generator?

G = gen()

print(next(G))
print(G.send(77))
print(G.send(88))
print(next(G))

print("Funkcja wlaczona normalnie", gen())

time.sleep(0.1)


# print("to nie generator", next(gen_X()))

print("a to co ?", next(GG))
print("a to co ?", next(GG))
print(GG)

print("generator", type((x**2 for x in range(10))))
print("set", type({x**2 for x in range(10)}))
print("dict", type({x: x**2 for x in range(10)}))
print("list", type([x**2 for x in range(10)]))

