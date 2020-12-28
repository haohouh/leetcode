from abc import ABCMeta,abstractclassmethod

class File(object):
  def __init__(self,size,type):
    self.isDirectory = False
    self.children = []
    self.size = size
    self.type = type





class Filter(metaclass=ABCMeta):
  @abstractclassmethod
  def filter(self): pass


class TypeFilter(Filter):
  def __init__(self,type1):
    self.type = type1

  def filter(self,file):
    return file.type == self.type

class SizeFilter(Filter):
  def __init__(self,size):
    self.size = size

  def filter(self,file):
    return file.size > self.size


class Findcommand(object):

  def find(self,)