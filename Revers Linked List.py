# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        def travers_llist(node):
            nonlocal head
            if node.next is None:
                head = node
                return
            
            prev_node = node
            next_node = node.next
            travers_llist(next_node)
            next_node.next = prev_node
            
        last_node = head
        travers_llist(head)
        last_node.next = None
        return head
        