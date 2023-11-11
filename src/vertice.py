
class Vertice:
    def __init__(self, grid_pos, affinity, previous_point=None, next_point=None):
        self.next_point = next_point
        self.previous_point = previous_point
        self.grid_pos = grid_pos
        self.affinity = affinity
