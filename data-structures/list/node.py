class Node:
  def __init__(self, initdata):
    self.data = initdata
    self.next = None
    self.index = None
    self.rindex = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next = newnext

  def getIndex(self):
    return self.index, self.rindex

  def setIndex(self, index, rindex):
    self.index = index
    self.rindex = rindex
