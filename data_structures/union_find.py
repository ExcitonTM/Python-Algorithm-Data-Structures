class UnionFind:
    """List implementation of a union find data structure.

    The data structure tracks the parents of a list of elements and component size of each union.

    Args:
        size (int): total number of nodes. They will be numbered 0 to size-1.
    """
    def __init__(self, size):
        self.size = size
        self.parent_tracker = list(range(size))
        self.component_size = [1] * size

    def find_parent(self, p):
        """
        Find the parent index of a given index p. Do path compression after finding parent.

        Args:
            p (int): input node.

        Returns:
            int: the parent of the input node.

        """
        parent = p
        while parent != self.parent_tracker[parent]:
            parent = self.parent_tracker[parent]
        while p != parent:
            next_node = self.parent_tracker[p]
            self.parent_tracker[p] = parent
            p = next_node
        return parent

    def union(self, p, q):
        """
        Union two input nodes.

        Args:
            p (int): first input node.
            q (int): second input node.

        Returns:

        """
        parent_p = self.find_parent(p)
        parent_q = self.find_parent(q)
        if parent_p != parent_q:
            if self.component_size[parent_p] < self.component_size[parent_q]:
                self.component_size[parent_q] += self.component_size[parent_p]
                self.parent_tracker[parent_p] = parent_q
            else:
                self.component_size[parent_p] += self.component_size[parent_q]
                self.parent_tracker[parent_q] = parent_p
        return

    def list_unions(self):
        """

        Returns:
            dict: A dictionary of parents as keys and their follower nodes list as value.

        """
        union_dict = {}
        for idx in range(self.size):
            parent = self.find_parent(idx)
            union = union_dict.get(parent, [])
            union.append(idx)
            union_dict[parent] = union
        return union_dict


if __name__ == '__main__':
    test_case = [[0, 3, 4], [1, 5], [2, 6], [3, 4], [4], [5], [6]]
    uf = UnionFind(len(test_case))
    for i, connect in enumerate(test_case):
        for j in connect:
            uf.union(i, j)
    print(uf.parent_tracker)
    print(uf.list_unions())
