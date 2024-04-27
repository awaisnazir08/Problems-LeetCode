class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits) == 1:
            return 1
        baskets = {}
        f1_i= 0
        f2_i = 1
        total_fruits = 0
        n = len(fruits) -1
        f1 =  fruits[f1_i]
        baskets[f1] = 1
        while f2_i <= n and fruits[f2_i] == f1:
            baskets[f1] += 1
            f2_i += 1
            f1_i += 1

        if(f2_i>=n):
            return len(fruits)

        f2 = fruits[f2_i]
        baskets[f2] = 1

        for i in range(f2_i + 1,len(fruits)):
            if fruits[i] == f1:
                baskets[f1] += 1
                f1_i = i
            elif fruits[i] == f2:
                baskets[f2] += 1
                f2_i = i
            else:
                total_fruits = max(total_fruits, baskets[f1] + baskets[f2])
                last_fruit = fruits[i - 1]
                if last_fruit == f2:
                    baskets[f2] = (i - 1) - f1_i
                    f2_i = i - 1
                    baskets[f1] = 1
                    f1 = fruits[i]
                    baskets[f1] = 1
                    f1_i = i
                elif last_fruit == f1:
                    baskets[f1] = i - 1 - f2_i
                    f1_i = i - 1
                    baskets[f2] = 1
                    f2 = fruits[i]
                    baskets[f2] = 1
                    f2_i = i
        return max(total_fruits, baskets[f1] + baskets[f2])

            



