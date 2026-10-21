#Lab 8-1: Creating user-defined class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def display(self):
        print('Width:', self.width)
        print(f'Height: {self.height}')

r1 = Rectangle(4, 5)
r2 = Rectangle(10, 10)

r1.display()
print()

r2.display()
print()

print(f"Width of r1: {r1.width}\nWidth of r2: {r2.width}",)
print(f"Height of r1: {r1.height}\Height of r2: {r2.height}\n",)

width = int(input('Enter width: '))
height = int(input('Enter height: '))

newRec = Rectangle(width, height)
newRec.display()

print(f"Width of NewR: {newRec.width}\nHeight of NewR: {newRec.height}",)