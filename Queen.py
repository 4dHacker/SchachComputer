from Board import Figure


class Queen(Figure):
    def __repr__(self):
        return "Q" if self.white else "q"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (-1, 0)):
            pos_x, pos_y = x, y
            pos_x += dx
            pos_y += dy
            while 0 <= pos_x < 8 and 0 <= pos_y < 8 and (board[pos_y][pos_x].empty):
                moves.append((pos_x, pos_y))
                pos_x += dx
                pos_y += dy
            if (board[pos_y][pos_x].white != self.white):
                moves.append((pos_x, pos_y))
        return moves
