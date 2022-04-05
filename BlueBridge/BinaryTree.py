class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 递归先序遍历
def preOrderTraversal(root):
    if root is None:
        return
    print(root.data, end="\t\t")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


# 递归中序遍历
def inOrderTraversal(root):
    if root is None:
        return
    preOrderTraversal(root.left)
    print(root.data, end="\t\t")
    preOrderTraversal(root.right)


# 递归后序遍历
def postOrderTraversal(root):
    if root is None:
        return
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    print(root.data, end="\t\t")


# 非递归先序遍历
def preOrderDisplay(root):
    if root is None:
        return
    stack = [root]
    while len(stack):
        node = stack.pop()
        print(node.data, end="\t\t")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# 非递归中序遍历
def inOrderDisplay(root):
    if root is None:
        return
    stack = []
    while len(stack) or root:  # 有区别的地方
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.data)
            root = root.right


# 非递归后序遍历
# 头先出栈s1，入栈s2
# 然后左右的遍历二叉树,左边入栈s1，右边入栈s1
# 这时s1顺序出栈，则满足右边先入栈s2，左边在入栈s2
# 最终实现头右左压入栈s2，s2输出则是逆序左右头
def postOrderDisplay(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1):  # 有区别的地方
        root = stack1.pop()
        stack2.append(root)
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)


# 获取二叉树的宽度
def getTreeWidth(root):
    if root is None:
        return 0
    queue = [root]
    levelMap = {root: 1}
    currentLevel = 1  # 初始化所在层数，也代表每次迭代的层数
    currentLevelNodes = 0  # 某层最大的节点数
    maxNodes = 0
    while queue:
        cur = queue.pop()
        curNodeLevel = levelMap.get(cur)
        if curNodeLevel == currentLevel:
            currentLevelNodes += 1
        else:
            maxNodes = max(maxNodes, currentLevelNodes)
            currentLevelNodes = 1
            currentLevel += 1
        if cur.left:
            # 队列的形式进入队列
            levelMap[cur.left] = curNodeLevel + 1
            queue.insert(0, cur.left)
        if cur.right:
            # 队列的形式进入队列
            levelMap[cur.right] = curNodeLevel + 1
            queue.insert(0, cur.right)
    return maxNodes


if __name__ == "__main__":
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)
    node8 = BinaryTreeNode(8)
    node9 = BinaryTreeNode(9)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node7
    node7.left = node9
    node3.right = node8

    print(getTreeWidth(node1))
