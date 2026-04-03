'''
* Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/description
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare halves
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True


# ---------- Helper functions for testing ----------
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ---------- Test run ----------
if __name__ == "__main__":
    sol = Solution()

    head1 = build_linked_list([1, 2, 2, 1])
    print("Input: [1, 2, 2, 1]")
    print("Is Palindrome?", sol.isPalindrome(head1))

    head2 = build_linked_list([1, 2, 3, 2, 1])
    print("\nInput: [1, 2, 3, 2, 1]")
    print("Is Palindrome?", sol.isPalindrome(head2))

    head3 = build_linked_list([1, 2])
    print("\nInput: [1, 2]")
    print("Is Palindrome?", sol.isPalindrome(head3))
