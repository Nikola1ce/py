# 二叉树的遍历
# 二叉树的遍历方式主要有两种：广度优先遍历（Breadth-First Traversal） 和 深度优先遍历（Depth-First Traversal）。
# 广度优先遍历（层次遍历）
# 规则：从树的第一层（根节点）开始访问，从上而下逐层遍历，在同一层中，按从左至右的顺序对结点逐个访问。
# 实现：使用队列辅助实现。
from _9_Tree import TreeNode
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
# 时间复杂度：O(n)，其中 n 是二叉树中节点的总数。
# 空间复杂度：O(n)，在最坏情况下，队列中最多会存储一层的节点数。
# 深度优先遍历
# 深度优先遍历有三种常见的方式：前序遍历（Pre-order Traversal）、中序遍历（In-order Traversal） 和 后序遍历（Post-order Traversal）。
# 前序遍历：根节点 -> 左子树 -> 右子树

def preorder_traversal(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)
# 中序遍历：左子树 -> 根节点 -> 右子树
def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)
# 后序遍历：左子树 -> 右子树 -> 根节点
def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=" ")
# 时间复杂度：O(n)，每个节点都被访问一次。
# 空间复杂度：O(h)，其中 h 是树的高度。


# 二叉搜索树的操作
# 二叉搜索树（BST）是一种特殊的二叉树，满足左子树的值小于根节点，右子树的值大于根节点的值。
# 基本操作
# 查找：在BST中查找一个值是否存在。

def search(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
    
# 插入：在BST中插入一个新值。
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# 删除：在BST中删除一个值。
def delete(root, val):
    if not root:
        return root
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root
# 查找最大值和最小值：
# 最大值：在BST中，最大值位于最右边的节点。
# 最小值：在BST中，最小值位于最左边的节点。
def find_min(root):
    while root.left:
        root = root.left
    return root.val

def find_max(root):
    while root.right:
        root = root.right
    return root.val
# 平衡二叉树
# 平衡二叉树是一种特殊的二叉搜索树，要求左右子树的高度差不超过1。常见的平衡二叉树有AVL树和红黑树。
# 判断是否为平衡二叉树
# 可以通过递归计算每个节点的左右子树高度差来判断。

def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0, True
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced

    _, balanced = check_balance(root)
    return balanced
# 最近公共祖先问题
# 最近公共祖先（LCA）是指在一棵树中距离两个（或多个）节点的最近的祖宗节点。
# 解决方法
# 计算每个节点的深度：使用深度优先搜索计算每个节点的深度。
# 将两个节点调整到同一深度：将较深的节点向上跳，直到两个节点处于同一深度。
# 同时向上跳：将两个节点同时向上跳，直到它们重合，这个重合的节点就是最近公共祖先。
def find_lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right
# 树的深度与宽度计算
# 深度计算
# 递归计算节点深度：
def get_depth(node, current_depth=0):
    if not node:
        return current_depth
    return max(get_depth(node.left, current_depth + 1), get_depth(node.right, current_depth + 1))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
print('深度')
print(get_depth(tree))
# 非递归实现树的高度：使用层序遍历来计算树的高度。
from collections import deque
def get_tree_height(root):
    if not root:
        return 0
    queue = deque([root])
    height = 0
    while queue:
        #每次向下一层
        height += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return height
print('高度，同上面深度')
print(get_tree_height(tree))
# 宽度计算
# 树的宽度可以通过层序遍历计算，每层的最大宽度即为该层节点数的最大值。
def get_tree_width(root):
    if not root:
        return 0
    queue = deque([root])
    max_width = 0
    while queue:
        level_width = len(queue)
        max_width = max(max_width, level_width)
        for _ in range(level_width):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return max_width
print('宽度')
print(get_tree_width(tree))

