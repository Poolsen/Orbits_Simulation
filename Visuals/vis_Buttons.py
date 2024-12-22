class Button:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shape = None


class Rectangle(Button):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        pass

