import random
import math


class Network:
    def __init__(self, resource):
        nodes = {int(k): v for k, v in resource['nodes'].items()}
        self.nodes = nodes

        links = {int(k): v for k, v in resource['links'].items()}
        for link in links:
            links[link]['costs'] = {
                int(links[link]['start']): (links[link]['attributes']['length']
                                            / links[link]['attributes']['speeds'][str(links[link]['start'])])
            }
            if not links[link]['attributes']['isOneWay']:
                links[link]['costs'][int(links[link]['end'])] = links[link]['attributes']['length'] \
                                                                / links[link]['attributes']['speeds'][
                                                                    str(links[link]['end'])]
            links[link]['opposite'] = {
                links[link]['start']: links[link]['end'],
                links[link]['end']: links[link]['start']
            }
        self.links = links
        # self.turn_matrix = turn_matrix

    # TODO: Account for no path
    def find_path(self, origin_node, destination_node):
        # Dijkstra's
        queue = {
            origin_node: {
                'complete': True,
                'cost': 0,
                'from': [origin_node]
            }
        }
        for link in self.nodes[origin_node]['outbound']:
            destination = self.links[link]['opposite'][origin_node]
            queue[destination] = {
                'complete': False,
                'cost': self.links[link]['costs'][origin_node],
                'from': [origin_node]
            }
        for node in self.nodes:
            if node not in queue:
                queue[node] = {
                    'complete': False,
                    'cost': math.inf,
                    'from': [origin_node]
                }
        try:
            while not queue[destination_node]['complete']:
                cheapest_node = None
                lowest_cost = math.inf
                for node in queue:
                    if not queue[node]['complete'] \
                            and queue[node]['cost'] < lowest_cost:
                        cheapest_node = node
                        lowest_cost = queue[node]['cost']
                current_node = cheapest_node
                queue[current_node]['complete'] = True
                for link in self.nodes[current_node]['outbound']:
                    new_cost = queue[current_node]['cost'] + self.links[link]['costs'][current_node]
                    if not queue[self.links[link]['opposite'][current_node]]['complete'] \
                            and queue[self.links[link]['opposite'][current_node]]['cost'] >= new_cost:
                        if queue[self.links[link]['opposite'][current_node]]['cost'] == new_cost:
                            queue[self.links[link]['opposite'][current_node]]['from'].append(current_node)
                        else:
                            queue[self.links[link]['opposite'][current_node]]['from'] = [current_node]
                            queue[self.links[link]['opposite'][current_node]]['cost'] = new_cost
            # cost = queue[destination_node]['cost']
            path = [destination_node]
            while path[0] != origin_node:
                path.insert(0, random.choice(queue[path[0]]['from']))
            return path
        except Exception as e:
            print(e)
            return None
