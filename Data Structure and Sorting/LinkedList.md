# Linked List

* Linear Data Structure
* Elements are stored as per memory availability
* Can access elements randomly using index
* Stores homogeneous elements i.e, similar elements
* Dynamic in size
* Easy to insert and delete elements
* Starting element or node is the key which is generally termed as head.

## Advantages and Disadvantages

* Advantages of Linked List:
    * Dynamic in size
    * No wastage of memory and size is always equal.
    * Easy to insert and delete elements.
    * Efficient memory allocation.
* Disadvantages of Linked List:
    * Random access is not possible.
    * If head is deleted, then entire list is lost.

## Implementation (Code)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next

```

```python
# Create a new linked list
my_list = LinkedList()

# Add some nodes to the list
my_list.add(1)
my_list.add(2)
my_list.add(3)

# Print the list
my_list.print() # Output: 1 2 3

# Remove a node from the list
my_list.remove(2)

# Print the list again
my_list.print() # Output: 1 3
```