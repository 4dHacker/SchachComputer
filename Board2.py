from Pieces2 import *

SHOW_MATERIAL = True


class Board:
    def copy(self):
        new_board = [row.copy() for row in self.board]
        board = Board()
        board.setup(new_board, self.whites_turn)

        return board

    def perft(self, depth):
        if depth == 0:
            return 1

        n = 0

        for move in self.get_possible_moves(self.whites_turn):
            new_board = self.copy()
            new_board.make_move(*move)
            n += new_board.perft(depth - 1)

        return n

    def material(self):
        white = 0
        black = 0

        for y in range(8):
            for x in range(8):
                if self.board[y][x].empty:
                    continue

                if self.board[y][x].white:
                    white += self.board[y][x].value

                else:
                    black += self.board[y][x].value

        return white, black

    def setup(self, new_board, whites_turn):
        self.board = new_board
        self.whites_turn = whites_turn

    def make_move(self, x, y, x2, y2):
        figure = self.board[y][x]

        if type(figure) == King and y == y2 and abs(x2 - x) == 2:
            if x2 < x:
                assert type(self.board[y][0]) == Rook

                self.board[y][3] = self.board[y][0]
                self.board[y][0] = Figure()

            else:
                assert type(self.board[y][7]) == Rook

                self.board[y][5] = self.board[y][7]
                self.board[y][7] = Figure()

        if type(figure) == Pawn and ((y == 1 and figure.white) or (y == 6 and not figure.white)):
            self.board[y2][x2] = Queen(self.board[y][x].white)
            self.board[y][x] = Figure()
            return

        self.board[y2][x2] = self.board[y][x]
        self.board[y][x] = Figure()

        self.whites_turn = not self.whites_turn

    def get_possible_moves(self, white):
        moves = []

        for y in range(8):
            for x in range(8):
                if self.board[y][x].empty or self.board[y][x].white != white:
                    continue

                for new_x, new_y in self.board[y][x].get_moves(self.board, x, y):
                    moves.append((x, y, new_x, new_y))

        return moves

    def __repr__(self):
        representation = []

        for row in self.board:
            representation.append(" ".join(map(repr, row)))

        if SHOW_MATERIAL:
            white, black = self.material()
            representation[4] += "   " + (" " if white - black < 0 else "+") + str(white - black)

        return "\n".join(representation)

    def __init__(self):
        self.board = [
            [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)],
            [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure(), Figure()],
            [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
            [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)]]
        self.whites_turn = True


if __name__ == "__main__":
    board = Board()

    print(board.perft(5))

    while True:
        eval(input(">>> "))
