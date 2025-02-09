# 6. 栈（Stack）
# 栈是一种后进先出（LIFO）的数据结构，通常用于递归调用等场景。
# 特点：
# 元素从栈顶添加和移除。
# Python 中可以用列表来实现栈。

# 创建栈
my_stack = []

# 添加元素
my_stack.append(1)
my_stack.append(2)

print(my_stack)
# 移除元素
print(my_stack.pop())  # 输出 2
print(my_stack.pop())  # 输出 1