from itertools import combinations
from functools import reduce
from networkx.utils import UnionFind

def prod(terms: list[int]):
    return reduce(
        lambda a, b: a * b,
        terms,
        1
    )

def dist(a, b):
    p1, p2, p3 = a
    q1, q2, q3 = b

    return (((p1 - q1) ** 2) + ((p2 - q2) ** 2) + ((p3 - q3) ** 2)) ** 0.5

file_path = './input.txt'

with open(file_path, 'r') as file:
    lines = [l.strip() for l in file.readlines()]

junctions = [eval(s) for s in lines]
total = len(junctions)

connections = sorted(zip(
    map(lambda p: dist(p[0], p[1]), combinations(junctions, 2)),
    combinations(range(total), 2)))

find = UnionFind(range(total))
inc = total

for i, (distance, connection) in enumerate(connections):
    if find[connection[0]] != find[connection[1]]:
        inc -= 1

        find.union(*connection)

        if inc == 1:
            print(junctions[connection[0]][0] * junctions[connection[1]][0])
        
            break