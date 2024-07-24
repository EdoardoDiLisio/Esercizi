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


def get_list_length(head) -> int:
    if not head:
        return 0
    
    current = head
    counter = 1
    while current.next:
        current = current.next
        counter += 1
    return counter


            

def reverse_list(head: Node):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
            
        
def is_palindrome(head: Node) -> list[int]:
    if not head or not head.next:
        return True
    
    length = get_list_length(head)

    sep = False
    current = head
    while current and not sep:
        current = current.next
        if current.pos >= length // 2:
            tail = reverse_list(current)
            sep = True

    current_head = head
    current_tail = tail
    while current_head and current_tail:
        if current_tail.val != current_head.val:
            return False
        
        current_head = current_head.next
        current_tail = current_tail.next

    return True


# Test case 1
ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)
print(is_palindrome(ll1.head)) 


# Test case 2
ll2 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll2.append(value)
print(is_palindrome(ll2.head)) 


# Test case 3 
ll3 = LinkedList()
ll3.append(1)
print(is_palindrome(ll3.head))


# Test case 4
ll4 = LinkedList()
ll4.append(1)
ll4.append(1)
print(is_palindrome(ll4.head)) 


# Test case 5 
ll5 = LinkedList()
ll5.append(1)
ll5.append(2)
print(is_palindrome(ll5.head))



    
