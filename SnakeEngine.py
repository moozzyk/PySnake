class SnakeEngine:
    def __init__(self, arena=None, width=None, height=None):
        if arena:
            self._arena = arena
        else:
            # validate x, y
            self._arena = [[' ' for _ in range(width)] for _ in range(height)]

    @property
    def arena_width(self):
        return len(self._arena[0])

    @property
    def arena_height(self):
        return len(self._arena)

    def get_field(self, row, col):
        # validate x, y
        return self._arena[row][col]
