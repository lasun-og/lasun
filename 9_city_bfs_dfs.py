# GRAPH REPRESENTATION

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(nodes)
index = {nodes[i]: i for i in range(n)}

# Adjacency List (for BFS)
adjList = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['B', 'C'],
    'F': ['C']
}

# Adjacency Matrix (for DFS)
# Edges: A-B, A-C, B-D, B-E, C-E, C-F (symmetric matrix)
adjMatrix = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 1, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 1, 0, 0, 0],  # E
    [0, 0, 1, 0, 0, 0]   # F
]

visited = [False] * n
order = []

# BFS USING ADJACENCY LIST
def bfs(start):
    visitedLocal = []
    q = [start]
    visitedLocal.append(start)
    orderLocal = []

    while q:
        u = q.pop(0)
        orderLocal.append(u)
        for v in adjList[u]:
            if v not in visitedLocal:
                visitedLocal.append(v)
                q.append(v)

    print("\nBFS Traversal:")
    print("Visited:", visitedLocal)
    print("Order  :", orderLocal)


# DFS USING ADJACENCY MATRIX
def dfsMatrix(uIdx):
    visited[uIdx] = True
    order.append(nodes[uIdx])
    for vIdx in range(n):
        if adjMatrix[uIdx][vIdx] == 1 and not visited[vIdx]:
            dfsMatrix(vIdx)


def runDfs(start):
    global visited, order
    visited = [False] * n
    order = []
    dfsMatrix(index[start])
    print("\nDFS Traversal:")
    print("Visited:", [nodes[i] for i in range(n) if visited[i]])
    print("Order  :", order)


# MAIN MENU
while True:
    print("\n****** PRACTICAL NO-09 (GRAPH TRAVERSALS) ******")
    print("****** PREPARED BY : NANDINI N MATE ******")

    print("\n==== MENU ===")
    print("GRAPH REPRESENTATION IN MAIN PROGRAM:")
    print("Nodes (Locations):", nodes)
    print("Edges (Routes): A-B, A-C, B-D, B-E, C-E, C-F")

    print("\nMENU OPTIONS:")
    print("1. DISPLAY ADJACENCY LIST")
    print("2. DISPLAY ADJACENCY MATRIX")
    print("3. BFS TRAVERSAL")
    print("4. DFS TRAVERSAL")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE: ").strip()

    if choice == "1":
        print("\nAdjacency List:")
        for node in adjList:
            print(node, ":", adjList[node])

    elif choice == "2":
        print("\nAdjacency Matrix:")
        print("   ", " ".join(nodes))
        for i in range(n):
            print(nodes[i], ":", adjMatrix[i])

    elif choice == "3":
        start = input("ENTER START NODE (A-F): ").upper()
        if start in nodes:
            bfs(start)
        else:
            print("INVALID NODE.")

    elif choice == "4":
        start = input("ENTER START NODE (A-F): ").upper()
        if start in nodes:
            runDfs(start)
        else:
            print("INVALID NODE.")

    elif choice == "5":
        print("THANK YOU!!!!")
        break

    else:
        print("INVALID CHOICE. PLEASE ENTER (1-5).")

