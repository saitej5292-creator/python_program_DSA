class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def has_cycle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow = slow.next
        fast=fast.next.next
         if slow==fast:
            return True
        return False
head=Node(20)
head.next=Node(60)
head.next.next=Node(80)
head.next.next.next=Node(100)
head.next.next.next.next=head.next
if has_cycle(head):
    print("loop detected")
else:
    print("no loop")    