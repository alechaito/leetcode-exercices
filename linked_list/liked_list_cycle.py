class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self, head):
        while head:
            print(head)
            head = head.next
n22 = ListNode(1, None)
n2 = ListNode(2, n22)
head = ListNode(1, n2)


def checkList(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

checkList(head)

"""
1 - Create a fast and slow pointer
2 - No matter what happens, sometime the pointers will be in the same place
3 - Pay attention to while stop condition
"""
