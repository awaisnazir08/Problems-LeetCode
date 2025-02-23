class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """

        N = len(img1)
        best = 0
        for dx in range(-N+1, N):
            for dy in range(-N+1, N):
                current_overlap = 0
                for x in range(N):
                    if 0 <= dx + x < N:
                        for y in range(N):
                            if 0 <= (dy + y) < N:
                                current_overlap += int(img1[x + dx][y + dy] == img2[x][y] == 1)
                best = max(best, current_overlap)
        
        return best
                                

        