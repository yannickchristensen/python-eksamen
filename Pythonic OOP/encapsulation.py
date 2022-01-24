""" class number:
    def __init__(self, x):
        self.__x = x
        
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x """



class number:
    def __init__(self, x):
        self.x = x
        
    @property
    def get_x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x



n1 = number(10)
n2 = number(10)

n1.x = n1.x + n2.x

#n1.set_x(n1.get_x() + n2.get_x())


print(n1.x)




