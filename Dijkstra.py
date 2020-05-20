import numpy as np
import random
from classes import Network

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
    # TODO: Network.find_path(origin_node, destination_node)
    origin_node = 1
    destination_node = 7
    # Dijkstra
    queue = [network.inbound[destination_node]]
    finished = False
    step = 0
    while not finished:
        block = []
        for destination in queue[step]:
            if destination in network.outbound[origin_node]:
                finished = True
                print('Finished on link %i' % destination)
            else:
                for origin in network.links:
                    if network.turn_matrix[network.links[origin]][network.links[destination]] \
                            and origin not in block \
                            and origin not in queue[step]:
                        block.append(origin)
        if not finished:
            queue.append(block)
            step += 1
    print('Queue:', queue)
    starts = [destination for destination in queue[step] if destination in network.outbound[origin_node]]
    path = [random.choice(starts)]
    while step > 0:
        step -= 1
        origin = path[-1]
        block = []
        for destination in queue[step]:
            if network.turn_matrix[network.links[origin]][network.links[destination]]:
                block.append(destination)
        path.append(random.choice(block))
    print('Path:', path)
