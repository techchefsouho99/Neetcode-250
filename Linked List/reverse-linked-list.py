from typing import Optional, List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list using the given implementation.
        Time: O(n), Space: O(1)
        """
        prev = None
        curr, temp = head, head
        while curr:
            curr = curr.next      # move curr first
            temp.next = prev      # reverse the link
            prev = temp           # move prev forward
            temp = curr           # move temp forward
        return prev


# ---- Helper functions for testing ----
def build_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ---- Run some tests ----
if __name__ == "__main__":
    s = Solution()

    assert to_list(s.reverseList(build_list([]))) == []
    assert to_list(s.reverseList(build_list([1]))) == [1]
    assert to_list(s.reverseList(build_list([1,2]))) == [2,1]
    assert to_list(s.reverseList(build_list([1,2,3,4,5]))) == [5,4,3,2,1]

    print("All tests passed ✅")
