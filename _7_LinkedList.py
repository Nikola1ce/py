# 7. 链表（LinkedList）
# 链表是一种线性数据结构，每个节点包含数据部分和指向下一个节点的指针。
# 特点：
# 动态数据结构，可以高效地插入和删除元素。
# Python 中没有内置的链表类型，但可以通过类来实现。
# 示例实现：
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """在链表末尾添加一个节点"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        """删除链表中值为key的节点"""
        # 保存头节点
        temp = self.head
        # 如果头节点就是要删除的节点
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # 查找要删除的节点
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # 如果没有找到要删除的节点
        if temp == None:
            return
        # 从链表中删除节点
        prev.next = temp.next
        temp = None
    

    def print_list(self):
        """打印链表"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    def reverse_linked_list(self):
        """翻转链表"""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # 保存下一个节点
            current.next = prev  # 反转当前节点的指针
            prev = current  # 移动prev指针
            current = next_node  # 移动current指针
        self.head = prev  # 返回新的头节点
        
    def has_cycle(self):
        """是否有环"""
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__=='__main__':
    # 创建链表
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("原始链表：")
    ll.print_list()

    # 删除节点
    ll.delete_node(3)
    print("删除节点3后的链表：")
    ll.print_list()

    ll.delete_node(2)
    print("删除节点2后的链表：")
    ll.print_list()

    ll.reverse_linked_list()
    print("链表翻转")
    ll.print_list()

    print("是否有环")
    print(ll.has_cycle())
