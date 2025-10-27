class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        def backtrack(start, elements):
            if len(elements) == k:
                res.append(elements[:])
            elif len(elements) > k:
                return
            else:
                for i in range(start, n + 1):
                    elements.append(i)
                    backtrack(i + 1, elements)
                    elements.pop()
        
        backtrack(1, [])
        return res

        