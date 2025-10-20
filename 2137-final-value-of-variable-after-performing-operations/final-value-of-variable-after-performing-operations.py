class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        res = 0
        for operation in operations:
            if '+' in operation:
                res += 1
            else:
                res -= 1
        
        return res
        