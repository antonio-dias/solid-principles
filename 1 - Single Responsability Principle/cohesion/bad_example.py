
class Square:

    def __init__(self):
        self.side = 5

    def calculateArea(self):
        return self.side * self.side

    def calculatePerimeter(self):
        return self.side * 4

    def draw(self):
        if self.highResolutionMonitor:
            # Render a high resolution image of a square
            pass
        else:
            # Render a normal image of a square
            pass

    def rotate(self, degree):
        # Rotate the image of the square clockwise to the required degree and re-render
        pass