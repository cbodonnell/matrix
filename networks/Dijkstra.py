import numpy as np
from networks.models import Network

links = {
    100: 0,
    200: 1,
    300: 2,
    400: 3,
    500: 4,
    600: 5,
    700: 6,
    800: 7,
}


# Node dictionary with 'outbound' links
outbound = {
    1: [100, 300],
    2: [100, 200],
    3: [200, 500],
    4: [600],
    5: [400, 600, 700],
    6: [700, 800],
    7: []
}


# Node dictionary with 'inbound' links
inbound = {
    1: [100],
    2: [100, 200, 400],
    3: [200],
    4: [300, 600],
    5: [600, 700],
    6: [500, 700],
    7: [800]
}


# x - origin, y - destination
turn_matrix = np.array(
    [
        [False, True, True, False, False, False, False, False],
        [True, False, False, False, True, False, False, False],
        [False, False, False, False, False, True, False, False],
        [True, True, False, False, False, False, False, False],
        [False, False, False, False, False, False, True, True],
        [False, False, False, True, False, False, True, False],
        [False, False, False, True, False, False, False, True],
        [False, False, False, False, False, False, False, False]
    ]
)


if __name__ == '__main__':
    # TODO: Network builder
    network = Network(links, outbound, inbound, turn_matrix)
    path = network.find_path(1, 7)
    print(path)
