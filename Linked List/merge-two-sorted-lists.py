'''
* Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return it as a new sorted list.
        Time: O(n+m), Space: O(1) extra
        """
        dummy = tail = ListNode()     # dummy/sentinel head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remainder
        tail.next = list1 if list1 else list2
        return dummy.next


# ---- Helpers for local testing ----
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


# ---- Run tests when executed directly ----
if __name__ == "__main__":
    s = Solution()

    a = build_list([1,2,4])
    b = build_list([1,3,4])
    merged = s.mergeTwoLists(a, b)
    assert to_list(merged) == [1,1,2,3,4,4]

    assert to_list(s.mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(s.mergeTwoLists(build_list([]), build_list([0]))) == [0]
    assert to_list(s.mergeTwoLists(build_list([2,5,7]), build_list([3]))) == [2,3,5,7]

    print("All tests passed ✅")
