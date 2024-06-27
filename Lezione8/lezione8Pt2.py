#EDOARDO DI LISIO
#27.06.2024

'''
Given a string s which consists of lowercase or uppercase letters, write a function that returns the length of the longest 
palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
print("Esercizio N.1 \n")
def longest_palindrome(s: str) -> int:
    from collections import Counter
    
    # Count the frequency of each character
    char_count = Counter(s)
    
    # Initialize the length of the longest palindrome
    length = 0
    # A flag to indicate if we have any odd frequency characters
    odd_found = False
    
    # Iterate over the character counts
    for count in char_count.values():
        if count % 2 == 0:
            # Even counts can all be used
            length += count
        else:
            # Odd counts: use count-1 to make it even, and set the flag
            length += count - 1
            odd_found = True
    
    # If there's any odd count, we can put exactly one odd character in the middle
    if odd_found:
        length += 1
    
    return length

# Test cases
print(longest_palindrome("abccccdd"))  # Output: 7
print(longest_palindrome("Aa"))        # Output: 1
print("\n\n")

'''
Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List concepts using classes. 
'''
print("Esercizio N.2 \n")
class Node:
    def __init__(self, value: int, next: 'Node' = None):
        self.value = value  # Initialize the node's value
        self.next = next  # Initialize the next node reference, default is None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    def append(self, value: int):
        if not self.head:
            # If the list is empty, create a new node and set it as the head
            self.head = Node(value)
        else:
            # If the list is not empty, traverse to the end and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

def reverse_list(head: Node) -> Node:
    previous = None  # Initialize the previous node as None
    current = head  # Start with the head of the list
    while current:
        next_node = current.next  # Store the next node
        current.next = previous  # Reverse the current node's pointer
        previous = current  # Move the previous pointer to the current node
        current = next_node  # Move to the next node in the list
    return previous  # Return the new head of the reversed list

def is_palindrome(head: Node) -> bool:
    if not head or not head.next:
        return True  # A list with 0 or 1 node is always a palindrome
    
    # Step 1: Find the middle of the linked list
    slow = head  # Initialize slow pointer
    fast = head  # Initialize fast pointer
    while fast and fast.next:
        slow = slow.next  # Move slow pointer by 1 step
        fast = fast.next.next  # Move fast pointer by 2 steps
    
    # Step 2: Reverse the second half of the list
    second_half_start = reverse_list(slow)  # Reverse from the middle to the end
    
    # Step 3: Compare the first half and the reversed second half
    first_half_start = head  # Start from the head of the list
    second_half_copy = second_half_start  # Keep a copy of the reversed second half's head to restore later
    while second_half_start:
        if first_half_start.value != second_half_start.value:
            return False  # If values are different, it's not a palindrome
        first_half_start = first_half_start.next  # Move to the next node in the first half
        second_half_start = second_half_start.next  # Move to the next node in the second half
    
    # Step 4: Restore the list (optional)
    reverse_list(second_half_copy)  # Reverse the second half back to original order
    
    return True  # If all values matched, the list is a palindrome

# Test cases
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(1)
print(is_palindrome(ll.head))  # Output: True

ll = LinkedList()
ll.append(1)
ll.append(2)
print(is_palindrome(ll.head))  # Output: False
print("\n\n")

'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions 
of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- push(x: int) -> None: Pushes element x to the top of the stack.
- pop() -> None Removes the element on the top of the stack and returns it.
- pop() -> None Returns the element on the top of the stack.
- empty() -> None Returns true if the stack is empty, false otherwise.
'''

print("Esercizio N.3 \n")
from queue import Queue

