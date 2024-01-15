class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bubble_sort(head):
    if not head or not head.next:
        return head

    swapped = True

    while swapped:
        current = head
        prev = None
        swapped = False

        while current and current.next:
            next_node = current.next

            if current.val > next_node.val:
                current.val, next_node.val = next_node.val, current.val
                swapped = True

            prev = current
            current = current.next

    return head

list1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(5)))))

sorted_list = bubble_sort(list1)

while sorted_list:
    print(sorted_list.val, end=" -> ")
    sorted_list = sorted_list.next
