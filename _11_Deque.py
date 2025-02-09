# 在 Python 中，deque（双端队列）是一种高效的双向队列，允许从两端快速添加和删除元素。它是 collections 模块中的一个类，提供了比普通列表更高效的队列操作。
# 为什么使用 deque？
# 普通列表（list）在头部插入或删除元素时效率较低，因为这需要移动列表中的所有元素。而 deque 在两端的操作时间复杂度为 O(1)，非常适合实现队列和栈。
# 如何使用 deque？
# 以下是一个完整的示例，展示如何使用 deque：
from collections import deque
# 创建一个 deque
d = deque([1, 2, 3])
# 添加元素
d.append(4)        # 右侧添加
d.appendleft(0)    # 左侧添加
print(d)           # 输出: deque([0, 1, 2, 3, 4])

# 移除元素
d.pop()            # 右侧移除
d.popleft()        # 左侧移除
print(d)           # 输出: deque([1, 2, 3])

# 扩展队列
d.extend([4, 5])   # 右侧扩展
d.extendleft([-1, 0])  # 左侧扩展
print(d)           # 输出: deque([-1, 0, 1, 2, 3, 4, 5])

# 旋转队列
d.rotate(2)        # 向右旋转 2 步
print(d)           # 输出: deque([4, 5, -1, 0, 1, 2, 3])

# 限制队列大小
d = deque(maxlen=3)
d.extend([1, 2, 3, 4])
print(d)           # 输出: deque([2, 3, 4])
# 应用场景
# deque 适用于以下场景：
# 队列和栈：实现高效的队列和栈操作。
# 滑动窗口：在滑动窗口问题中，deque 可以高效地维护窗口内的元素。
# 多线程环境：deque 是线程安全的，适合在多线程环境中使用。