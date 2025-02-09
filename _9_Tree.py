# 9. 树（Tree）
# 树是一种分层的数据结构，每个节点可以有多个子节点。
# 特点：
# 常见的树有二叉树、二叉搜索树、平衡树等。
# Python 中没有内置的树类型，但可以通过类来实现。
# 示例实现（二叉树）：
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 创建二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)