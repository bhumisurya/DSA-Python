class ListNode:
  def __init__(self, value):
    self.val = value
    self.next = None

def has_cycle(head):
  slow = fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow is fast:
      return True
  return False
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = c

print(has_cycle(a))