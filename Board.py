class Figure:
    def __repr__(self):
        return " "

    def get_moves(self, board, x, y):
        return []

    def __init__(self):
        self.empty = True


# TODO
class Bishop(Figure):
    def __repr__(self):
        return "B" if self.white else "b"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white


# TODO
class Pawn(Figure):
    def __repr__(self):
        return "P" if self.white else "p"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white


# TODO
class Queen(Figure):
    def __repr__(self):
        return "Q" if self.white else "q"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white


# TODO
class Rook(Figure):
    def __repr__(self):
        return "R" if self.white else "r"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white


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


class Board:
    def setup(self, new_board):
        self.board = new_board

    def make_move(self, x, y, x2, y2):
        figure = self.board[y][x]

        if type(figure) == Pawn and ((y == 1 and figure.white) or (y == 6 and not figure.white)):
            self.board[y2][x2] = Queen(self.board[y][x].white)
            self.board[y][x] = Figure()
            return

        self.board[y2][x2] = self.board[y][x]
        self.board[y][x] = Figure()

    def get_possible_moves(self):
        moves = []

        for y in range(8):
            for x in range(8):
                moves += self.board[y][x].get_moves(board, x, y)

        return moves

    def __repr__(self):
        representation = []

        for row in self.board:
            representation.append(" ".join(map(repr, row)))

        return "\n".join(representation)

    def __init__(self):
        self.board = [
            [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False),
             Rook(False)],
            [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
            [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)]]


if __name__ == "__main__":
    board = Board()
    board.setup([[Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Pawn(False), Figure(), Figure(), Figure(), Figure(), Figure()],
                 [Figure(), Figure(), Figure(), Rook(True), Figure(), Figure(), Figure(), Figure()]])
    board.make_move(2, 6, 3, 7)
    print(board)
