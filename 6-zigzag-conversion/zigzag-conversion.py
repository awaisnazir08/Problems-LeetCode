class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        jump = (numRows - 1) * 2
        newString = ''
        for i in range(numRows):
            if i < len(s):
                newString += s[i]
            if i == 0 or i == numRows - 1:
                index = i
                index += jump
                while index < len(s):
                    newString +=s[index]
                    index += jump
            else:
                index = i
                midJump = i
                index += jump
                midJump += jump - (2 * i)
                while index < len(s) or midJump < len(s):
                    if midJump < len(s):
                        newString += s[midJump]
                    if index < len(s):
                        newString += s[index]
                    midJump = index
                    index += jump
                    midJump += jump - (2*i)
        return newString


        