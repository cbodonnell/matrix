import random


class Network:
    def __init__(self, links, inbound, outbound, turn_matrix):
        self.links = links
        self.inbound = inbound
        self.outbound = outbound
        self.turn_matrix = turn_matrix

    # TODO: Add in weight based on length/travel_time/"cost"
    def find_path(self, origin_node, destination_node):
        # Dijkstra
        queue = [self.inbound[destination_node]]
        finished = False
        step = 0
        while not finished:
            block = []
            for destination in queue[step]:
                if destination in self.outbound[origin_node]:
                    finished = True
                    # print('Finished on link %i' % destination)
                else:
                    for origin in self.links:
                        origin = int(origin)
                        if self.turn_matrix[self.links[origin]][self.links[destination]] \
                                and origin not in block \
                                and origin not in queue[step]:
                            block.append(origin)
            if not finished:
                queue.append(block)
                step += 1
        # print('Queue:', queue)
        starts = [destination for destination in queue[step] if destination in self.outbound[origin_node]]
        path = [random.choice(starts)]
        while step > 0:
            step -= 1
            origin = path[-1]
            block = []
            for destination in queue[step]:
                if self.turn_matrix[self.links[origin]][self.links[destination]]:
                    block.append(destination)
            path.append(random.choice(block))
        # print('Path:', path)
        return path
