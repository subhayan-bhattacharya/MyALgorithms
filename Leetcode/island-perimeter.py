#https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        prev = []
        perimeter = 0
        for index,g in enumerate(grid):
            if index == 0:
                for i,value in enumerate(g):
                    if value == 1:
                        perimeter = perimeter + 1
                        if len(prev) > 0:
                            if prev[-1] != i - 1:
                                perimeter = perimeter + 2
                        prev.append(i)
                if len(prev) > 0:
                    perimeter = perimeter + 2
                if len(grid) == 1:
                    break
            else:
                temp = []
                for i,value in enumerate(g):
                    if value == 1:
                        if len(temp) > 0:
                            if temp[-1] != i - 1:
                                perimeter = perimeter + 2
                        temp.append(i)
                        if i in prev:
                            prev.remove(i)
                        else:
                            perimeter = perimeter + 1
                if len(temp) > 0:
                    perimeter = perimeter + len(prev) + 2
                    prev = temp
        perimeter = perimeter + len(prev)
        return perimeter