import sys
import json
from client import RStarTree

def main():
    rtree = RStarTree()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "insert":
            rtree.insert(params.get("mbr", []), params.get("item"))
            res = {"status": "ok"}
        elif method == "query":
            res = {"matches": rtree.query_range(params.get("query_mbr", []))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
