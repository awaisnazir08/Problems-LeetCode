import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        s = ""
        def allow_consecutive(char):
            if len(s) <= 1:
                return True
            if (s[-1] == s[-2]) and (s[-1] == char):
                return False
            else:
                return True
        
        heap = []
        if a:
            heapq.heappush(heap, (a * -1, 'a'))
        if b:
            heapq.heappush(heap, (b * -1, 'b'))
        if c:
            heapq.heappush(heap, (c * -1, 'c'))

        while heap:
            top_element = heapq.heappop(heap)
            freq = top_element[0] * -1
            char = top_element[1]

            if allow_consecutive(char):
                s += char
                freq -= 1
                if freq > 0:
                    heapq.heappush(heap, (freq * -1, char))
            else:
                if not heap:
                    return s
                second_top_element = heapq.heappop(heap)
                sec_freq = second_top_element[0] * -1
                sec_char = second_top_element[1]

                heapq.heappush(heap, (freq * -1, char))

                if allow_consecutive(sec_char):
                    s += sec_char
                    sec_freq -= 1
                    if sec_freq > 0:
                        heapq.heappush(heap, (sec_freq * -1, sec_char))
        
        return s


