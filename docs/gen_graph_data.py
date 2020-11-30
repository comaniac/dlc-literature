import glob
import json
import os
import re

IGNORE_FILES = ["README.md"]

def main():
    data = {}
    adjs = {}
    for file_name_ in glob.glob("./*.md"):
        file_name = os.path.basename(file_name_)
        if file_name in IGNORE_FILES:
            continue

        # A graph node
        node = {}

        # Node name is the file name without suffix
        name = os.path.basename(file_name).replace(".md", "")
        node["name"] = name
        node["id"] = name
        print("Create node %s" % name)

        # TODO: More meaningful color and shape
        node["data"] = {
            "$color": "#557EAA",
            "$type": "circle",
            "$dim": 8
        }

        with open(file_name, "r") as fp:
            for line in fp:
                matches = re.findall(r"\[\[(.*?)\]\]", line)
                if not matches:
                    continue
                for match in matches:
                    if match not in data:
                        data[match] = None
                    if match not in adjs:
                        adjs[match] = set()
                    adjs[match].add(name)

        data[node["id"]] = node

    # Validation and process connections
    for name, node in data.items():
        if node is None:
            raise RuntimeError("Node definition missing: %s" % name)

        print("Node %s connects to:" % name)
        if name not in adjs: # Standalone node
            continue

        node["adjacencies"] = []
        for adj in adjs[name]:
            print("\t%s" % adj)
            adj_entry = {
                "nodeTo": adj,
                "nodeFrom": name,
            }
            node["adjacencies"].append(adj_entry)


    ret = "data = `[%s]`\n" % ",".join([json.dumps(v) for v in data.values()])
    with open("docs/data.json", "w") as fp:
        fp.write(ret)


if __name__ == "__main__":
    main()
