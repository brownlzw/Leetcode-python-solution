from random import randint
class RandomizedSet(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.li = []
    self.m = {}

  def insert(self, val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.m:
      self.m[val] = len(self.li)
      self.li.append(val)
      return True
    else:
      return False

  def remove(self, val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.m:
      return False
    index = self.m[val]
    if index != len(self.li) - 1:
      last = self.li[len(self.li) - 1]
      self.li[index], self.li[len(self.li) - 1] = last, val
      self.m[last] = index
    self.li.pop()
    del self.m[val]
    return True


  def getRandom(self):
    """
    Get a random element from the set.
    :rtype: int
    """
    return self.li[randint(0, len(self.li) - 1)]



    # Your RandomizedSet object will be instantiated and called as such:
    # obj = RandomizedSet()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()
