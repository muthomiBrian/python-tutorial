from node import Node

class UnorderedList:
  def __init__(self):
    self.head = None
    self.last = None

  def isEmpty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    if self.head == None:
      self.head = temp
      self.last = temp
    else:
      temp.setNext(self.head)
      self.head = temp
    self.setIndex()

  def size(self):
    current = self.head
    count = 0
    while  current != None:
      count = count + 1
      current = current.getNext()
    return count

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()

    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())
    self.setIndex()

  def append(self, item):
    temp = Node(item)
    self.last.setNext(temp)
    self.last = temp
    self.setIndex()

  def setIndex(self):
    current = self.head
    count = 0
    size = self.size()
    rcount = size * -1
    last = False
    while current != None and not last:
      current.setIndex(count, rcount)
      count = count + 1
      rcount = rcount + 1
      if current.getNext() != None:
        current = current.getNext()
      else:
        last = True

  def insert(self, position, item):
    if position == 0 or position < (self.size() + 1) * -1:
      self.add(item)
    if position > 0 and position < self.size() + 1:
      previous = self.findByPosition(position - 1)
      next = previous.getNext()
      temp = Node(item)
      temp.setNext(next)
      previous.setNext(temp)
      self.setIndex()
    if position < 0 and position > (self.size() + 1) * -1:
      previous = self.findByPosition(position)
      next = previous.getNext()
      temp = Node(item)
      temp.setNext(next)
      previous.setNext(temp)
      self.setIndex()
      
    if position > self.size() -1 or position == -1:
      self.append(item)

  def findByPosition(self, position):
    current = self.head
    target = None
    found = False
    while current != None and not found :
      currentPosition = current.getIndex()
      if position in currentPosition:
        target = current
        found = True
      else:
        current = current.getNext()
    return target

  def index(self, item):
    current = self.head
    found = False
    index = None
    while current != None and not found:
      if current.getData() == item:
        index = current.getIndex()[0]
        found = True
      else:
        current = current.getNext()
    return index

  def pop(self, pos = -1):
    current = self.head
    if pos == -1:
      current = self.last
      if self.last == self.head:
        self.head = None
        self.last = None
      else:
        self.last = self.findByPosition(-2)
        self.last.setNext(None)
      self.setIndex()
      return current.getData()
    else:
      current = self.findByPosition(pos)
      previous = self.findByPosition(pos - 1)
      next = current.getNext()
      previous.setNext(next)
      self.setIndex()
      return current.getData()
