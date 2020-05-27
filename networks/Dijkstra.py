import numpy as np
from networks.models import Network
import random
import math
import time

links = {
    100: {
        'index': 0,
        'start': 1,
        'end': 2,
        'costs': {
            1: 10,
            2: 10
        },
        'opposite': {
            1: 2,
            2: 1
        }

    },
    200: {
        'index': 1,
        'start': 2,
        'end': 3,
        'costs': {
            2: 10,
            3: 10
        },
        'opposite': {
            2: 3,
            3: 2
        }
    },
    300: {
        'index': 2,
        'start': 1,
        'end': 4,
        'costs': {
            1: 5
        },
        'opposite': {
            1: 4,
            4: 1
        }
    },
    400: {
        'index': 3,
        'start': 5,
        'end': 2,
        'costs': {
            5: 5
        },
        'opposite': {
            5: 2,
            2: 5
        }
    },
    500: {
        'index': 4,
        'start': 3,
        'end': 6,
        'costs': {
            3: 10
        },
        'opposite': {
            3: 6,
            6: 3
        }
    },
    600: {
        'index': 5,
        'start': 4,
        'end': 5,
        'costs': {
            4: 10,
            5: 10
        },
        'opposite': {
            4: 5,
            5: 4
        }
    },
    700: {
        'index': 6,
        'start': 5,
        'end': 6,
        'costs': {
            5: 15,
            6: 10
        },
        'opposite': {
            5: 6,
            6: 5
        }
    },
    800: {
        'index': 7,
        'start': 6,
        'end': 7,
        'costs': {
            6: 20
        },
        'opposite': {
            6: 7,
            7: 6
        }
    }
}


# Node dictionary with 'inbound' links
# inbound = {
#     1: [100],
#     2: [100, 200, 400],
#     3: [200],
#     4: [300, 600],
#     5: [600, 700],
#     6: [500, 700],
#     7: [800]
# }
# outbound = {
#     1: [100, 300],
#     2: [100, 200],
#     3: [200, 500],
#     4: [600],
#     5: [400, 600, 700],
#     6: [700, 800],
#     7: []
# }
# Node dictionary
nodes = {
    1: {
        'inbound': [100],
        'outbound': [100, 300]
    },
    2: {
        'inbound': [100, 200, 400],
        'outbound': [100, 200]
    },
    3: {
        'inbound': [200],
        'outbound': [200, 500]
    },
    4: {
        'inbound': [300, 600],
        'outbound': [600]
    },
    5: {
        'inbound': [600, 700],
        'outbound': [400, 600, 700]
    },
    6: {
        'inbound': [500, 700],
        'outbound': [700, 800]
    },
    7: {
        'inbound': [800],
        'outbound': []
    },
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
    origin_node = 1
    destination_node = 7
    start_time = time.time()
    # Dijkstra
    queue = {
        origin_node: {
            'complete': True,
            'cost': 0,
            'from': [origin_node]
        }
    }
    for link in nodes[origin_node]['outbound']:
        destination = links[link]['opposite'][origin_node]
        queue[destination] = {
            'complete': False,
            'cost': links[link]['costs'][origin_node],
            'from': [origin_node]
        }
    for node in nodes:
        if node not in queue:
            queue[node] = {
                'complete': False,
                'cost': math.inf,
                'from': [origin_node]
            }
    current_node = origin_node
    current_link = None
    while not queue[destination_node]['complete']:
        cheapest_node = None
        lowest_cost = math.inf
        # next_moves = [(links[link]['opposite'][current_node], link) for link in nodes[current_node]['outbound']]
        for node in queue:
            if not queue[node]['complete'] \
                    and queue[node]['cost'] < lowest_cost:
                    cheapest_node = node
                    lowest_cost = queue[node]['cost']
        for link in nodes[current_node]['outbound']:
            if links[link]['opposite'][current_node] == cheapest_node:
                cheapest_link = link
        current_node = cheapest_node
        queue[current_node]['complete'] = True
        for link in nodes[current_node]['outbound']:
            new_cost = queue[current_node]['cost'] + links[link]['costs'][current_node]
            if not queue[links[link]['opposite'][current_node]]['complete'] \
                    and queue[links[link]['opposite'][current_node]]['cost'] >= new_cost:
                if queue[links[link]['opposite'][current_node]]['cost'] == new_cost:
                    queue[links[link]['opposite'][current_node]]['from'].append(current_node)
                else:
                    queue[links[link]['opposite'][current_node]]['from'] = [current_node]
                    queue[links[link]['opposite'][current_node]]['cost'] = new_cost
        # print(queue)
    cost = queue[destination_node]['cost']
    path = [destination_node]
    while path[0] != origin_node:
        path.insert(0, random.choice(queue[path[0]]['from']))
    time_elapsed = time.time() - start_time
    print('Path:', path)
    print('Cost:', cost)
    print('Time (s):', time_elapsed)



