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


n3 = ListNode(4, None)
n2 = ListNode(2, n3)
h1 = ListNode(1, n2)


n3 = ListNode(4, None)
n2 = ListNode(3, n3)
h2 = ListNode(1, n2)



 def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    def mergeLists(l1, l2):
        # avoid edge cases
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            # check the smaller value to add to tail
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next # l1 need to be updated to the next node
            else:
                tail.next = l2
                l2 = l2.next
            #update current tail node to the next
            tail = tail.next
        
        # if some of the nodes ends just append another one to our tail
        if l1 is None:
            tail.next = l2
        elif l2 is None:
            tail.next = l1
        
        return dummy.next


    # keep doing that until we have just one list
    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i < len(lists) - 1 else None
            mergedLists.append(mergeLists(l1, l2))
        
        # updated lists because now all of them are merged
        lists = mergedLists

    # here we have just 1 list and its already sorted
    return lists[0]
    
"""
We know how to merge two linked lists so the trick here is how to do that

we go ahead with 2 steps merging two linked lists and sorting them

"""