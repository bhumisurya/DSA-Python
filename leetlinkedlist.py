class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Convert list to linked list
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy

    for value in arr:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Add two numbers
def addTwoNumbers(l1, l2):

    dummy = ListNode()
    current = dummy

    carry = 0

    while l1 or l2 or carry:

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry

        digit = total % 10
        carry = total // 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    return dummy.next


# Convert linked list to normal list
def linkedListToList(head):

    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# -------------------------
# Main
# -------------------------

l1 = [2, 4, 3]
l2 = [5, 6, 4]

head1 = createLinkedList(l1)
head2 = createLinkedList(l2)

answer = addTwoNumbers(head1, head2)

print("l1: ", l1)
print("l2: ", l2)
print("Addition: ", linkedListToList(answer))