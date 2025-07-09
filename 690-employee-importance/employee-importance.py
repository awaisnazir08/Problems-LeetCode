from collections import deque
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        start = 0
        indices_id = {}
        for i in range(len(employees)):
            indices_id[employees[i].id] = i
        
        queue = deque()
        s = set()

        queue.append(indices_id[id])
        s.add(indices_id[id])

        total_importance = 0
        while queue:
            employee_index = queue.popleft()
            total_importance += employees[employee_index].importance
            for subordinate in employees[employee_index].subordinates:
                if indices_id[subordinate] not in s:
                    s.add(indices_id[subordinate])
                    queue.append(indices_id[subordinate])
        
        return total_importance


        