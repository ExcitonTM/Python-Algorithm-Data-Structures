# Leetcode Problems
Leet code problems compilation.


## Table of Contents
- [DFS & BFS](#dfs-and-bfs)
- [Union Find](#union-find)
- [Minimum Spanning Tree](#minimum-spanning-tree)
- [Sliding Window](#sliding-window)

## Backtracking
- [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

## DFS and BFS
- [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) \
If a graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and must be a tree. \
Problem can also be solved with Union find.
- [133. Clone Graph](https://leetcode.com/problems/clone-graph/) \
DFS through the graph. Use a hashmap to record node to newly cloned node.
- [1059. All Paths from Source Lead to Destination](https://leetcode.com/problems/all-paths-from-source-lead-to-destination) \
Backtrack all paths. Check for loop. Similar to 797

## Union Find
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) \
Can also use DFS/BFS.

- [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) 

- [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)

- [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/) \
Assign weight to union path.

## Minimum Spanning Tree

-[1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
- [1168. Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) \
Vertex also has weight like edges. The trick is to use one more imaginary vertex and assign vertex weight to edges
connecting to the imaginary vertex.


## Sliding window
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) 

- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)