# visited = set()
# structure = initial_structure()   # queue, stack, recursion
#
# add(start)
#
# while structure not empty:
#     node = get_next(structure)
#
#     if node in visited:
#         continue
#
#     visited.add(node)
#
#     process(node)
#
#     for neighbor in neighbors(node):
#         if neighbor not in visited:
#             add(neighbor)

def traverse(start, graph):
    visited = set()
    stack = [start]  # або queue, або recursion

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        process(node)

        for nei in graph[node]:
            if nei not in visited:
                stack.append(nei)