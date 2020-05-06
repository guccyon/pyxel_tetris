class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def apply(self, direction):
        return Point(
            self.x + direction.value[0],
            self.y + direction.value[1]
        )
    def add(self, x, y):
        return Point(self.x + x, self.y + y)

class Px:
    def __init__(self, pixel):
        self.value = pixel
    
    def actual(self):
        return self.value * 8
    
    def add(self, pixel):
        self.value += pixel
        return self
