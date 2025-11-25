class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        if k % 2 == 0:
            return -1
        
        if k % 10 == 5:
            return -1
        
        n = 1
        length = 1
        while True:
            if n % k == 0:
               return length 
            else:
                n = n * 10 + 1
                length += 1

        