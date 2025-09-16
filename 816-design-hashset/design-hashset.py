class MyHashSet(object):

    def __init__(self):
        self.s = set()
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.s.add(key)

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.s:
            self.s.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.s
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)