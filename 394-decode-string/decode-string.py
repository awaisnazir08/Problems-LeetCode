class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        new_string = ''
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                inside_string = ''
                while stack and stack[-1] != '[':
                    current = stack.pop()
                    inside_string = current + inside_string
                if stack:
                    stack.pop()
                number = ''
                while stack and stack[-1].isdigit():
                    current = stack.pop()
                    number = current + number
                number = int(number)
                inside_string = inside_string*number
                for j in inside_string:
                    stack.append(j)
                # if stack:
                #     stack.pop()
        string = ''
        number = ''
        while stack:
            current = stack.pop()
            if current.isdigit():
                number = current + number
            else:
                string = current + string
        if number:
            number = int(number)
            new_string = new_string*number
            return string + new_string
        else:
            return new_string + string

                




            


                
        