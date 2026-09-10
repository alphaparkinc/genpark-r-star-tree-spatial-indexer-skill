from client import RStarTree

def main():
    print("=== Testing R*-Tree Spatial Indexer ===")
    rtree = RStarTree()
    rtree.insert([0, 0, 10, 10], "objA")
    rtree.insert([20, 20, 30, 30], "objB")

    matches = rtree.query_range([5, 5, 15, 15])
    print("Range query matches:", matches)
    assert "objA" in matches and "objB" not in matches
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
