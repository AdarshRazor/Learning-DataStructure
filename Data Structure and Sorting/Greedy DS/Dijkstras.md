# Dijkstra's algorithm

Dijkstra's algorithm finds the shortest path between two nodes in a graph.

It is a weighted graph algorithm, meaning that each edge in the graph has a weight associated with it.

![image](https://user-images.githubusercontent.com/33658792/236693272-4439d949-fcb6-466e-8730-e946091bd903.png)

## Implementation

1. Create a set of unvisited nodes and set the distance to the starting node as zero, and all other distances as infinity.
2. Select the unvisited node with the smallest distance, this will be the current node.
3. For each neighbor of the current node, calculate the distance and the weight of the edge between the current node and the neighbor.
4. If this calculated distance is less than the neighbor's current distance, update the neighbor's distance to the calculated distance.
5. Mark the current node as visited.
6. When all nodes have been visited, the algorithm has finished and the shortest distances to all nodes from the starting node have been found and you are done. :fire:

## Space and time complexity

* Worst complexity: O((E+V) * log V)
* Average complexity: O((E+V) * log V)
* Best complexity: O(V^2)
* Space complexity: O(V)

Where `E is the number of edges` and `V is the number of vertices` in the graph.

## When to use

- When need to find the shortest path between two nodes in a weighted graph.

Here is the [link](https://www.youtube.com/watch?v=hFnVSiQMktA) of the video from GeeksforGeeks which might clear you idea.

## Implementation (Code)

```python
import heapq

def dijkstra(graph, start):
    # Initialize the distances to all nodes as infinity except for the starting node, which has distance 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Initialize the priority queue with the starting node and its distance
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        (current_distance, current_node) = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the distance in the distances dictionary, skip this iteration
        if current_distance > distances[current_node]:
            continue
            
        # Visit all the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the tentative distance to the neighbor node
            tentative_distance = current_distance + weight
            
            # Update the distance in the distances dictionary if the tentative distance is smaller
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                
                # Add the neighbor and its distance to the priority queue
                heapq.heappush(priority_queue, (tentative_distance, neighbor))
                
    return distances

```