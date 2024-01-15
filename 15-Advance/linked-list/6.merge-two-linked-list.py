class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_linked_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    current = list1
    while current.next:
        current = current.next
    current.next = list2

    return list1

list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(4, ListNode(5, ListNode(6)))

merged_list = merge_linked_lists(list1, list2)

while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
