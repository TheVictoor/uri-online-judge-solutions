import math

import sys
sys.setrecursionlimit(100000)

n, quantity_by_travel = [int(i) for i in input().strip().split()]
taxes = [int(i) for i in input().strip().split()]
taxes.insert(0, 0)
visided = [False for _ in range(n+1)]
graphs = {}

class Edge:
    def __init__(self, name):
        self.name = name
        self.neighbors = []


while True:
    try:
        a, b, cost = [int(i) for i in input().strip().split()]

        a_edge = graphs.get(a) or Edge(name=a)
        b_edge = graphs.get(b) or Edge(name=b)

        a_edge.neighbors.append((b_edge, cost))
        b_edge.neighbors.append((a_edge, cost))

        graphs[a] = a_edge
        graphs[b] = b_edge
    except: 
        break


travels = 0
def dfs(city: Edge, cost):
    global travels

    city_tax = taxes[city.name]
    visided[city.name] = True

    for neightbor, n_cost in city.neighbors:
        if not visided[neightbor.name]:
            city_tax += dfs(neightbor, n_cost)

    n_travels = math.ceil(city_tax/quantity_by_travel)   
    travels += n_travels * 2 * cost

    return city_tax    

travels = 0
dfs(graphs.get(1), 0)
print(travels)
