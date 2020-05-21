import random


class Network:
    def __init__(self, links, outbound, inbound, turn_matrix):
        self.links = links
        self.outbound = outbound
        self.inbound = inbound
        self.turn_matrix = turn_matrix

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
