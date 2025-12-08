boxes = [
    tuple(map(int, line.split(",")))
    for line in open("input").read().strip().split("\n")
]


parents = [i for i in range(len(boxes))]
ranks = [0 for _ in range(len(boxes))]


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if ranks[rootX] > ranks[rootY]:
            parents[rootY] = rootX
        elif ranks[rootX] < ranks[rootY]:
            parents[rootX] = rootY
        else:
            parents[rootY] = rootX
            ranks[rootX] += 1


edges = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dist = (
            (boxes[i][0] - boxes[j][0]) ** 2
            + (boxes[i][1] - boxes[j][1]) ** 2
            + (boxes[i][2] - boxes[j][2]) ** 2
        )
        edges.append((dist, i, j))
edges.sort()

# for i in range(1000):
#     d, u, v = edges[i]
#     union(u, v)

# components = {}
# for i in range(len(boxes)):
#     comp_id = find(i)
#     components[comp_id] = components.get(comp_id, set()) | {i}

# sizes = sorted([len(component) for component in components.values()])

# print(sizes[-1] * sizes[-2] * sizes[-3])

number_of_components = len(boxes)
for d, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        number_of_components -= 1
        if number_of_components == 1:
            print(boxes[u][0] * boxes[v][0])
