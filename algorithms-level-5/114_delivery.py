def solution(N, road, K):
    from collections import defaultdict, deque

    # Create a graph from the road information
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Initialize distances with infinity
    distances = {i: float('inf') for i in range(1, N + 1)}
    distances[1] = 0  # Starting point

    # Use a queue for BFS
    queue = deque([1])

    while queue:
        current = queue.popleft()
        current_distance = distances[current]

        for neighbor, weight in graph[current]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                queue.append(neighbor)

    # Count how many nodes are reachable within distance K
    return sum(1 for d in distances.values() if d <= K)   
    
    
    
    
    
    
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # Output: 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # Output: 4
