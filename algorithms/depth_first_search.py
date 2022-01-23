class DFS:
    def __init__(self, num_nodes, adjacency_list):
        self.graph = adjacency_list
        self.num_nodes = num_nodes
        self.visited = [False] * num_nodes

    def dfs_from(self, at):
        # Finish dfs if node "at" is visited
        if self.visited[at] is True:
            return []
        self.visited[at] = True
        path = [at]
        neighbours = self.graph[at]
        for nxt in neighbours:
            path.extend(self.dfs_from(nxt))
        return path


if __name__ == '__main__':
    g = [[1, 2], [3], [4, 5], [6], [3], [6, 7], [], []]
    n = len(g)
    my_dfs = DFS(n, g)
    r0 = my_dfs.dfs_from(2)
    print(r0)
    print(my_dfs.visited)
