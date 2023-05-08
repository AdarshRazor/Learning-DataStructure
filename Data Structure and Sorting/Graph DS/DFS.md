# Depth First Search

Breadth-first search starts at a specific node and explores as far as possible along each branch before backtracking.

It explores as deep as possible before backtracking. Depth-first search can be implemented recursively or iteratively using a stack. 

![image](https://user-images.githubusercontent.com/33658792/236693272-4439d949-fcb6-466e-8730-e946091bd903.png)

## Implementation

1. Choose a starting node to begin the search.
2. Create an empty set to keep track of visited nodes.
3. Start with the given/starting node.
4. While the queue is not empty, dequeue a node from the front of the queue.
5. If the vertex has not been visited yet, mark it as visited and print it.
6. Add all unvisited neighbors of the current node to the back of the queue.
7. Repeat the process until the queue is empty and you are done. :fire:

## Space and time complexity

* Worst complexity:  O(|V| + |E|), where |V| is the number of vertices (nodes) in the graph and |E| is the number of edges.
* Average complexity: O(|V| + |E|), since in most cases, we will not need to traverse the entire graph.
* Best complexity: O(|V|), when the starting node is the only node in the graph.
* Space complexity: O(|V|), since in the worst case, we will need to store all the nodes in the queue.

## When to use

- It is useful for finding paths between two nodes in a graph.

- You want to detect cycles in a graph.

- You have `limited memory`, as DFS can be implemented recursively with constant space complexity.

Here is the [link](https://www.youtube.com/watch?v=Y40bRyPQQr0) of the video from GeeksforGeeks which might clear you idea.

## Implementation (Code)

```python
# Define a graph as a dictionary
graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}

# Define a function to perform DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Call the dfs function with a starting node
dfs(graph, 'A')
```

Output:

`A`

`B`

`D`

`E`

`F`

`C`