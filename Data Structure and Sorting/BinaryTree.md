# Binary Tree
 
It is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.
 
Each node in a binary tree contains a value. The left child is less than parent node, while the right child is greater than the parent node.

## Implementation

1. Define a Node class to represent each node in the binary tree.
2. Define a BinaryTree class to represent the binary tree itself, with a root attribute that references the root Node.
3. Define a method to insert a new Node into the binary tree, following the binary search tree condition. `[left child is less than parent node, while the right child is greater than the parent node]`
4. Define a method to search for a value in the binary tree, by recursively traversing the tree until the value is found or a leaf node is reached.
5. Define a method to delete a node from the binary tree, handling three cases: no children, one child, or two children.
6. Define methods to traverse the binary tree in-order, pre-order, and post-order, visiting each node in the desired order and you are done. :fire:

<br>

* In-order traversal: Visit the left subtree, then the current node, then the right subtree.
* Pre-order traversal: Visit the current node, then the left subtree, then the right subtree.
* Post-order traversal: Visit the left subtree, then the right subtree, then the current node.

## Space and time complexity

* Worst complexity: O(n)
* Average complexity: 
    * Balanced tree: O(log n)
    * Unbalanced tree: O(n)
* Best complexity: O(1)
* Space complexity: O(n), where n is the number of nodes in the tree.

## When to use

- When you have a large dataset that needs to be efficiently searched or sorted.

- When you need to maintain a tree structure that can be easily modified by adding or deleting nodes.

Here is the [link](https://www.youtube.com/watch?v=W6aZKAJcNJA) of the video from GeeksforGeeks which might clear you idea.

## Advantages and Disadvantages

* Advantages [Balanced]:
    * Efficient for searching and retrieving data.
    * Allows for efficient insertion and deletion of nodes.
    * Provides a hierarchical structure that can be used to model relationships between data, such as in family trees or organizational charts.
    * Can be used to implement other data structures such as priority `queues and heaps`.
* Disadvantages [Unbalanced]:
    * Unbalanced trees can lead to inefficient searching and retrieving of data, reducing performance.
    * Insertion and deletion of nodes can be inefficient for unbalanced trees.

## Implementation (Code)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        parent = None
        current = self.root
        while current is not None:
            if value == current.value:
                # Case 1: no children
                if current.left is None and current.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                # Case 2: one child
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                # Case 3: two children
                else:
                    # Find the smallest value in the right subtree
                    successor = current.right
                    while successor.left is not None:
                        successor = successor.left
                    # Replace the node to be deleted with the successor
                    current.value = successor.value
                    # Delete the successor
                    self.delete(successor.value)
                return
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)

```
