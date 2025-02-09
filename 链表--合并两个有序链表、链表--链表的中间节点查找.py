from _7_LinkedList import Node as Node
from _7_LinkedList import LinkedList as LinkedList

# 3. 合并两个有序链表
# 将两个有序链表合并为一个新的有序链表。可以使用迭代法实现。
def merge_two_lists(list1, list2):
    dummy = LinkedList()  
    current = dummy.head = Node(0) # 创建一个虚拟头节点
    
    head1,head2 = list1.head,list2.head
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    current.next = head1 if head1 else head2  # 连接剩余部分
    dummy.head = dummy.head.next
    return dummy
# 4. 查找链表的中间节点
# 使用快慢指针法，快指针每次移动两步，慢指针每次移动一步。当快指针到达链表末尾时，慢指针指向中间节点。
def find_middle_node(list):
    slow = list.head
    fast = list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # 返回中间节点
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(5)
ll.append(7)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
ll2.append(8)

ll3=merge_two_lists(ll,ll2)
ll3.print_list()

node = find_middle_node(ll3)
print("3中间节点:")
print(node.data)