class MyStack:
    def __init__(self):
        # Initialize two queues
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.active_queue = self.queue1

    def push(self, x: int) -> None:
        # Push the element to the active queue
        self.active_queue.put(x)

    def pop(self) -> int:
        # Transfer all elements except the last one to the other queue
        inactive_queue = self.queue2 if self.active_queue is self.queue1 else self.queue1
        while self.active_queue.qsize() > 1:
            inactive_queue.put(self.active_queue.get())
        
        # Get the last element which is the top of the stack
        top_element = self.active_queue.get()
        
        # Swap the active and inactive queues
        self.active_queue = inactive_queue
        
        return top_element

    def top(self) -> int:
        # Transfer all elements except the last one to the other queue
        inactive_queue = self.queue2 if self.active_queue is self.queue1 else self.queue1
        while self.active_queue.qsize() > 1:
            inactive_queue.put(self.active_queue.get())
        
        # Get the last element which is the top of the stack
        top_element = self.active_queue.get()
        
        # Push it back to the inactive queue
        inactive_queue.put(top_element)
        
        # Swap the active and inactive queues
        self.active_queue = inactive_queue
        
        return top_element

    def empty(self) -> bool:
        # Check if the active queue is empty
        return self.active_queue.empty()

# Example usage:
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False
print("\n\n")

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if 
there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to 
denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return true if there 
is a cycle in the linked list. Otherwise, return false.
Model the Node and Linked List concepts using classes.
'''

print("Esercizio N.4 \n")
class Node:
    def __init__(self, value: int, next: 'Node' = None):
        self.value = value  # Initialize the node's value
        self.next = next  # Initialize the next node reference, default is None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    def append(self, value: int):
        if not self.head:
            # If the list is empty, create a new node and set it as the head
            self.head = Node(value)
        else:
            # If the list is not empty, traverse to the end and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    
    def get_node(self, index: int) -> Node:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None  # If the index is out of bounds

def has_cycle(head: Node) -> bool:
    if not head:
        # If the list is empty, there is no cycle
        return False

    slow = head  # Initialize slow pointer
    fast = head  # Initialize fast pointer

    while fast and fast.next:
        slow = slow.next  # Move slow pointer by 1 step
        fast = fast.next.next  # Move fast pointer by 2 steps

        if slow == fast:
            # If slow and fast pointers meet, there is a cycle
            return True

    # If fast pointer reaches the end, there is no cycle
    return False

# Example usage:
ll = LinkedList()
ll.append(3)
ll.append(2)
ll.append(0)
ll.append(-4)

# Creating a cycle manually for testing
node2 = ll.get_node(1)  # Node with value 2
node_last = ll.get_node(3)  # Node with value -4
node_last.next = node2  # -4 points back to 2 to form a cycle

print(has_cycle(ll.head))  # Output: True

ll_no_cycle = LinkedList()
ll_no_cycle.append(1)
ll_no_cycle.append(2)

print(has_cycle(ll_no_cycle.head))  # Output: False
print("\n\n")

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number 
of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, 
nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set 
to 0 and should be ignored. nums2 has a length of n.
'''

print("Esercizio N.5 \n")
def merge(nums1, m, nums2, n):
    # Start filling nums1 from the end
    i = m - 1  # Pointer for the last element in the initial part of nums1
    j = n - 1  # Pointer for the last element in nums2
    k = m + n - 1  # Pointer for the last position in nums1
    
    # Iterate while there are elements in both nums1 and nums2
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]  # Place the larger element at the end of nums1
            i -= 1  # Move the pointer in nums1
        else:
            nums1[k] = nums2[j]  # Place the larger element at the end of nums1
            j -= 1  # Move the pointer in nums2
        k -= 1  # Move the pointer in nums1

    # If there are remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
print("\n\n")

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
'''

print("Esercizio N.6 \n")
def is_valid_parenthesis(s: str) -> bool:
    stack = []  # Initialize an empty stack
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Iterate through each character in the string
    for char in s:
        if char in bracket_map.values():
            # If char is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_map.keys():
            # If char is a closing bracket
            if not stack:
                return False  # No matching opening bracket in stack
            top_element = stack.pop()  # Pop the top element from stack
            if bracket_map[char] != top_element:
                return False  # Closing bracket does not match the last opened bracket
    
    # After iterating through all characters, stack should be empty for valid parenthesis
    return len(stack) == 0

# Example usage:
print(is_valid_parenthesis("()"))  # Output: True
print(is_valid_parenthesis("()[]{}"))  # Output: True
print(is_valid_parenthesis("(]"))  # Output: False
print(is_valid_parenthesis("([)]"))  # Output: False
print(is_valid_parenthesis("{[]}"))  # Output: True
