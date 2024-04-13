class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        l = 0
        r = 0
        my_dict = {}
        n = 0
        temp = 0
        while (r < len(s)):
            if s[r] not in my_dict:
                my_dict[s[r]] = 1
                temp += 1
                r += 1

            else:
                j = l
                check = False
                while (j < r):
                    if s[j] == s[r]:
                        check = True
                        break
                    else:
                        j += 1
                if not check:
                    temp += 1
                    r += 1
                    continue
                n = max(n, temp)
                while s[l] != s[r] and l < len(s):
                    l += 1
                l += 1
                temp = r - l + 1
                r += 1
        return max(temp, n)
                



        