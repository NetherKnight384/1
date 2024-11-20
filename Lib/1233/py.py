

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    
    @property
    def height(self):
        return(self.__height)
    @property
    def width(self):
        return(self.__height)

    @height.getter
    def height(self):
        return(self.__height)
    @height.setter
    def height(self, par):
        self.__height = par

    @width.getter
    def width(self):
        return(self.__width)
    @width.setter
    def width(self, par):
        self.__width = par

    def area(self):
        return(self.__height * self.__width)

class Boock:
    def __init__(self, title, auhtor, year):
        self.__title = title
        self.__auhtor = auhtor
        self.__year = year
    
    def __str__(self):
        return(f"Title: {self.__title}, auhtor: {self.__auhtor}, year: {self.__year}")
    
    def __repr__(self):
        return(f"{self.__title},{self.__auhtor},{self.__year}")

class Circle:
    def __init__(self, rad) -> None:
        self.__rad = rad
        self.__p = 3.14
    
    def set_diam(self,diam):
        self.__rad = diam/2

    def area(self):
        return(self.__p * self.__rad ** 2)

class Bank:
    def __init__(self, id, val) -> None:
        self.id = id
        self.__val = val
    
    @property
    def balance(self):
        return(self.__val)


    @balance.getter
    def balance(self):
        return(self.__val)
    @balance.setter
    def balance(self, val):
        if val >= 0:
            self.__val = val
        else:
            pass

test = Bank(1, 34.06)
test2 = Bank
print(test.balance)
test.balance = -29
print(test.balance)
test.balance = 0
print(test.balance)
    