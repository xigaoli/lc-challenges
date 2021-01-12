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
        #use map
        emap={}
        for item in employees:
            emap[item.id]=item
        
        def dfs(empid):
            subords=emap[empid].subordinates
            rslt=emap[empid].importance
            for subid in subords:
                rslt+=dfs(subid)
            return rslt
        ans = dfs(id)
        return ans