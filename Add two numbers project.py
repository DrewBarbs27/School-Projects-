class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    # Iterate through both linked lists
    while l1 or l2 or carry:
        # Extract digits from the current nodes
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # Calculate the sum with carry
        total = x + y + carry
        carry = total // 10

        # Create a new node for the result
        current.next = ListNode(total % 10)
        current = current.next

        # Move to the next nodes if available
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Example usage:
# Assume l1 = 2 -> 4 -> 3 and l2 = 5 -> 6 -> 4, which represent the numbers 342 and 465 in reverse order.
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = add_two_numbers(l1, l2)
# The sum is 807, which is represented as 7 -> 0 -> 8 in reverse order.
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 7 0 8
