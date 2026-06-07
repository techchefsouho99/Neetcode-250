'''
* Course Schedule - https://leetcode.com/problems/course-schedule/description
'''
from typing import List


class Solution:

    def dfs(self, crs: int, preMap: dict[int, List[int]], state: List[int]) -> bool:

        # cycle found
        if state[crs] == 1:
            return False

        # already processed
        if state[crs] == 2:
            return True

        state[crs] = 1  # mark as visiting

        for preReq in preMap[crs]:
            if not self.dfs(preReq, preMap, state):
                return False

        state[crs] = 2  # mark as visited
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build adjacency list
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        for course in range(numCourses):
            if not self.dfs(course, preMap, state):
                return False

        return True


# Example Usage
sol = Solution()

print(sol.canFinish(2, [[1, 0]]))
# True

print(sol.canFinish(2, [[1, 0], [0, 1]]))
# False

print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]))
# True

print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2], [0, 3]]))
# False