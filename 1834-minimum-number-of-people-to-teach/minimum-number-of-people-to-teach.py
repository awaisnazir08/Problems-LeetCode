class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        res = float("inf")
        person_lang = {}

        for i, language in enumerate(languages):
            person_lang[i + 1] = language
        
        to_teach = set()
        for f1, f2 in friendships:
            l1 = person_lang[f1]
            l2 = person_lang[f2]

            if not list(set(l1) & set(l2)):
                to_teach.add(f1)
                to_teach.add(f2)
        
        for l in range(1, n + 1):
            count = 0
            for person in to_teach:
                if l not in person_lang[person]:
                    count += 1
            res = min(count, res)

        return res


