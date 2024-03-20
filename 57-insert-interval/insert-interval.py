class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
        #just rely on invariant of sorted by start and then check out of order then intersection cases
        ni = newInterval  
        intervals = [ni] + intervals
        lst = [ni]
        for i in intervals[1:] :   
            cs,ce = i 
            ls,le = lst[-1]
            if cs > le :  
                lst.append(i) 
            else :  
                last = lst.pop() 
                if ls > ce : 
                    lst.append(i) 
                    lst.append(last) 
                else : 
                    lst.append([min(cs,ls),max(ce,le)]) 
        return lst
