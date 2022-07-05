import matplotlib.pyplot as plt
from geometry import Rectangle as Rt, Polyline


def m_plot(rct: Rt, crc=(0, 0, 0)):
    if rct.p1.x < rct.p2.x and rct.p1.y > rct.p2.y:
        r_startpoint = (rct.p1.x, rct.p2.y)
    elif rct.p1.x > rct.p2.x and rct.p1.y < rct.p2.y:
        r_startpoint = (rct.p2.x, rct.p1.y)
    elif rct.p1.x > rct.p2.x and rct.p1.y > rct.p2.y:
        r_startpoint = (rct.p2.x, rct.p2.y)
    else:
        r_startpoint = (rct.p1.x, rct.p1.y)

    max_ax = max(abs(rct.p1.x), abs(rct.p1.y), abs(rct.p2.x), abs(rct.p2.y)) + 10
    plt.axis([-max_ax, max_ax, -max_ax, max_ax])
    plt.axis("equal")

    x, y = [0, 0], [-max_ax, max_ax]

    plt.plot(x, y, c='black', linestyle='dotted', linewidth='1')
    plt.plot(y, x, c='black', linestyle='dotted', linewidth='1')

    d1 = plt.Rectangle(r_startpoint, rct.metrics()[0], rct.metrics()[1], fill=False, edgecolor='black')
    m1 = plt.Circle((rct.p1.x, rct.p1.y), radius=.2, color='red', label=f'P1: {rct.p1.x},{rct.p1.y}')
    m2 = plt.Circle((rct.p2.x, rct.p2.y), radius=.2, color='blue', label=f'P2: {rct.p2.x},{rct.p2.y}')
    if crc[-1] > .1:
        c1 = plt.Circle((crc[0], crc[1]), radius=crc[-1], fill=True, color='green',
                        label=f'C1: {crc[0]}, {crc[1]}, {crc[2]}')
    elif crc[-1] == 0:
        c1 = plt.Circle((crc[0], crc[1]), radius=0)
    else:
        c1 = plt.Circle((crc[0], crc[1]), radius=crc[-1], color='green', label=f'P3: {crc[0]}, {crc[1]}')

    plt.gca().add_artist(d1)
    plt.gca().add_artist(m1)
    plt.gca().add_artist(m2)
    plt.gca().add_artist(c1)
    plt.legend()
    plt.show()


def p_poly(points: Polyline):
    x, y, mx = [], [], []
    for obj in points.pts:
        x.append(obj.x)
        y.append(obj.y)
        mx.append(abs(obj.x))
        mx.append(abs(obj.y))

    n_max = max(mx) + 10
    plt.axis([-n_max, n_max, -n_max, n_max])
    plt.axis("equal")
    ox, oy = [0, 0], [-n_max, n_max]
    plt.plot(ox, oy, c='black', linestyle='dotted', linewidth='1')
    plt.plot(oy, ox, c='black', linestyle='dotted', linewidth='1')

    plt.plot(x, y, marker='o')
    # for i, j in zip(x, y):
    #     plt.text(i + .5, j + .5, f'{i}, {j}', color='red')
    plt.show()
