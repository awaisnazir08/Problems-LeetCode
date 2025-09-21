import math

class Solution(object):
    def minOperations(self, queries):
        def prefix(n):
            """Compute F(n) = sum_{i=1}^n (floor(log4(i)) + 1)"""
            if n <= 0:
                return 0
            total = 0
            k = 0
            start = 1
            while start <= n:
                end = min(n, 4**(k+1) - 1)
                count = end - start + 1
                total += count * (k + 1)
                start *= 4
                k += 1
            return total
        
        ops = 0
        for l, h in queries:
            total = prefix(h) - prefix(l - 1)
            ops += (total + 1) // 2   # ceil(total/2)
        return ops
