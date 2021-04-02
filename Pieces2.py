class Figure:
    def __repr__(self):
        return " "

    def get_moves(self, board, x, y):
        return []

    def __init__(self):
        self.empty = True
        self.value = 0


class King(Figure):
    def __repr__(self):
        return "K" if self.white else "k"

    def get_moves(self, board, x, y):
        moves = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 == dy:
                    continue

                if not (0 <= x + dx < 8 and 0 <= y + dy < 8):
                    continue

                if board[y + dy][x + dx].empty or board[y + dy][x + dx].white != self.white:
                    moves.append((x + dx, y + dy))

        return moves

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white
        self.value = 0


class Queen(Figure):
    def __repr__(self):
        return "Q" if self.white else "q"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white
        self.value = 9

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)):
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


class Knight(Figure):
    def __repr__(self):
        return "N" if self.white else "n"

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]:
            if not (0 <= x + dx < 8 and 0 <= y + dy < 8):
                continue

            if board[y + dy][x + dx].empty or board[y + dy][x + dx].white != self.white:
                moves.append((x + dx, y + dy))

        return moves

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white
        self.value = 3


class Bishop(Figure):
    def __repr__(self):
        return "B" if self.white else "b"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white
        self.value = 3

    def get_moves(self, board, x, y):
        moves = []

        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
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
            home = 6
            direction = -1
            if y==3 and x<7 and type(board[x+1][2])==Pawn and board[x+1][2]!=self.white:
                moves.append(x+1, 2)
            elif y==3 and x>0 and type(board[x-1][2])==Pawn and board[x-1][2]!=self.white:
                moves.append(x-1,2)
        else:
            home = 1
            direction = 1
            if y==4 and x<7 and type(board[x+1][5])==Pawn and board[x+1][5]!=self.white:
                moves.append(x+1, 5)
            elif y==3 and x>0 and type(board[x-1][5])==Pawn and board[x-1][5]!=self.white:
                moves.append(x-1,5)


        if board[y + direction][x].empty:
            moves.append((x, y + direction))

            if y == home and board[y + (2 * direction)][x].empty:
                moves.append((x, y + 2 * direction))

        for i in (1, -1):
            if 0 <= (x + i) < 8:
                if not board[y + direction][x + i].empty and board[y + direction][x + i].white != self.white:
                    moves.append((i + x, y + direction))

        return moves

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white
        self.value = 1


class Rook(Figure):
    def __repr__(self):
        return "R" if self.white else "r"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white
        self.value = 5

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
