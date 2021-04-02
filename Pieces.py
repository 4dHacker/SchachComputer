class Figure:
    def __repr__(self):
        return " "

    def get_moves(self, board, x, y):
        return []

    def __init__(self):
        self.empty = True


class King(Figure):
    def __repr__(self):
        return "Q" if self.white else "q"

    def get_moves(self, board, x, y):
        moves = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 == dy:
                    continue

                if not (0 <= x + dx < 8 and 0 <= y + dy < 8):
                    continue

                if board[y + dy][x + dx].empty or board[y + dy][x + dx].white != self.white:
                    moves.append((dx, dy))

        return moves

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white


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
            if 0 <= pos_x < 8 and 0 <= pos_y < 8:
                if board[pos_y][pos_x].white != self.white:
                    moves.append((pos_x, pos_y))
        return moves


class Bishop(Figure):
    def __repr__(self):
        return "B" if self.white else "b"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            pos_x, pos_y = x, y
            pos_x += dx
            pos_y += dy
            while 0 <= pos_x < 8 and 0 <= pos_y < 8 and (board[pos_y][pos_x].empty):
                moves.append((pos_x, pos_y))
                pos_x += dx
                pos_y += dy
            if 0 <= pos_x < 8 and 0 <= pos_y < 8:
                if board[pos_y][pos_x].white != self.white:
                    moves.append((pos_x, pos_y))
        return moves


class Knight(Figure):
    def __repr__(self):
        return "N" if self.white else "n"

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]:
            if not (0 <= x + dx < 8 and 0 <= y + dy < 8):
                continue

            if board[y + dy][x + dx].empty or board[y + dy][x + dx].white != self.white:
                moves.append((dx, dy))

        return moves

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white


class Rook(Figure):
    def __repr__(self):
        return "R" if self.white else "r"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            pos_x, pos_y = x, y
            pos_x += dx
            pos_y += dy
            while 0 <= pos_x < 8 and 0 <= pos_y < 8 and board[pos_y][pos_x].empty:
                moves.append((pos_x, pos_y))
                pos_x += dx
                pos_y += dy
            if 0 <= pos_x < 8 and 0 <= pos_y < 8:
                if board[pos_y][pos_x].white != self.white:
                    moves.append((pos_x, pos_y))
        return moves



class Pawn(Figure):
    def __repr__(self):
        return "P" if self.white else "p"



    def get_moves(self, board, x, y):
        moves = []
        if self.white:
            home=6
            direction=-1
        else:
            home=6
            direction=-1
        if board[y + direction][x].empty:
            moves.append(x)
        if y == home and board[y + (2*direction)][x].empty:
            moves.append((x, y + 2*direction))

        for i in (1,-1):
            if 0<=(y + direction)<8 or 0<=(x+i)<8:
                pass

        return moves

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white

