"""
Бинарное дерево
граф - состоит из множества вершин и ребер применяется в соц сетях в фейсбук и т.д
сосдают для каждого человека граф его друзей, постов и т.д
различают full binyry tree как все вершины имеют по два (либо ноль)
исходящих ребра
и Complete Tree где какой то из уровней не имее у каждой вершины два ребенка
"""


class Vertex:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_vertex):
        self.root_vertex = root_vertex

    def pre_order(self, start, path):
        if start is not None:
            path += f'{start.data} ->'
            path = self.pre_order(start=start.left, path=path)
            if start is self.root_vertex:
                path += "\n"
            path = self.pre_order(start=start.right, path=path)
        return path

    def in_order_print(self, start):
        if start is None:
            return
        else:
            self.in_order_print(start=start.left)
            print(f"{start.data} ->")
            self.in_order_print(start=start.right)

    def post_order_print(self, start):
        if start is None:
            return
        else:
            self.in_order_print(start=start.left)
            self.in_order_print(start=start.right)
            print(f"{start.data} ->")


if __name__ == '__main__':
    tree = BinaryTree(root_vertex=Vertex("F"))
    tree.root_vertex.left = Vertex("B")
    tree.root_vertex.left.left = Vertex("A")
    tree.root_vertex.left.right = Vertex("D")
    tree.root_vertex.left.right.left = Vertex("C")
    tree.root_vertex.left.right.right = Vertex("E")
    tree.root_vertex.right = Vertex("G")
    tree.root_vertex.right.right = Vertex("I")
    tree.root_vertex.right.right.left = Vertex("H")
    print(tree.pre_order(start=tree.root_vertex, path=""))

