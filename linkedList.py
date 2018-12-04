
class Node():
    """
    linked list
    """
    def __init__(self, val):
        self.val = val
        self.next = None # the pointer initially points to nothing

    def traverse(self):
        node = self # start from the head node
        while node:
            print(node.val) # access the node value
            node = node.next # move on to the next node


def reverse_list(head):
    new_head = None
    while head:
        head.next, head, new_head = new_head, head.next, head
    return new_head

def remove(node, val):
    head = node
    while node.next:
        if node.next.val == val:
            node.next = node.next.next
        node = node.next
    return head

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2  # 12->99
node2.next = node3  # 99->37
# the entire linked list is 12->99->37

node1.traverse()

new_head = remove(node1, 99)
new_head.traverse()

new_head = reverse_list(node1)
new_head.traverse()



class DoublyNode:
    """
    double linked list
    """
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def traverse(self, reverse = False):
        node = self
        while node:
            print(node.val)
            if reverse:
                node = node.prev
            else:
                node = node.next

n1 = DoublyNode(12)
n2 = DoublyNode(99)
n3 = DoublyNode(37)

n1.next = n2
n2.next = n3
n3.prev = n2
n2.prev = n1

n1.traverse()
n3.traverse(reverse=True)






