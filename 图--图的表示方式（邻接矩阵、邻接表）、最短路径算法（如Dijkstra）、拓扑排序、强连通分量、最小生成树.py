# 1. 邻接矩阵表示图
class GraphAdjMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        # 无向图
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight
        # 如果是有向图，去掉上面的 self.matrix[v][u] = weight

    def print_matrix(self):
        for row in self.matrix:
            print(row)

# 示例
g = GraphAdjMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_matrix()
# 输出结果
# [0, 1, 1, 0]
# [1, 0, 1, 0]
# [1, 1, 0, 1]
# [0, 0, 1, 0]

# 2. 邻接表表示图
class GraphAdjList:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        # 无向图
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
        # 如果是有向图，去掉上面的 self.adj_list[v].append((u, weight))

    def print_adj_list(self):
        for i, neighbors in enumerate(self.adj_list):
            print(f"{i}: {neighbors}")

# 示例
g = GraphAdjList(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.print_adj_list()
# 输出结果
# 0: [(1, 1), (2, 1)]
# 1: [(0, 1), (2, 1)]
# 2: [(0, 1), (1, 1), (3, 1)]
# 3: [(2, 1)]
# 总结
# 邻接矩阵：适用于稠密图，实现简单，但空间复杂度高。
# 邻接表：适用于稀疏图，空间复杂度低，但查找边的存在性需要遍历链表。


#  最短路径算法
# 2.1 Dijkstra 算法
# Dijkstra 算法用于计算从单个源点到图中所有其他顶点的最短路径。它适用于无负权边的图。
# 算法步骤：
# 初始化：将源点的距离设为 0，其他所有顶点的距离设为无穷大。
# 使用优先队列（最小堆）存储顶点及其距离。
# 每次从优先队列中取出距离最小的顶点 u，更新与 u 相连的所有顶点的距离。
# 重复上述步骤，直到所有顶点都被处理。
import heapq
grap = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
def dijkstra(graph, start):
    # graph 是一个字典，键为节点，值为邻接节点及其距离的列表
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # 堆中存储(距离, 节点)对

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) 
        # 节点已经在更短路径上处理过，跳过
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # 只有当找到更短的路径时才进行更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

print(dijkstra(grap,'C'))