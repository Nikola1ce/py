# 括号匹配
# 括号匹配问题通常使用栈来解决。栈用于跟踪最近遇到的左括号，当遇到右括号时，检查栈顶是否有匹配的左括号。
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # 右括号到左括号的映射

    for char in s:
        if char in mapping:  # 如果是右括号
            if stack and stack[-1] == mapping[char]:  # 检查栈顶是否有匹配的左括号
                stack.pop()  # 匹配成功，弹出栈顶元素
            else:
                return False  # 没有匹配的左括号
        else:
            stack.append(char)  # 如果是左括号，压入栈

    return not stack  # 如果栈为空，说明所有括号都匹配成功

# 示例
print(is_valid_parentheses("()"))  # 输出：True
print(is_valid_parentheses("()[]{}"))  # 输出：True
print(is_valid_parentheses("(]"))  # 输出：False



# 逆波兰表达式（后缀表达式）的求值可以通过栈来实现。遇到数字时，将其压入栈；遇到运算符时，从栈中弹出两个操作数，进行运算后将结果压回栈。
def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:  # 如果是运算符
            b = stack.pop()  # 弹出第二个操作数
            a = stack.pop()  # 弹出第一个操作数
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # 注意整数除法
        else:
            stack.append(int(token))  # 如果是数字，压入栈

    return stack[0]  # 最终栈中只剩下一个元素，即结果

# 示例
tokens = ["2", "1", "+", "3", "*"]
print(evaluate_reverse_polish_notation(tokens))  # 输出：9


# 3. 单调栈
# 单调栈是一种特殊的栈结构，栈内的元素保持单调递增或单调递减。它常用于解决滑动窗口、下一个更大元素等问题。
# 示例：下一个更大元素
# 给定一个数组，找到每个元素后面的第一个比它大的元素。
def next_greater_element(nums):
    result = [-1] * len(nums)  # 初始化结果数组，默认值为-1
    stack = []  # 单调栈，存储索引

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:  # 如果栈顶元素小于当前元素
            idx = stack.pop()  # 弹出栈顶元素
            result[idx] = nums[i]  # 更新结果数组
        stack.append(i)  # 当前索引入栈

    return result

# 示例
nums = [4, 1, 2, 3]
print(next_greater_element(nums))  # 输出：[2, 2, 3, -1]


# 4. 单调栈：滑动窗口最大值
# 给定一个数组和一个窗口大小，找到每个窗口内的最大值。
from collections import deque
def max_sliding_window(nums, k):
    if not nums:
        return []
    
    result = []
    window = deque()  # 单调队列，存储索引

    for i in range(len(nums)):
        # 移除队列中不在当前窗口范围内的元素
        while window and window[0] <= i - k:
            window.popleft()

        # 移除队列中比当前元素小的元素，保持单调递减
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)  # 当前索引入队

        # 当窗口大小达到k时，开始记录结果
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# 示例
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(nums, k))  # 输出：[3, 3, 5, 5, 6, 7]