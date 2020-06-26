class MobileDevice:

    def __init__(self, screen, connector):
        self.screen = screen
        self.connector = connector

    def printInfo(self):
        return "screen: " + self.screen + ", connector " + self.connector


    private doSomethind()

class Smartphone(MobileDevice):
    def printInfo(self):
        return "Smartphone " + super(Smartphone, self).printInfo()


class Tablet(MobileDevice):
    def printInfo(self):
        return "Tablet " + super(Tablet, self).printInfo()


if __name__ == '__main__':
    for device in [
        Smartphone("lcd", "3g"),
        Tablet("oled", "3g/wi-fi")
    ]:
        print(device.printInfo())
