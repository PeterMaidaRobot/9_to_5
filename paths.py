from enum import Enum
from node import Node


class Destinations(Enum):
    ENTRANCE = "ENTRANCE"
    SECRETARY = "SECRETARY"
    LARGE_CONF = "LARGE CONF"
    SMALL_CONF = "SMALL CONF"
    JUNCTION_1 = "JUNCTION_1"
    JUNCTION_2 = "JUNCTION_2"
    JUNCTION_3 = "JUNCTION_3"
    JUNCTION_4 = "JUNCTION_4"
    JUNCTION_5 = "JUNCTION_5"
    JUNCTION_6 = "JUNCTION_6"
    JUNCTION_7 = "JUNCTION_7"
    JUNCTION_8 = "JUNCTION_8"
    JUNCTION_9 = "JUNCTION_9"
    JUNCTION_10 = "JUNCTION_10"
    JUNCTION_11 = "JUNCTION_11"
    JUNCTION_12 = "JUNCTION_12"
    DESK_A = "DESK A"
    DESK_B = "DESK B"
    DESK_C = "DESK C"
    DESK_D = "DESK D"
    DESK_E = "DESK E"
    DESK_F = "DESK F"
    DESK_G = "DESK G"
    DESK_H = "DESK H"
    DESK_I = "DESK I"
    DESK_J = "DESK J"
    DESK_K = "DESK K"
    DESK_L = "DESK L"
    DESK_M = "DESK M"
    DESK_N = "DESK N"
    DESK_O = "DESK O"
    DESK_P = "DESK P"
    DESK_Q = "DESK Q"
    DESK_R = "DESK R"
    DESK_S = "DESK S"
    DESK_T = "DESK T"
    DESK_U = "DESK U"
    DESK_V = "DESK V"
    DESK_W = "DESK W"
    DESK_X = "DESK X"
    DESK_Y = "DESK Y"
    DESK_Z = "DESK Z"
    DESK_AA = "DESK AA"
    DESK_BB = "DESK BB"
    DESK_CC = "DESK CC"
    DESK_DD = "DESK DD"
    HALL_A = "HALL A"
    HALL_B = "HALL B"
    HALL_C = "HALL C"
    HALL_D = "HALL D"
    HALL_E = "HALL E"
    HALL_F = "HALL F"
    HALL_G = "HALL G"
    HALL_H = "HALL H"
    HALL_I = "HALL I"
    HALL_J = "HALL J"
    HALL_K = "HALL K"
    HALL_L = "HALL L"
    HALL_M = "HALL M"
    HALL_N = "HALL N"
    HALL_O = "HALL O"
    HALL_P = "HALL P"
    HALL_Q = "HALL Q"
    HALL_R = "HALL R"
    HALL_S = "HALL S"
    HALL_T = "HALL T"
    HALL_U = "HALL U"
    HALL_V = "HALL V"
    HALL_W = "HALL W"
    HALL_X = "HALL X"
    HALL_Y = "HALL Y"
    HALL_Z = "HALL Z"
    HALL_AA = "HALL AA"
    HALL_BB = "HALL BB"
    HALL_CC = "HALL CC"
    HALL_DD = "HALL DD"


nodes = []
DESK_TO_HALL_DIST = 45
HALL_TO_HALL_DIST = 55
JUNCTION_WIDTH_DIST = 210

