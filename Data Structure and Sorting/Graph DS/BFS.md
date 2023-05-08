# Breath First Search

Breadth-first search is a way of exploring a graph or tree by visiting all the nodes at the same "level" or "depth" before moving on to the next level.

It starts at the root node (or any arbitrary node), visits all its neighbors (the nodes directly connected to it), and then moves on to the neighbors' neighbors, and so on, until all nodes have been visited.

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

- It is useful for finding the shortest path between two nodes in an unweighted graph.

- You want to find the smallest number of steps to reach a solution in a search problem.

- You want to traverse a tree or graph level by level.

Here is the [link](https://www.youtube.com/watch?v=0u78hx-66Xk) of the video from GeeksforGeeks which might clear you idea.

## Implementation (Code)

```python
from collections import deque

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    visited = set()      # Set to keep track of visited nodes
    queue = deque([start]) # Start with the given node
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        
        # If the vertex has not been visited yet, mark it as visited and print it
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
        
            # Add all of its neighbors to the queue
            queue.extend(graph[vertex] - visited)
    
    return visited

# Call the bfs function to traverse the graph starting from the node 'A'
bfs(graph, 'A')
```

Output: `A B C D E F G`
