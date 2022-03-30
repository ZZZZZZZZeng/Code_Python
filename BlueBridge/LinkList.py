# 2022.3.30
class LNode:
    def __init__(self, data, next=None):
        # 结点初始化函数, p 即模拟所存放的下一个结点的地址
        # 为了方便传参, 设置 p 的默认值为 0
        self.data = data
        self.next = next


class LinkList:
    def __init__(self, data=None):
        self.head = None

    # 链表初始化函数，方法类似于尾插法
    def initList(self, data=None):
        # 初始化链表，头结点不存储数据
        self.head = LNode(None)
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        if data:
            for i in data:
                node = LNode(i)
                p.next = node
                p = p.next

    # 判断链表是否为空
    def isEmpty(self):
        if self.head is None or self.head.next is None:
            print("Empty List!")
            return 1
        else:
            return 0

    # 取链表长度
    def getLength(self):
        if self.isEmpty():
            return 0
        p = self.head
        length = 0
        while p.next:
            length += 1
            p = p.next
        return length

    # 遍历链表
    def travelList(self):
        if self.isEmpty():
            exit(0)
        print('link list traveling result: ')
        p = self.head.next
        while p:
            print(p.data, end="\t\t")
            p = p.next
        print()

    # 查询某一位置链表数据
    def searchElem(self, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("Key Error! Program Exit.")
            exit(0)
        p = self.head
        while index >= 0:
            p = p.next
            index -= 1
        print(p.data)

    # 链表插入数据
    def insertElem(self, value, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("Key Error! Program Exit.")
            exit(0)
        p = self.head
        pre = None
        i = 0
        while i <= index:
            pre = p
            p = p.next
            i += 1
        # 遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = LNode(value)
        pre.next = node
        node.next = p

    # 链表删除数据
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("Key Error! Program Exit.")
            exit(0)
        # 链表头结点不计入
        i = -1
        p = self.head
        # 遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                if i == index:
                    pre.next = p.next
                    p = None
                    return 1
        # p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("a")
    l = LinkList()
    print(l)
    l.initList(data)
    print(l.getLength())
    l.travelList()
    l.insertElem(666, 3)
    l.travelList()
    l.deleteElem(3)
    l.travelList()
    l.searchElem(4)
