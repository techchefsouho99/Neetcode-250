from typing import Optional, List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively inverts a binary tree (swap left and right subtrees).
        Time: O(n), Space: O(h) where h is tree height (due to recursion stack)
        """
        if root is None:
            return

        # Recurse into left and right subtrees first
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Swap children
        root.left, root.right = root.right, root.left

        return root


# ---- Helper functions for building and printing ----
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a level-order list of values.
    None means no node at that position.
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

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to level-order list (with None for empty nodes)."""
    from collections import deque
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result


# ---- Run tests ----
if __name__ == "__main__":
    s = Solution()

    root = build_tree([4,2,7,1,3,6,9])
    inverted = s.invertTree(root)
    assert tree_to_list(inverted) == [4,7,2,9,6,3,1]

    root2 = build_tree([2,1,3])
    inverted2 = s.invertTree(root2)
    assert tree_to_list(inverted2) == [2,3,1]

    root3 = build_tree([])
    inverted3 = s.invertTree(root3)
    assert tree_to_list(inverted3) == []

    print("All tests passed ✅")