def init_paths():

    # First two columns (halls and desks)
    junction_1 = Node(Destinations.JUNCTION_1.value,
                      130,
                      140)
    hall_a = Node(Destinations.HALL_A.value,
                  junction_1.x,
                  junction_1.y + HALL_TO_HALL_DIST)
    desk_a = Node(Destinations.DESK_A.value,
                  hall_a.x + DESK_TO_HALL_DIST,
                  hall_a.y)
    hall_b = Node(Destinations.HALL_B.value,
                  hall_a.x,
                  hall_a.y + HALL_TO_HALL_DIST)
    desk_b = Node(Destinations.DESK_B.value,
                  hall_b.x + DESK_TO_HALL_DIST,
                  hall_b.y)
    hall_c = Node(Destinations.HALL_C.value,
                  hall_b.x,
                  hall_b.y + HALL_TO_HALL_DIST)
    desk_c = Node(Destinations.DESK_C.value,
                  hall_c.x + DESK_TO_HALL_DIST,
                  hall_c.y)

    junction_2 = Node(Destinations.JUNCTION_2.value,
                      hall_c.x,
                      hall_c.y + HALL_TO_HALL_DIST)
    hall_d = Node(Destinations.HALL_D.value,
                  junction_2.x,
                  junction_2.y + HALL_TO_HALL_DIST)
    desk_d = Node(Destinations.DESK_D.value,
                  hall_d.x + DESK_TO_HALL_DIST,
                  hall_d.y)
    hall_e = Node(Destinations.HALL_E.value,
                  hall_d.x,
                  hall_d.y + HALL_TO_HALL_DIST)
    desk_e = Node(Destinations.DESK_E.value,
                  hall_e.x + DESK_TO_HALL_DIST,
                  hall_e.y)
    hall_f = Node(Destinations.HALL_F.value,
                  hall_e.x,
                  hall_e.y + HALL_TO_HALL_DIST)
    desk_f = Node(Destinations.DESK_F.value,
                  hall_f.x + DESK_TO_HALL_DIST,
                  hall_f.y)
    junction_3 = Node(Destinations.JUNCTION_3.value,
                      hall_f.x,
                      hall_f.y + HALL_TO_HALL_DIST)


    # Second two columns (halls and desks)
    junction_4 = Node(Destinations.JUNCTION_4.value,
                      junction_1.x + JUNCTION_WIDTH_DIST,
                      junction_1.y)
    hall_g = Node(Destinations.HALL_G.value,
                  junction_4.x,
                  junction_4.y + HALL_TO_HALL_DIST)
    desk_g = Node(Destinations.DESK_G.value,
                  hall_g.x - DESK_TO_HALL_DIST,
                  hall_g.y)
    hall_h = Node(Destinations.HALL_H.value,
                  hall_g.x,
                  hall_g.y + HALL_TO_HALL_DIST)
    desk_h = Node(Destinations.DESK_H.value,
                  hall_h.x - DESK_TO_HALL_DIST,
                  hall_h.y)
    hall_i = Node(Destinations.HALL_I.value,
                  hall_h.x,
                  hall_h.y + HALL_TO_HALL_DIST)
    desk_i = Node(Destinations.DESK_I.value,
                  hall_i.x - DESK_TO_HALL_DIST,
                  hall_i.y)

    junction_5 = Node(Destinations.JUNCTION_5.value,
                      hall_i.x,
                      hall_i.y + HALL_TO_HALL_DIST)
    hall_j = Node(Destinations.HALL_J.value,
                  junction_5.x,
                  junction_5.y + HALL_TO_HALL_DIST)
    desk_j = Node(Destinations.DESK_J.value,
                  hall_j.x - DESK_TO_HALL_DIST,
                  hall_j.y)
    desk_m = Node(Destinations.DESK_M.value,
                  hall_j.x + DESK_TO_HALL_DIST,
                  hall_j.y)
    hall_k = Node(Destinations.HALL_K.value,
                  hall_j.x,
                  hall_j.y + HALL_TO_HALL_DIST)
    desk_k = Node(Destinations.DESK_K.value,
                  hall_k.x - DESK_TO_HALL_DIST,
                  hall_k.y)
    desk_n = Node(Destinations.DESK_N.value,
                  hall_k.x + DESK_TO_HALL_DIST,
                  hall_k.y)
    hall_l = Node(Destinations.HALL_L.value,
                  hall_k.x,
                  hall_k.y + HALL_TO_HALL_DIST)
    desk_l = Node(Destinations.DESK_L.value,
                  hall_l.x - DESK_TO_HALL_DIST,
                  hall_l.y)
    desk_o = Node(Destinations.DESK_O.value,
                  hall_l.x + DESK_TO_HALL_DIST,
                  hall_l.y)
    junction_6 = Node(Destinations.JUNCTION_6.value,
                      hall_l.x,
                      hall_l.y + HALL_TO_HALL_DIST)

    junction_7 = Node(Destinations.JUNCTION_7.value,
                      junction_5.x + JUNCTION_WIDTH_DIST,
                      junction_5.y)
    hall_p = Node(Destinations.HALL_P.value,
                  junction_7.x,
                  junction_7.y + HALL_TO_HALL_DIST)
    desk_p = Node(Destinations.DESK_P.value,
                  hall_p.x - DESK_TO_HALL_DIST,
                  hall_p.y)
    desk_s = Node(Destinations.DESK_S.value,
                  hall_p.x + DESK_TO_HALL_DIST,
                  hall_p.y)
    hall_q = Node(Destinations.HALL_Q.value,
                  hall_p.x,
                  hall_p.y + HALL_TO_HALL_DIST)
    desk_q = Node(Destinations.DESK_Q.value,
                  hall_q.x - DESK_TO_HALL_DIST,
                  hall_q.y)
    desk_t = Node(Destinations.DESK_T.value,
                  hall_q.x + DESK_TO_HALL_DIST,
                  hall_q.y)
    hall_r = Node(Destinations.HALL_R.value,
                  hall_q.x,
                  hall_q.y + HALL_TO_HALL_DIST)
    desk_r = Node(Destinations.DESK_R.value,
                  hall_r.x - DESK_TO_HALL_DIST,
                  hall_r.y)
    desk_u = Node(Destinations.DESK_U.value,
                  hall_r.x + DESK_TO_HALL_DIST,
                  hall_r.y)
    junction_8 = Node(Destinations.JUNCTION_8.value,
                      hall_r.x,
                      hall_r.y + HALL_TO_HALL_DIST)

    junction_9 = Node(Destinations.JUNCTION_9.value,
                      junction_7.x + JUNCTION_WIDTH_DIST,
                      junction_7.y)
    hall_v = Node(Destinations.HALL_V.value,
                  junction_9.x,
                  junction_9.y + HALL_TO_HALL_DIST)
    desk_v = Node(Destinations.DESK_V.value,
                  hall_v.x - DESK_TO_HALL_DIST,
                  hall_v.y)
    desk_y = Node(Destinations.DESK_Y.value,
                  hall_v.x + DESK_TO_HALL_DIST,
                  hall_v.y)
    hall_w = Node(Destinations.HALL_W.value,
                  hall_v.x,
                  hall_v.y + HALL_TO_HALL_DIST)
    desk_w = Node(Destinations.DESK_W.value,
                  hall_w.x - DESK_TO_HALL_DIST,
                  hall_w.y)
    desk_z = Node(Destinations.DESK_Z.value,
                  hall_w.x + DESK_TO_HALL_DIST,
                  hall_w.y)
    hall_x = Node(Destinations.HALL_X.value,
                  hall_w.x,
                  hall_w.y + HALL_TO_HALL_DIST)
    desk_x = Node(Destinations.DESK_X.value,
                  hall_x.x - DESK_TO_HALL_DIST,
                  hall_x.y)
    desk_aa = Node(Destinations.DESK_AA.value,
                   hall_x.x + DESK_TO_HALL_DIST,
                   hall_x.y)
    junction_10 = Node(Destinations.JUNCTION_10.value,
                       hall_x.x,
                       hall_x.y + HALL_TO_HALL_DIST)

    junction_11 = Node(Destinations.JUNCTION_11.value,
                       junction_9.x + JUNCTION_WIDTH_DIST,
                       junction_9.y)
    hall_bb = Node(Destinations.HALL_BB.value,
                   junction_11.x,
                   junction_11.y + HALL_TO_HALL_DIST)
    desk_bb = Node(Destinations.DESK_BB.value,
                   hall_bb.x - DESK_TO_HALL_DIST,
                   hall_bb.y)
    hall_cc = Node(Destinations.HALL_CC.value,
                   hall_bb.x,
                   hall_bb.y + HALL_TO_HALL_DIST)
    desk_cc = Node(Destinations.DESK_CC.value,
                   hall_cc.x - DESK_TO_HALL_DIST,
                   hall_cc.y)
    hall_dd = Node(Destinations.HALL_DD.value,
                   hall_cc.x,
                   hall_cc.y + HALL_TO_HALL_DIST)
    desk_dd = Node(Destinations.DESK_DD.value,
                   hall_dd.x - DESK_TO_HALL_DIST,
                   hall_dd.y)
    junction_12 = Node(Destinations.JUNCTION_12.value,
                       hall_dd.x,
                       hall_dd.y + HALL_TO_HALL_DIST)


    # Misc
    entrance = Node(Destinations.ENTRANCE.value, 640, 140)

    add_edges(junction_1, [hall_a, junction_4])
    add_edges(hall_a, [junction_1, desk_a, hall_b])
    add_edges(desk_a, [hall_a])
    add_edges(hall_b, [desk_b, hall_a, hall_c])
    add_edges(desk_b, [hall_b])
    add_edges(hall_c, [desk_c, hall_b, junction_2])
    add_edges(desk_c, [hall_c])

    add_edges(junction_2, [hall_c, hall_d, junction_5])
    add_edges(hall_d, [junction_2, desk_d, hall_e])
    add_edges(desk_d, [hall_d])
    add_edges(hall_e, [desk_e, hall_d, hall_f])
    add_edges(desk_e, [hall_e])
    add_edges(hall_f, [desk_f, hall_e, junction_3])
    add_edges(desk_f, [hall_f])
    add_edges(junction_3, [hall_f, junction_6])

    add_edges(junction_4, [hall_g, junction_1, entrance])
    add_edges(hall_g, [junction_4, desk_g, hall_h])
    add_edges(desk_g, [hall_g])
    add_edges(hall_h, [desk_h, hall_g, hall_i])
    add_edges(desk_h, [hall_h])
    add_edges(hall_i, [desk_i, hall_h, junction_5])
    add_edges(desk_i, [hall_i])

    add_edges(junction_5, [hall_i, junction_2, hall_j, junction_7])
    add_edges(hall_j, [junction_5, desk_j, desk_m, hall_k])
    add_edges(desk_j, [hall_j])
    add_edges(desk_m, [hall_j])
    add_edges(hall_k, [desk_k, desk_n, hall_j, hall_l])
    add_edges(desk_k, [hall_k])
    add_edges(desk_n, [hall_k])
    add_edges(hall_l, [desk_l, desk_o, hall_k, junction_6])
    add_edges(desk_l, [hall_l])
    add_edges(desk_o, [hall_l])
    add_edges(junction_6, [hall_l, junction_3, junction_8])

    add_edges(junction_7, [junction_5, hall_p, junction_9])
    add_edges(hall_p, [junction_7, desk_p, desk_s, hall_q])
    add_edges(desk_p, [hall_p])
    add_edges(desk_s, [hall_p])
    add_edges(hall_q, [desk_q, desk_t, hall_p, hall_r])
    add_edges(desk_q, [hall_q])
    add_edges(desk_t, [hall_q])
    add_edges(hall_r, [desk_r, desk_u, hall_q, junction_8])
    add_edges(desk_r, [hall_r])
    add_edges(desk_u, [hall_r])
    add_edges(junction_8, [hall_r, junction_6, junction_10])

    add_edges(junction_9, [junction_7, hall_v, junction_11])
    add_edges(hall_v, [junction_9, desk_v, desk_y, hall_w])
    add_edges(desk_v, [hall_v])
    add_edges(desk_y, [hall_v])
    add_edges(hall_w, [desk_z, desk_w, hall_v, hall_x])
    add_edges(desk_w, [hall_w])
    add_edges(desk_z, [hall_w])
    add_edges(hall_x, [desk_x, desk_aa, hall_w, junction_10])
    add_edges(desk_x, [hall_x])
    add_edges(desk_aa, [hall_x])
    add_edges(junction_10, [hall_x, junction_8, junction_12])

    add_edges(junction_11, [junction_9, hall_bb])
    add_edges(hall_bb, [junction_11, desk_bb, hall_cc])
    add_edges(desk_bb, [hall_bb])
    add_edges(hall_cc, [desk_cc, hall_bb, hall_dd])
    add_edges(desk_cc, [hall_cc])
    add_edges(hall_dd, [desk_dd, hall_cc, junction_12])
    add_edges(desk_dd, [hall_dd])
    add_edges(junction_12, [hall_dd, junction_10])

    add_edges(entrance, [junction_4])


    nodes.append(junction_1)
    nodes.append(hall_a)
    nodes.append(desk_a)
    nodes.append(hall_b)
    nodes.append(desk_b)
    nodes.append(hall_c)
    nodes.append(desk_c)

    nodes.append(junction_2)
    nodes.append(hall_d)
    nodes.append(desk_d)
    nodes.append(hall_e)
    nodes.append(desk_e)
    nodes.append(hall_f)
    nodes.append(desk_f)
    nodes.append(junction_3)

    nodes.append(junction_4)
    nodes.append(hall_g)
    nodes.append(desk_g)
    nodes.append(hall_h)
    nodes.append(desk_h)
    nodes.append(hall_i)
    nodes.append(desk_i)

    nodes.append(junction_5)
    nodes.append(hall_j)
    nodes.append(desk_j)
    nodes.append(desk_m)
    nodes.append(hall_k)
    nodes.append(desk_k)
    nodes.append(desk_n)
    nodes.append(hall_l)
    nodes.append(desk_l)
    nodes.append(desk_o)
    nodes.append(junction_6)

    nodes.append(junction_7)
    nodes.append(hall_p)
    nodes.append(desk_p)
    nodes.append(desk_s)
    nodes.append(hall_q)
    nodes.append(desk_q)
    nodes.append(desk_t)
    nodes.append(hall_r)
    nodes.append(desk_r)
    nodes.append(desk_u)
    nodes.append(junction_8)

    nodes.append(junction_9)
    nodes.append(hall_v)
    nodes.append(desk_v)
    nodes.append(desk_y)
    nodes.append(hall_w)
    nodes.append(desk_w)
    nodes.append(desk_z)
    nodes.append(hall_x)
    nodes.append(desk_x)
    nodes.append(desk_aa)
    nodes.append(junction_10)

    nodes.append(junction_11)
    nodes.append(hall_bb)
    nodes.append(desk_bb)
    nodes.append(hall_cc)
    nodes.append(desk_cc)
    nodes.append(hall_dd)
    nodes.append(desk_dd)
    nodes.append(junction_12)

    nodes.append(entrance)

    verify_bidrectional_neigbors()
    generate_weights()


def verify_bidrectional_neigbors():
    for node in nodes:
        for neighbor1 in node.neighbors:
            if node not in neighbor1.neighbors:
                print(f"Node {node.name} missing in neighbors for {neighbor1.name}")


def generate_weights():
    # TODO... do I have to do Dijstka's for each node.... would take a long time.
    pass


def add_edges(node, neighbors):
    for neighbor in neighbors:
        node.add_edge(neighbor)


def get_path(source, destination):
    return [nodes[2], nodes[1], nodes[3], nodes[4]]


def draw(surface):
    for node in nodes:
        node.draw(surface)

