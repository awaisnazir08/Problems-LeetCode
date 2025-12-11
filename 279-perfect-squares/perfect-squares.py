class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        for i in range(int(sqrt(n)), 0, -1):
            arr.append(i**2)
        
        q = []
        for num in arr:
            remaining = n - num
            if remaining == 0:
                return 1
            elif remaining > 0:
                q.append((1, remaining))


        while q:
            current_count, current_sum = q.pop(0)
            current_count += 1
            for num in arr:
                remaining = current_sum - num
                if remaining == 0:
                    return current_count
                elif remaining > 0:
                    q.append((current_count, remaining))
        
        return 0


