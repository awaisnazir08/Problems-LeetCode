class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for element in operations:
            if element.isdigit() or '-' in element:
                stack.append(int(element))
            elif element == 'C':
                stack.pop()
            elif element == 'D':
                a = stack.pop()
                c = a * 2
                stack.append(a)
                stack.append(c)
            elif element == '+':
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(b)
                stack.append(a)
                stack.append(c)
            
        res = 0
        while stack:
            item = stack.pop()
            res += item
        return res
        