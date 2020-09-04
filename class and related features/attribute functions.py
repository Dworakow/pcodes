
class Mycolor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, item):
        if item == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif item == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green, self.blue
            )
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == "rgbcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        super().__setattr__(key, value)


    def __dir__(self):
        return ("red", "blue", "green", "rgbcolor", "hexcolor")

def main():

    cls=Mycolor()

    print(cls.rgbcolor)
    print(cls.hexcolor)

    cls.rgbcolor = (125,200, 86)

    print(cls.rgbcolor)
    print(cls.hexcolor)

    print(cls.red)

    print(dir(cls))

main()