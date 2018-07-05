# https://leetcode.com/problems/employee-importance/description/
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        map = {}
        for e in employees:
            map[e.id] = e
            
        def get_importance(id):
            return map[id].importance + sum([get_importance(i) for i in map[id].subordinates])
        
        return get_importance(id)