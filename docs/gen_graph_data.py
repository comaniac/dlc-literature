import glob
import json
import os
import re

IGNORE_FILES = ["README.md"]

def main():
    data = {}
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
            "$dim": 5
        }

        adj = set()
        with open(file_name, "r") as fp:
            for line in fp:
                matches = re.findall(r"\[\[(.*?)\]\]", line)
                if not matches:
                    continue
                for match in matches:
                    print("\t%s" % match)
                    if match not in data:
                        data[match] = None
                    adj.add(match)
            node["adjacencies"] = list(adj)

        data[node["id"]] = node

    # Validation
    for name, node in data.items():
        if node is None:
            raise RuntimeError("Node definition missing: %s" % name)

    ret = "data = `[%s]`\n" % ",".join([json.dumps(v) for v in data.values()])
    with open("docs/data.json", "w") as fp:
        fp.write(ret)


if __name__ == "__main__":
    main()
