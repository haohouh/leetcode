from abc import ABCMeta,abstractclassmethod

class Abc(metaclass = ABCMeta):
    @property
    @abstractclassmethod
    def size(self):
        pass

    @abstractclassmethod
    def method(self):
        pass

    def concreteMethod(self):
        pass

class Singleroom(Abc):
    def __init__(self):
        self._size = 1

    def method(self):
        pass

    @property
    def size(self):
        return self._size 

class Doubleroon(Abc):

    def __init__(self):
        self._size = 2 

    def method(self):
        pass
    
    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    s1 = Singleroom()
    print(s1.size)
    d1 = Doubleroon()
    print(d1.size)