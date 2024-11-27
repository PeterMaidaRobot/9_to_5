from node import Node


class Paths:

    def __init__(self):
        self.nodes = []

        a = Node('A', 130, 140)
        b = Node('B', 350, 140)
        c = Node('C', 640, 140)
        d = Node('D', 350, 370)
        e = Node('E', 550, 370)

        self.add_edges(a, [b])
        self.add_edges(b, [a, c, d])
        self.add_edges(c, [b])
        self.add_edges(d, [b, e])
        self.add_edges(e, [d])

        self.nodes.append(a)
        self.nodes.append(b)
        self.nodes.append(c)
        self.nodes.append(d)
        self.nodes.append(e)

    def add_edges(self, node, neighbors):
        for neighbor in neighbors:
            node.add_edge(neighbor)

    def draw(self, surface):
        for node in self.nodes:
            node.draw(surface)

