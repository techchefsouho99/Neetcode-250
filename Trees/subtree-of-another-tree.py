from typing import Optional, List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Returns True if subRoot is a subtree of root.
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


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

    # True: subRoot exists in root
    root1 = build_tree([3, 4, 5, 1, 2])
    sub1  = build_tree([4, 1, 2])
    assert s.isSubtree(root1, sub1) is True

    # False: similar but extra node '0' breaks match
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub2  = build_tree([4, 1, 2])
    assert s.isSubtree(root2, sub2) is False

    # Edge cases
    assert s.isSubtree(build_tree([]), build_tree([])) is True   # empty in empty
    assert s.isSubtree(build_tree([1, 1]), build_tree([1])) is True
    assert s.isSubtree(build_tree([1]), build_tree([2])) is False

    print("All tests passed ✅")
