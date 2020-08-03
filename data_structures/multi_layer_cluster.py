from scipy import spatial
from data_structures.union_find import UnionFind


def _shift_idx(match_ij, start_idx):
    for i in range(len(match_ij)):
        match_i = [match_idx + start_idx for match_idx in match_ij[i]]
        match_ij[i] = match_i
    return match_ij


class MultiLayerCluster:
    """

    """

    def __init__(self, layers):
        self.layers = layers
        self.match_all_layers = []
        self.layers_combined = []
        self.layer_start_idx = []
        self.layers_tree = []
        self.num_layers = len(layers)
        for layer in layers:
            self.layer_start_idx.append(len(self.layers_combined))
            if len(layer) > 0:
                self.layers_tree.append(spatial.KDTree(layer))
            else:
                # Handle KDTree exception for empty list
                self.layers_tree.append(None)
            self.layers_combined += layer

    def cluster_all_layers(self, self_r, other_r):
        for i in range(self.num_layers):
            tree_i = self.layers_tree[i]
            if tree_i:
                match_ii = tree_i.query_ball_tree(tree_i, self_r)
                match_i = _shift_idx(match_ii, self.layer_start_idx[i])
                for j in range(i + 1, self.num_layers):
                    tree_j = self.layers_tree[j]
                    if tree_j:
                        match_ij = tree_i.query_ball_tree(tree_j, other_r)
                    else:
                        match_ij = [[] for _ in range(len(self.layers[i]))]
                    match_ij = _shift_idx(match_ij, self.layer_start_idx[j])
                    match_i = [match_i[k] + match_ij[k] for k in range(len(self.layers[i]))]
            else:
                match_i = []
            self.match_all_layers += match_i
        return self.match_all_layers

    def compress_match(self):
        uf = UnionFind(len(self.match_all_layers))
        for i, connect in enumerate(self.match_all_layers):
            for j in connect:
                uf.union(i, j)
        return uf.list_unions()


if __name__ == '__main__':
    l1 = [(1, 1), (2, 2), (3, 3)]
    l2 = [(1.1, 1.1), (0.9, 0.9), (2.1, 2.1), (3.2, 3.2)]
    l3 = []
    l4 = [(1.15, 1.15), (3.1, 3.1)]
    layers = [l1, l2, l3, l4]
    cluster_r = 0.2
    dsa_r = 0.2
    dsa = MultiLayerCluster(layers)
    result = dsa.cluster_all_layers(cluster_r, dsa_r)
    print(dsa.compress_match())
