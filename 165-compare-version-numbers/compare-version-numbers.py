class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]

        l1 = len(v1)
        l2 = len(v2)

        if l1 > l2:
            for i in range(l1-l2):
                v2.append(0)
        elif l2 > l1:
            for i in range(l2 - l1):
                v1.append(0)
        
        for n1, n2 in zip(v1, v2):
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        
        return 0
        