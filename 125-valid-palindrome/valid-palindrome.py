class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= s.lower()
        s = re.sub(r'[\W_]', '', s)

        return s == s[::-1]
        