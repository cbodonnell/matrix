import numpy as np


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
    origin_node = 1
    destination_node = 6
    # Dijkstra
    queue = [inbound[destination_node]]
    finished = False
    step = 0
    while not finished:
        block = []
        for destination in queue[step]:
            if destination in outbound[origin_node]:
                finished = True
                print('Finished on link %i' % destination)
            else:
                for origin in links:
                    if turn_matrix[links[origin]][links[destination]] and origin not in block and origin not in queue[step]:
                        block.append(origin)
        if not finished:
            queue.append(block)
            step += 1

    print(queue)
    # [[800]]

    # [[800], [500, 700]]
    # ...
