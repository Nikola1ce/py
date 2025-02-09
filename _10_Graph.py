# 10. 图（Graph）
# 图是一种由节点和边组成的复杂数据结构，用于表示复杂的关系网络。
# 特点：
# 图可以是有向图或无向图，边可以有权重。
# Python 中没有内置的图类型，但可以通过字典或类来实现。
# 示例实现（无向图）：
# 使用字典表示图
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# 遍历图
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

print(dfs(graph, "A"))  # 输出所有可达的节点