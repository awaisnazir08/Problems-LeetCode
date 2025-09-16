class MyHashMap(object):

    def __init__(self):
        self.map = []
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.map:
            self.map.append([key, value])
            return
        
        for i, (k, v) in enumerate(self.map):
            if k == key:
                self.map[i][1] = value
                return
        self.map.append([key, value])
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i, (k, v) in enumerate(self.map):
            if k == key:
                return v
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i, (k, v) in enumerate(self.map):
            if k == key:
                del self.map[i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)