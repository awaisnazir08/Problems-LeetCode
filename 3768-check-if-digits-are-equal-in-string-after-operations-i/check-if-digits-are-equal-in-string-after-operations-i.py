class Solution(object):
    def hasSameDigits(self, s):
        s = list(map(int, s))  # store digits as integers

        while len(s) > 2:
            for i in range(len(s) - 1):
                s[i] = (s[i] + s[i + 1]) % 10
            s.pop()

        return s[0] == s[1]
