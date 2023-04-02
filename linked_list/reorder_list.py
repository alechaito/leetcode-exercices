class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"{self.val} -> {self.next.val}"

    def show(self, head):
        while head:
            print(head)
            head = head.next

n4 = ListNode(4, None)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)


def reorderList(head):
        sp, fp = head, head.next

        # using a slow and fast pointer to find the middle
        while sp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        # head of second portion
        head2 = sp.next
        sp.next = None # cutting the continuation to create 2 linked lists

        #now we need to reorder the second linked_list
        prev = None
        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp

        # now we merge
        first, second = head, prev
        while head:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

reorderList(head)

"""
1 - We need to discover the middle if its a odd number of nodes, first portion is bigger
2 - Reorder the second linked list to be easy to merge
3 - Just reorganize the pointers of linked lists
"""
