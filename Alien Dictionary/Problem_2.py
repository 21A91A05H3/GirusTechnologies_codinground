from collections import defaultdict, deque

def build_graph(words):
    graph = defaultdict(set)
    indegree = defaultdict(int)

    for word in words:
        for char in word:
            if char not in indegree:
                indegree[char] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return {}, {}

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    return graph, indegree

def alien_order(words):
    graph, indegree = build_graph(words)
    if not graph and not indegree:
        return ""

    # Print the graph (for debugging/understanding)
    print("Graph edges:")
    for node in graph:
        for neighbor in graph[node]:
            print(f"{node} -> {neighbor}")
    print()

    queue = deque([char for char in indegree if indegree[char] == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(indegree):
        return ""

    return "".join(order)

def run_test():
    words = ["baa", "abcd", "abca", "cab", "cad"]
    print("Words:", words)
    result = alien_order(words)
    print("\nTopological Order (Valid Character Order):", result)

run_test()

