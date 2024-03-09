graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
}

visit = []
stack = []


def bfs(visit,graph,knot):
    visit.append(knot)
    stack.append(knot)

    while stack:
        s = stack.pop(0)
        print(s, end=" ")


        for neighbor in graph[s]:
            if neighbor not in visit:
                stack.append(neighbor)



bfs(visit, graph, "A")

