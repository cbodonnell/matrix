class Network:
    def __init__(self, links, outbound, inbound, turn_matrix):
        self.links = links
        self.outbound = outbound
        self.inbound = inbound
        self.turn_matrix = turn_matrix
