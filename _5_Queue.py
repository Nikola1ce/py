# 5. 队列（Queue）
# 队列是一种先进先出（FIFO）的数据结构，通常用于任务调度等场景。
# 特点：
# 元素从队列头部移出，从队列尾部添加。
# Python 提供了 queue.Queue 模块来实现线程安全的队列。
# 常用操作：
# Python
# 复制
from queue import Queue

# 创建队列
my_queue = Queue()

# 添加元素
my_queue.put(1)
my_queue.put(2)

# 获取弹出元素
print(my_queue.get())  # 输出 1
print(my_queue.get())  # 输出 2

print(my_queue.empty())  # 检查队列是否为空。
my_queue.maxsize = 2
my_queue.put(1)
my_queue.put(2)
print(my_queue.full())  # 检查队列是否已满（需要设置队列的最大长度）。
print(my_queue.qsize())  # 返回队列中元素的数量。
