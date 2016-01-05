class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if (val < node.v):
            if (node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if (node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def lca(self, r, n1, n2):
        if r is None:
            return None
        if n1 < r.v and n2 < r.v:
            return self.lca(r.l, n1, n2)
        if n1 > r.v and n2 > r.v:
            return self.lca(r.r, n1, n2)
        return r.v
        ''' for calling method of class use self !!!!!!!!!!!!!!!!!!'''


def main():
    tree = Tree()
    x = [20, 8, 22, 4, 12, 10, 14]
    for i in x:
        tree.add(i)
    n1 = input("enter n1")
    n2 = input("enter n2")

    print tree.lca(tree.getRoot(), n1, n2)
    # print "the lca of " + str(n1) + " and " + str(n2) + " is " + tree.lca(tree.getRoot(), n1, n2)


if __name__ == "__main__":
    main()
