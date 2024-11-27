from enum import Enum
from node import Node


class Destinations(Enum):
    ENTRANCE = "ENTRANCE"
    DESK_A = "DESK A"


nodes = []


def init_paths():

    a = Node(Destinations.DESK_A.value, 130, 140)
    b = Node('B', 350, 140)
    c = Node(Destinations.ENTRANCE.value, 640, 140)
    d = Node('D', 350, 370)
    e = Node('E', 550, 370)

    add_edges(a, [b])
    add_edges(b, [a, c, d])
    add_edges(c, [b])
    add_edges(d, [b, e])
    add_edges(e, [d])

    nodes.append(a)
    nodes.append(b)
    nodes.append(c)
    nodes.append(d)
    nodes.append(e)


def add_edges(node, neighbors):
    for neighbor in neighbors:
        node.add_edge(neighbor)

def get_path(source, destination):
    return [nodes[2], nodes[1], nodes[3], nodes[4]]

def draw(surface):
    for node in nodes:
        node.draw(surface)

