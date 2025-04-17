class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        new_s = ''

        for j in range(len(s) -1 , -1, -1 ):
            if s[j] != " ":
                stack.append(s[j])
            else:
                while stack:
                    new_s += stack.pop()
                if new_s and new_s[-1] != ' ':
                    new_s += ' '

        while stack:
            new_s += stack.pop()
        
        
        return new_s.strip()