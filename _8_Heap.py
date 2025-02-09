# 在 Python 中，heapq 模块提供了一种实现堆（heap）的方式，主要用于实现优先队列（priority queue）。堆是一种特殊的完全二叉树，分为最小堆（min-heap）和最大堆（max-heap）。
# 最小堆（Min-Heap）
# 定义：在最小堆中，父节点的值总是小于或等于其子节点的值。
# 性质：
# 堆顶（根节点）是所有节点中的最小值。
# 任意节点的值都小于或等于其子节点的值。
# 应用场景：
# 实现优先队列，用于处理任务调度、事件驱动模拟等。
# 在算法中用于快速获取最小值，如 Dijkstra 算法。
# 最大堆（Max-Heap）
# 定义：在最大堆中，父节点的值总是大于或等于其子节点的值。
# 性质：
# 堆顶（根节点）是所有节点中的最大值。
# 任意节点的值都大于或等于其子节点的值。
# 应用场景：
# 实现优先队列，用于处理任务调度、事件驱动模拟等。
# 在算法中用于快速获取最大值，如堆排序。
# Python 的 heapq 模块
# Python 的 heapq 模块默认实现的是最小堆。它提供了一系列函数来操作堆，包括插入、删除等操作。

# 常用函数
# heapq.heappush(heap, item)：
# 将 item 添加到堆中，并保持堆的性质。
# 时间复杂度：O(log n)。
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heap)  # 输出：[1, 3, 2]

# heapq.heappop(heap)：
# 从堆中移除并返回最小的元素（堆顶元素），并保持堆的性质。
# 时间复杂度：O(log n)。
heap = [1, 3, 2]
heapq.heapify(heap)  # 将列表转换为堆
print(heapq.heappop(heap))  # 输出：1
print(heap)  # 输出：[2, 3]

# heapq.heapify(x)：
# 将列表 x 转换为堆。
# 时间复杂度：O(n)。
lst = [3, 1, 2]
heapq.heapify(lst)
print(lst)  # 输出：[1, 3, 2]

# heapq.nsmallest(n, iterable)：
# 返回 iterable 中最小的 n 个元素，保持原始顺序。
lst = [3, 1, 2, 4, 5]
print(heapq.nsmallest(3, lst))  # 输出：[1, 2, 3]

# heapq.nlargest(n, iterable)：
# 返回 iterable 中最大的 n 个元素，保持原始顺序。
lst = [3, 1, 2, 4, 5]
print(heapq.nlargest(3, lst))  # 输出：[5, 4, 3]

# 实现最大堆
# 虽然 heapq 默认实现的是最小堆，但可以通过对元素取负值来实现最大堆的效果。
# 创建一个最大堆
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
# 获取最大值
max_value = -heapq.heappop(max_heap)
print(max_value)  # 输出：3

# 使用 heapq 的注意事项
# 堆的性质：heapq 模块的堆是基于列表实现的，堆顶元素始终是列表的第一个元素。
# 最大堆的实现：通过将元素取负值，可以利用最小堆实现最大堆。
# 性能：heapq 的插入和删除操作的时间复杂度为 O(log n)，堆化操作的时间复杂度为 O(n)。