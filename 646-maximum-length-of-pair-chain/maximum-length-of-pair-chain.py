class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key = lambda x:x[1])

        res = [pairs[0]]
        ans = 0

        for pair in pairs[1:]:
            if res[-1][1] < pair[0]:
                res.append(pair)
            else:
                ans = max(ans, len(res))
                
        return max(ans, len(res))

