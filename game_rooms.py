class Rooms:
    def __init__(self, row=2, col=0):
        self.row = row
        self.col = col
        self.house = [['wall', 'Балкон', 'wall'],
                      ['Спальня', 'Холл', 'Кухня'],
                      ['Подземелье', 'Коридор', 'Оружейная']]

    def get_way(self, side, nsteps):

        max_row = len(self.house) - 1
        max_col = len(self.house[0]) - 1

        if side == 0:  # Север
            new_row = max(0, self.row - nsteps)
            stop = min(self.row - 0 + 1, nsteps + 1)
            way = [self.house[self.row - i][self.col] for i in range(1, stop)]
            self.row = new_row

        if side == 1:  # Восток
            new_col = min(2, self.col + nsteps)
            stop = min(max_col - self.col + 1, 1 + nsteps)
            way = [self.house[self.row][self.col + i] for i in range(1, stop)]
            if stop-1 < nsteps: way.append('wall')
            self.col = new_col

        if side == 2:  # Юг
            new_row = min(2, self.row + nsteps)
            stop = min(max_row - self.row + 1, 1 + nsteps)
            way = [self.house[self.row + i][self.col] for i in range(1, stop)]
            if stop - 1 < nsteps: way.append('wall')
            self.row = new_row

        if side == 3:  # Запад
            new_col = max(0, self.col - nsteps)
            stop = min(self.col - 0 + 1, 1 + nsteps)
            way = [self.house[self.row][self.col - i] for i in range(1, stop)]
            if stop - 1 < nsteps: way.append('wall')
            self.col = new_col

        if (self.row == 0) and (self.col == 0):
            self.row = 1
        if (self.row == 0) and (self.col == 2):
            self.row = 1
        return way
