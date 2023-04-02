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

n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)

n = 2


def removeNthFromEnd(head, n: int):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # moving our right pointer to right distance from the left
    while n > 0 and right:
        right = right.next
        n -= 1

    # lets shift our pointers until find the end
    # at the end left pointer will be 1 pos after the node that we want to delete
    while right:
        right = right.next
        left = left.next

    #just delete node removing the link
    left.next = left.next.next

    return dummy.next


removeNthFromEnd(head, n)

