class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def search(self, node, parent, data):
        if node is None:  # False表示未找到该节点
            return False, node, parent
        if node.data == data:  # True表示找到该节点
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print('无该关键字，删除失败！')
        else:
            if n.lchild is None:
                if n == p.lchild:  # n是父节点的左子节点
                    p.lchild = n.rchild
                else:  # n是父节点的右子节点
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # 左右子树均不为空
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p  # 删除next

    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)

    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data)


a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)
bst.inOrderTraverse(bst.root)
bst.delete(bst.root, 13)
bst.inOrderTraverse(bst.root)
