# Binary Tree
 
It is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.
 
Each node in a binary tree contains a value. The left child is less than parent node, while the right child is greater than the parent node.

## Implementation

1. Define a Node class to represent each node in the binary tree.
2. Define a BinaryTree class to represent the binary tree itself, with a root attribute that references the root Node.
3. Define a method to insert a new Node into the binary tree, following the binary search tree condition.
4. Define a method to search for a value in the binary tree, by recursively traversing the tree until the value is found or a leaf node is reached.
5. Define a method to delete a node from the binary tree, handling three cases: no children, one child, or two children.
6. Define methods to traverse the binary tree in-order, pre-order, and post-order, visiting each node in the desired order and you are done. :fire:


## Space and time complexity

* Worst complexity: n^2
* Average complexity: n^2
* Best complexity: n
* Space complexity: 1

## When to use

- Bubble sort is easy to implement.

- It is fast enough when you have small data sets.

Here is the [link](https://www.youtube.com/watch?v=nmhjrI-aW5o) of the video from GeeksforGeeks which might clear you idea.

```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [27,13,57,43,98,3,7,11,45,21,100]

print(bubble_sort(arr))
```
