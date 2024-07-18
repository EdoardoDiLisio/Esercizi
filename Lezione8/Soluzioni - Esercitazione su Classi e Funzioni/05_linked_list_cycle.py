class Node:
    pos = 0
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
        self.pos = Node.pos
        Node.pos += 1


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def append(self, val: int):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def get_node(self, index: int):
        if index == 0:
            return self.head
        
        current = self.head
        while current.next:
            current = current.next
            if current.pos == index:
                return current
            


def has_cycle(head: Node):
    prev: Node = head
    current: Node = head.next

    if current is None:
        return False
    
    if current.pos <= prev.pos:
        return True
    
    while current.next != None:
        prev = current
        current = current.next
        if current.pos <= prev.pos:
            return True
    
    return False





# Test case 1
ll1 = LinkedList()
for i in range(5):
    ll1.append(i)
node1 = ll1.get_node(1)  # Node with value 1
node4 = ll1.get_node(4)  # Node with value 4
node4.next = node1  # Creating a cycle

print(has_cycle(ll1.head))
# 0 -> 1 -> 2 -> 3 -> 4 

# Test case 2
ll2 = LinkedList()
for i in range(5):
    ll2.append(i)

print(has_cycle(ll2.head))


# Test case 3
ll4 = LinkedList()
ll4.append(1)
node = ll4.head
node.next = node  # Creating a cycle

print(has_cycle(ll4.head))


# Test case 4
ll3 = LinkedList()
ll3.append(1)

print(has_cycle(ll3.head))  # Output: False