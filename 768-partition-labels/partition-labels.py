class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        map = {}
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = [i, i]
            else:
                map[s[i]][1] = i
        
        arr = []

        for key, value in map.items():
            arr.append(value)
        
        arr.sort(key=lambda x: x[0])

        res = [arr[0]]
        current = arr[0]
        for item in arr[1:]:
            if item[0] < current[1]:
                res[-1] = [current[0], max(item[1], current[1])]
                current = res[-1]
            else:
                res.append(item)
                current = res[-1]
        sizes = []
        for element in res:
            sizes.append(element[1] - element[0] + 1)
        
        return sizes
