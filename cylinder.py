class cylinder():
    pi = 3.14
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius
    def volume(self):
        return cylinder.pi * self.radius* self.radius* self.height
    def surfacearea(self):
        return  2*cylinder.pi*self.radius*(self.radius+self.height)

if __name__ == "__main__":
    c = cylinder(2,3)
    print(c.volume())
    print(c.surfacearea())

