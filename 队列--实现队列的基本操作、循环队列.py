# 队列的基本操作
# 队列（Queue）是一种先进先出（FIFO，First In First Out）的数据结构，元素从队列的一端添加，从另一端移除。队列的基本操作包括：
# 1. 初始化队列
# 创建一个空队列。
queue = []
# 2. 入队（Enqueue）
# 将一个元素添加到队列的尾部。
queue.append(1)
queue.append(2)
# 3. 出队（Dequeue）
# 从队列的头部移除一个元素，并返回该元素。如果队列为空，通常会抛出异常或返回一个特殊值。
if queue:
    element = queue.pop(0)
else:
    raise IndexError("Queue is empty")
# 4. 查看队首元素（Peek）
# 查看队列头部的元素，但不移除它。

if queue:
    front_element = queue[0]
else:
    raise IndexError("Queue is empty")
# 5. 检查队列是否为空
# 判断队列是否为空。

is_empty = len(queue) == 0
# 6. 获取队列的大小
# 获取队列中元素的数量。

size = len(queue)
# 循环队列（Circular Queue）
# 循环队列是一种高效的队列实现方式，通过将队列的尾部连接到头部，形成一个环形结构，从而避免了普通队列在出队操作中频繁移动元素的问题。
# 特点
# 空间高效：避免了普通队列中因出队操作导致的元素移动，提高了空间利用率。
# 时间复杂度：入队和出队操作的时间复杂度均为 O(1)。

class CircularQueue:
    def __init__(self, k: int):
        self.k = k  # 队列的最大容量
        self.queue = [None] * k  # 初始化队列
        self.head = 0  # 队首指针
        self.tail = 0  # 队尾指针
        self.count = 0  # 当前队列中的元素数量

    def enqueue(self, value: int) -> bool:
        """入队操作"""
        if self.is_full():
            return False  # 队列已满，无法入队
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True

    def dequeue(self) -> bool:
        """出队操作"""
        if self.is_empty():
            return False  # 队列为空，无法出队
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def front(self) -> int:
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.head]

    def is_empty(self) -> bool:
        """检查队列是否为空"""
        return self.count == 0

    def is_full(self) -> bool:
        """检查队列是否已满"""
        return self.count == self.k

    def size(self) -> int:
        """获取队列的大小"""
        return self.count

# 示例
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
print(cq.front())  # 输出: 1
cq.dequeue()
print(cq.front())  # 输出: 2
# 循环队列的关键点
# 队首指针和队尾指针：
# head 指向队首元素。
# tail 指向下一个入队的位置。
# 环形结构：
# 使用模运算 % 来实现环形结构，避免数组越界。
# 队列已满和队列为空的判断：
# 队列为空：count == 0。
# 队列已满：count == k。