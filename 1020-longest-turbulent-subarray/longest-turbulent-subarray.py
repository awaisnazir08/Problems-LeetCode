class Solution(object):

    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 1
        n = len(arr) - 1
        l = 0
        r = 1
        result = 0
        if arr[l] == arr[r]:
            while r < len(arr) and arr[l] == arr[r]:
                l += 1
                r += 1
        if r == len(arr):
            return 1
        if arr[l] > arr[r]:
            check = 0
        elif arr[l] < arr[r]:
            check = 1
        r += 1
        while r <= n:
            if check == 0:
                if arr[r-1]  < arr[r]:
                    check = 1
                    r += 1
                elif arr[r-1] > arr[r]:
                    result = max(result, r - l)
                    l = r - 1
                    check = 0
                    r += 1
                else:
                    result = max(result, r - l)
                    while r < len(arr) and arr[r-1] == arr[r]:
                        r += 1
                    if r < n:
                        l = r - 1
                        check = (arr[l] < arr[r])
                    else:
                        return result
            elif check == 1:
                if arr[r - 1] > arr[r]:
                    check = 0
                    r += 1
                elif arr[r - 1] < arr[r]:
                    check = 1
                    result = max(result, r - l)
                    l = r - 1
                    r += 1
                else:
                    result = max(result, r - l)
                    while r < len(arr) and arr[r-1] == arr[r]:
                        r += 1
                    if r < n:
                        l = r - 1
                        check = (arr[l] < arr[r])
                    else:
                        return result
        return max(result, r - l)


            


        