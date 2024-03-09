graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": [],
}



visit = set()


def dfs(visit,graph,knot):
    if knot not in visit:
        print(knot)
        visit.add(knot)
        for neighbor in graph[knot]:
            dfs(visit,graph,neighbor)




dfs(visit,graph,"A")

