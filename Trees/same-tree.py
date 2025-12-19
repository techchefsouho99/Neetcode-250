from typing import Optional, List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Returns True if two binary trees are identical (same structure and values).
        Time: O(n), Space: O(h) due to recursion.
        """
        # both empty
        if p is None and q is None:
            return True
        # one empty, one not
        if p is None or q is None:
            return False
        # both exist: compare values
        if p.val != q.val:
            return False
        # compare subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ---- Helpers for local testing ----
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order values (None indicates no node).
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

    # Same trees
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    assert s.isSameTree(p1, q1) is True

    # Different structure
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    assert s.isSameTree(p2, q2) is False

    # Different values
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    assert s.isSameTree(p3, q3) is False

    # Both empty
    p4 = build_tree([])
    q4 = build_tree([])
    assert s.isSameTree(p4, q4) is True

    print("All tests passed ✅")
