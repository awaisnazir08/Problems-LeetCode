class Solution(object):
    '''
    this commented out solution is correct, I have tested it out using online python compiler as well
    '''
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         d = {}
#         for num in nums:
#             if num not in d:
#                 d[num] = 1
#             else:
#                 d[num] += 1

#         sorted_dict_by_values = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
#         # first_k_elements = dict(islice(sorted_dict_by_values.items(), k))

#         # return list(first_k_elements)

#         return list(sorted_dict_by_values.keys())[:k]
        
    def topKFrequent(self, nums, k):
        defDict = defaultdict(int)
        for number in nums:
            defDict[number] += 1
        return sorted(defDict, key=defDict.get, reverse=True)[:k]