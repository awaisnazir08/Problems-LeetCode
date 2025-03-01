import heapq
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """


        heap = []

        for product in products:
            if product[0] == searchWord[0]:
                heapq.heappush(heap, product)
        
        searches = []
        for i in range(len(searchWord)):
            current_search_list = []
            current = searchWord[:i + 1]
            while (heap):
                extracted_element = heapq.heappop(heap)
                if current == extracted_element[:i + 1]:
                    current_search_list.append(extracted_element)
            
            searches.append(current_search_list[:3])

            heapq.heapify(current_search_list)
            heap = current_search_list

        return searches
                


