class Rectangle():
    def __init__(self,width,length,x,y):
        self.width = width
        self.length = length
        self.x = x
        self.y = y
        
    def get_area(self):
        print(f'Area: {self.length * self.width}')
    def get_perimeter(self):
        print(f'Perimeter: {2*self.width + 2*self.length}')
    def coord(self):
        print(f'Coordinates: ({self.x},{self.y})')

rec1 = Rectangle(10,15,5,3)
rec2 = Rectangle(3,5,15,7)

print('Rectangle #1')
rec1.coord()
rec1.get_area()
rec1.get_perimeter()
print('Rectangle #2')
rec2.coord()
rec2.get_area()
rec2.get_perimeter()


