class Node(object):
  def __init__(self, k, v, f):
    self.key = k
    self.val = v
    self.freq = f
    self.prev = None
    self.next = None

class LFUCache(object):
  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.capacity = capacity
    self.m = {}
    self.freq = {}
    self.min_f = 1

  def add(self, cur):
    m, f = self.m, self.freq
    freq = cur.freq + 1
    cur.freq = freq
    if freq not in f:
      root = Node(None, None, freq)
      root.prev, root.next = root, root
      f[freq] = root
    else:
      root = f[freq]
    p = root.prev
    p.next, cur.prev = cur, p
    cur.next, root.prev = root, cur
    return cur.val

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    m, f = self.m, self.freq
    if key not in m:
      return -1
    else:
      cur = m[key]
      cur.prev.next, cur.next.prev = cur.next, cur.prev
      if f[self.min_f].next is f[self.min_f]:
        self.min_f += 1
      return self.add(cur)


  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    m, f = self.m, self.freq
    if not self.capacity:
      return
    if key in m:
      m[key].val = value
      self.get(key)
    else:
      if len(m) == self.capacity:
        root = f[self.min_f]
        cur = root.next
        node = cur.next
        root.next, node.prev = node, root
        del m[cur.key]
      self.min_f = 1
      cur = Node(key, value, 0)
      self.add(cur)
      m[key] = cur




    # Your LFUCache object will be instantiated and called as such:
    # obj = LFUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)