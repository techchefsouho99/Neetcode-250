from typing import Optional, List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursive depth:
        Time: O(n), Space: O(h) where h is height due to recursion stack
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ---- Helpers for local testing ----
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list.
    None means no node.
    """
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# ---- Run tests ----
if __name__ == "__main__":
    s = Solution()

    # Example 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    assert s.maxDepth(root1) == 3

    # Example 2
    root2 = build_tree([1, None, 2])
    assert s.maxDepth(root2) == 2

    # Edge cases
    root3 = build_tree([])
    assert s.maxDepth(root3) == 0

    root4 = build_tree([1])
    assert s.maxDepth(root4) == 1

    print("All tests passed ✅")
