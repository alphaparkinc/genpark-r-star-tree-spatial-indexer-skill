class RStarNode:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.entries = []

class RStarTree:
    """
    R*-Tree Spatial Indexer for 2D bounding boxes.
    """
    def __init__(self, max_cap=4):
        self.max_cap = max_cap
        self.root = RStarNode(is_leaf=True)

    def insert(self, mbr, item):
        self.root.entries.append((mbr, item))

    def query_range(self, query_mbr):
        results = []
        qx1, qy1, qx2, qy2 = query_mbr
        for (x1, y1, x2, y2), item in self.root.entries:
            if not (x2 < qx1 or x1 > qx2 or y2 < qy1 or y1 > qy2):
                results.append(item)
        return results
