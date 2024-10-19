from collections import deque

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = deque()
        dot_counter = 0
        for item in path:
            if item == '/' and len(stack) > 0 and stack[-1] == '/':
                    while len(stack) != 0 and stack[-1] == '/': 
                        stack.pop()
                # stack.append(item)
            elif item == '.' and stack[-1] == '/':
                dot_counter += 1
            elif item == '.' and dot_counter == 1:
                dot_counter += 1
            elif item == '.' and dot_counter >= 2:
                dot_counter = 0
            elif item != '.' and item != '/' and dot_counter > 0:
                dot_counter = 0
            elif item == '/' and dot_counter == 2:
                stack.pop()
                stack.pop()
                stack.pop()
                while len(stack) != 0 and stack[-1] != '/':
                    stack.pop()
                if len(stack) != 0:
                    stack.pop()
                dot_counter = 0
            elif item == '/' and dot_counter == 1:
                stack.pop()
                dot_counter = 0
                if len(stack) != 0:
                    stack.pop()
            stack.append(item)

        if stack[-1] == '.' and dot_counter == 1:
            stack.pop()
        if stack[-1] == '/' and len(stack) > 1:
            stack.pop()
        if stack[-1] == '.' and dot_counter == 2:
            stack.pop()
            stack.pop()
            stack.pop()
            while len(stack) != 0 and stack[-1] != '/':
                stack.pop()
            if len(stack) != 0:
                stack.pop()
        
        return "".join(stack) if len(stack) > 1 else '/'
        
