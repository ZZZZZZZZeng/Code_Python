# 2022.03.31
class LNode:
    def __init__(self, data=None, next=None):
        # 结点初始化函数, p 即模拟所存放的下一个结点的地址
        # 为了方便传参, 设置 p 的默认值为 0
        self.data = data
        self.next = next


# 使用HashSet，判断一个链表是否有环，并找到入环的第一个节点
#  额外空间O(N)O
def hashGetLoopNode(head):
    if head is None or head.next is None:
        print("No Loop")
        exit(0)
    cur = head.next
    nodes = set()
    while cur and cur not in nodes:
        nodes.add(cur)
        cur = cur.next
    if cur is None:
        print("No Loop")
        exit(0)
    else:
        return cur


# 快慢指针获取入环首节点
# 额外空间O(1)
def getLoopNode(head):
    if head is None or head.next is None or head.next.next is None:
        print("No Loop")
        exit(0)
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next is None or fast.next.next is None:
            print("No Loop")
            exit(0)
        slow = slow.next
        fast = fast.next.next
    # 将快指针重置为链表头
    fast = head
    # 然后一起走，当他们相遇的时候就是LOOP节点
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


# 如果两个链表相交，求相交的节点
def getIntersectNode(head1, head2):
    if head1 is None or head2 is None or head1.next is None or head2.next is None:
        print("No Intersection")
        exit(0)
    n = 0
    cur1 = head1.next
    cur2 = head2.next
    while cur1 is not None:
        n += 1
        cur1 = cur1.next
    while cur2 is not None:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        print("No Intersection")
        exit(0)
    # 这里将长的那根链表给cur1
    cur1 = head1 if n > 0 else head2
    # 这里将短的那根链表给cur2
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)
    while n:
        cur1 = cur1.next
        n -= 1
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


# 两个有环链表，判断是否有公共环，并返回链表相交第一个节点
# loop1为第一个链表入环的首节点，loop2是第二个的
def bothLoopNode(head1, loop1, head2, loop2):
    if head1 is None or head1.next is None or head2 is None or head2.next is None:
        print("No Intersection")
        exit(0)
    # 有公共环，查找相交节点，类似于getIntersectNode
    if loop1 == loop2:
        n = 0
        cur1 = head1.next
        cur2 = head2.next
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next
        # 这里将长的那根链表给cur1
        cur1 = head1 if n > 0 else head2
        # 这里将短的那根链表给cur2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        while n:
            cur1 = cur1.next
            n -= 1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        print("No Intersection")
        exit(0)


if __name__ == "__main__":
    node0 = LNode()
    node00 = LNode()
    node1 = LNode(1)
    node2 = LNode(2)
    node3 = LNode(3)
    node4 = LNode(4)
    node5 = LNode(5)
    node6 = LNode(6)
    node7 = LNode(7)
    node8 = LNode(8)
    node0.next = node1
    node00.next = node7
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node4
    node7.next = node8
    node8.next = node3
    Node = bothLoopNode(node0, getLoopNode(node0), node00, getLoopNode(node00))

    print(Node.data)
