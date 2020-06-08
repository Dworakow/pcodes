#dekoratory + klasy
import time


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime=0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(self, *args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print ('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

class praca:
    @timer
    def __init__(self, name, staz, kasa):
        self.name = name
        self.staz = staz
        self.kasa = kasa
        # print(self)

    def __str__(self):
        return '[Praca: %r, %dy, %d PLN]' % (self.name, self.staz, self.kasa)

class hobby(praca):
    def __init__(self, name, staz):
        praca.__init__(self, name, staz, kasa = 0)

    def __str__(self):
        print("dshfsjhfjdfhs")# return '[Hobby: %r, %dy]' % (self.name, self.staz)

def funkcja(N):
    return [x*2 for x in range(N)]


if __name__ == '__main__':
    obecna = praca('Nokia', 2, 4500)
    przyszla = praca('Atos', 0 , 10)
    przeszla = praca('SSAB', 6 , 3500)
    teraz = hobby('Python',1)
    funkcja(20000000)
    funkcja(20000000)
    funkcja(20000000)



