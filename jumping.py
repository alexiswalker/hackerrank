class Path:
    def __init__(self, path):
        self._path = path[::-1]
        self._actual_position = 0
        self._last_position = len(self._path) - 1

    def can_do_n_steps(self, n):
        next_position = self._actual_position + n
        return next_position <= self._last_position and self._path[next_position] == 0

    def do_n_steps(self, n):
        self._actual_position = self._actual_position + n
        return

    def am_i_in_last_position(self):
        return self._actual_position == self._last_position


def jumpingOnClouds(c):
    path = Path(c)
    jump = 0

    while not path.am_i_in_last_position():

        for n in [2, 1]:
            if path.can_do_n_steps(n):
                path.do_n_steps(n)
                jump = jump + 1
                break

    return jump


print jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
print jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0])
