'''
* Combination Sum: https://leetcode.com/problems/combination-sum/
'''
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i: int, curr: List[int], total: int):
            if total == target:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                # Pruning because candidates is sorted
                if total + candidates[j] > target:
                    return

                curr.append(candidates[j])

                # Reuse same candidate
                dfs(j, curr, total + candidates[j])

                # Backtrack
                curr.pop()

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    solution = Solution()

    candidates = [2, 3, 6, 7]
    target = 7

    result = solution.combinationSum(candidates, target)

    print("Candidates:", candidates)
    print("Target:", target)
    print("Combinations:")
    for combination in result:
        print(combination)