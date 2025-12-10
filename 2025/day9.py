import random

coords = open("input").read().strip().split("\n")
coords = [tuple(map(int, coord.split(","))) for coord in coords]


max_x = max(x for x, y in coords)
max_y = max(y for x, y in coords)


def area_rectangle(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (1 + abs(y2 - y1))


edges = set()

coords_x = {}
coords_y = {}
pts_connected = {}
for x, y in coords:
    if x not in coords_x:
        coords_x[x] = [y, -1]
    else:
        prev_y1 = coords_x[x][0]
        coords_x[x][0] = min(prev_y1, y)
        coords_x[x][1] = max(prev_y1, y)
        edges.add(((x, prev_y1), (x, y)))
        pts_connected[(x, prev_y1)] = pts_connected.get((x, prev_y1), []) + [(x, y)]
        pts_connected[(x, y)] = pts_connected.get((x, y), []) + [(x, prev_y1)]

    if y not in coords_y:
        coords_y[y] = [x, -1]
    else:
        prev_x1 = coords_y[y][0]
        coords_y[y][0] = min(prev_x1, x)
        coords_y[y][1] = max(prev_x1, x)
        edges.add(((prev_x1, y), (x, y)))
        pts_connected[(prev_x1, y)] = pts_connected.get((prev_x1, y), []) + [(x, y)]
        pts_connected[(x, y)] = pts_connected.get((x, y), []) + [(prev_x1, y)]


def ray_cast(pts, test):
    inside = False
    xt, yt = test
    n = len(pts)
    for k in range(n):
        xi, yi = pts[k]
        xj, yj = pts[(k + 1) % n]
        if ((yi > yt) != (yj > yt)) and (xt < (xj - xi) * (yt - yi) * (yj - yi) + xi):
            inside = not inside
    return inside


polygons = []
start = list(pts_connected.keys())[0]
current = start
prev = None
while len(polygons) != len(edges):
    nxt1, nxt2 = pts_connected[current]
    if nxt1 == prev:
        nxt1 = nxt2
    prev = current
    current = nxt1
    polygons.append(current)


def on_segment(pt):
    edge1 = coords_x.get(pt[0], None)
    edge2 = coords_y.get(pt[1], None)
    if edge1 is not None:
        y1, y2 = edge1
        if y1 <= pt[1] <= y2:
            return True
    if edge2 is not None:
        x1, x2 = edge2
        if x1 <= pt[0] <= x2:
            return True
    return False


ans = 0
for i in range(len(coords)):
    x1, y1 = coords[i]
    for j in range(i + 1, len(coords)):
        x2, y2 = coords[j]
        if x1 == x2 or y1 == y2:
            continue
        area = area_rectangle(x1, y1, x2, y2)
        if area <= ans:
            continue
        inside = True
        # select random points along the edges
        nb_points = min(1000, abs(x2 - x1) + 1)
        points = random.sample(range(min(x1, x2), max(x1, x2) + 1), nb_points)
        for i in points:
            # for i in range(min(x1, x2), max(x1, x2) + 1):
            if not (ray_cast(polygons, (i, y1)) or on_segment((i, y1))) or not (
                on_segment((i, y2)) or ray_cast(polygons, (i, y2))
            ):
                inside = False
                break
        nb_points = min(1000, abs(y2 - y1) + 1)
        points = random.sample(range(min(y1, y2), max(y1, y2) + 1), nb_points)
        for j in points:
            # for j in range(min(y1, y2), max(y1, y2) + 1):
            if not (ray_cast(polygons, (x1, j)) or on_segment((x1, j))) or not (
                on_segment((x2, j)) or ray_cast(polygons, (x2, j))
            ):
                inside = False
                break
        if inside:
            print("FOUND ONE")
            ans = max(ans, area)
            # print(x1, y1, x2, y2, ans)
            print(ans)

print(ans)
