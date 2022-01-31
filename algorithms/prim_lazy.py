import heapq


class PrimLazy:
    def __init__(self, num_nodes, adjacency_list_with_weight):
        """
        Implementation of Prim algorithm to find minimum spanning tree. "Lazy" means we keep all edges from explored
        territory to unexplored in a heap. Only when we pop the edge from the heap, we check if
        the destination edge has already been reached through an edge with smaller weight earlier.
        The algorithm can optimized with an "eager" implementation where for a given node, only
        the edge with the smallest weight is stored(in an indexed priority queue as opposed to heap).
        Args:
            num_nodes:
            adjacency_list_with_weight:
        """
        self.num_nodes = num_nodes
        self.graph = adjacency_list_with_weight
        self.pq = []

    def mst(self, s=0):
        mst_edges = []
        mst_cost = 0
        visited = [False] * self.num_nodes
        self._add_edges(s, visited)
        while len(self.pq) > 0 and (len(mst_edges) != self.num_nodes-1):
            weight, from_node, to_node = heapq.heappop(self.pq)
            if visited[to_node]:
                continue
            mst_cost += weight
            mst_edges.append((from_node, to_node, weight))
            self._add_edges(to_node, visited)

    def _add_edges(self, node, visited):
        visited[node] = True
        for neighbor_with_weight in self.graph[node]:
            neighbor, weight = neighbor_with_weight
            if not visited[neighbor]:
                heapq.heappush(self.pq, (weight, node, neighbor))




