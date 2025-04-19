class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)

        stack = []
        stack.append((temperatures[0],0))
        for i in range(1, len(temperatures)):
            if not stack and (temperatures[i] <= stack[-1][0]):
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    top = stack.pop()
                    answer[top[1]] = (i - top[1])
                stack.append((temperatures[i], i))
            
        return answer
                



            
                 