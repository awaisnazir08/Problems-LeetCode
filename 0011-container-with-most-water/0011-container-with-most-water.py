class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        area = 0
        j = len(height) - 1
        while i != j:
            new_area = min(height[i], height[j]) * (j - i)
            area = max(new_area, area)




            if height[j] < height[i]:
                j -= 1
            else:
                i += 1

        return area
        