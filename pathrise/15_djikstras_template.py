import heapq
def djikstras(graph, start_node, end_node):
    # 1. Make priority queue and distance/cost dictionary
    pq = [(0, start_node, ())]
    heapq.heapify(pq)
    distance = {start_node: 0}
    
    # 2. Iterate over priority queue
    while pq:
        curr_cost, node, path = heapq.heappop(pq)
        if curr_cost > distance[node]: continue
        path += (node, )
        # 3. Terminating condition (Optional)
        if node == end_node:
            return (curr_cost, path)
        # 4. Add unvisited neighbours to queue
        for cost_to_neighbour, neighbour in graph[node]:
            old_cost = distance.get(neighbour, float('inf'))
            new_cost = curr_cost + cost_to_neighbour
            if new_cost < old_cost:
                distance[neighbour] = new_cost
                heapq.heappush(pq, (new_cost, neighbour, path))
    
    return float('inf') #if end node was not reached, cost is infinity and there is no path