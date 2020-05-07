class Point:
    def __init__(self, x, y, unit_size = 8):
        self.x = x
        self.y = y
        self.__unit_size = unit_size
        self.__actual = None

    def apply(self, direction):
        return Point(
            self.x + direction.value[0],
            self.y + direction.value[1])

    def add(self, x, y):
        return Point(self.x + x, self.y + y)
    
    def actual(self):        
        if self.__actual == None:
            self.__actual = Point(
                Px(self.x, self.__unit_size).actual(),
                Px(self.y, self.__unit_size).actual())
        return self.__actual

class Px:
    def __init__(self, pixel, unit_size = 8):
        self.value = pixel
        self.__unit_size = unit_size
    
    def actual(self):
        return self.value * self.__unit_size
    
    def add(self, pixel):
        self.value += pixel
        return self
