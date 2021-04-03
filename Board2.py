from Pieces2 import *
import time

SHOW_MATERIAL = True


class Board:
    def copy(self):
        new_board = [row.copy() for row in self.board]
        board = Board(False)
        board.left_down_moved = self.left_down_moved
        board.right_down_moved = self.right_down_moved
        board.left_up_moved = self.left_up_moved
        board.right_up_moved = self.right_up_moved
        board.black_king_moved = self.black_king_moved
        board.white_king_moved = self.white_king_moved
        board.setup(new_board, self.whites_turn, False)

        return board

    def minimax(self, depth, origin):
        if depth == 0:
            a, b = self.material()
            return b - a

        evaluation = []

        for move in self.possible_moves:
            new_board = self.copy()
            new_board.make_move(*move)

            if new_board.check_king(not new_board.whites_turn):
                continue

            evaluation.append((new_board.minimax(depth - 1, False), move))

        if len(evaluation) == 0:
            if self.check_king(self.whites_turn):
                return 1000 if self.whites_turn else -1000

            else:
                return 0

        if self.whites_turn:
            return min(evaluation, key=lambda a: a[0])[origin]

        return max(evaluation, key=lambda a: a[0])[origin]

    def perft(self, depth):
        if depth == 0:
            return 1

        n = 0

        for move in self.possible_moves:
            new_board = self.copy()
            new_board.make_move(*move)

            if new_board.check_king(not new_board.whites_turn):
                continue

            n += new_board.perft(depth - 1)

        return n

    def get_filter_moves(self):
        l = []

        for move in self.possible_moves:
            new_board = self.copy()
            new_board.make_move(*move)

            if new_board.check_king(not new_board.whites_turn):
                continue

            if type(self.board[move[1]][move[0]]) == Pawn and (move[3] == 7 or move[3] == 0):
                l.append((move[0], move[1], move[2], move[3], "q"))

            else:
                l.append(move)

        return l

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

    def setup(self, new_board, whites_turn, with_possible_moves=True):
        self.board = new_board
        self.whites_turn = whites_turn

        if with_possible_moves:
            self.possible_moves = self.get_possible_moves(self.whites_turn)

    def make_move(self, x, y, x2, y2, promotion=""):
        figure = self.board[y][x]
        if x == 0 and y == 0:
            self.left_up_moved = True
        elif x == 0 and y == 7:
            self.left_down_moved = True
        elif x == 7 and y == 0:
            self.right_up_moved = True
        elif x == 7 and y == 7:
            self.right_down_moved = True
        elif x == 4 and y == 7:
            self.white_king_moved = True
        elif x == 4 and y == 0:
            self.black_king_moved = True

        if type(figure) == Pawn and abs(y2 - y) == 2:
            self.passent_possible = x

        else:
            self.passent_possible = -1

        if type(figure) == Pawn and abs(x - x2) == 1 and self.board[y2][x2].empty:
            self.board[y][x2] = Figure()

        if type(figure) == King and y == y2 and abs(x2 - x) >= 2:
            if x2 < x:
                assert type(self.board[y][0]) == Rook

                self.board[y][3] = self.board[y][0]
                self.board[y][0] = Figure()

            else:
                assert type(self.board[y][7]) == Rook

                self.board[y][5] = self.board[y][7]
                self.board[y][7] = Figure()

        if type(figure) == Pawn and ((y == 1 and figure.white) or (y == 6 and not figure.white)) and promotion == "":
            self.board[y2][x2] = Queen(self.board[y][x].white)
            self.board[y][x] = Figure()

        elif promotion != "":
            self.board[y2][x2] = {"q": Queen, "n": Knight, "r": Rook, "b": Bishop}[promotion](self.board[y][x].white)

        else:
            self.board[y2][x2] = self.board[y][x]

        self.board[y][x] = Figure()

        self.whites_turn = not self.whites_turn
        self.possible_moves = self.get_possible_moves(self.whites_turn)

    def get_possible_moves(self, white, ignore_castling=False):
        moves = []

        for y in range(8):
            for x in range(8):
                if self.board[y][x].empty or self.board[y][x].white != white:
                    continue

                for new_x, new_y in self.board[y][x].get_moves(self.board, x, y):
                    if self.board[new_y][new_x].empty and type(self.board[y][x]) == Pawn and abs(x - new_x) == 1:
                        if self.passent_possible != new_x:
                            continue

                    if type(self.board[y][x]) == King and abs(new_x - x) >= 2:
                        if ignore_castling:
                            continue

                        if y == 7:
                            if new_x < x:
                                if self.white_king_moved or self.left_down_moved:
                                    continue

                                if self.check(x, y) or self.check(x - 1, y) or self.check(x - 2, y):
                                    continue

                            else:
                                if self.white_king_moved or self.right_down_moved:
                                    continue

                                if self.check(x, y) or self.check(x + 1, y) or self.check(x + 2, y):
                                    continue

                        else:
                            if new_x < x:
                                if self.black_king_moved or self.left_up_moved:
                                    continue

                                if self.check(x, y) or self.check(x - 1, y) or self.check(x - 2, y):
                                    continue

                            else:
                                if self.black_king_moved or self.right_up_moved:
                                    continue

                                if self.check(x, y) or self.check(x + 1, y) or self.check(x + 2, y):
                                    continue

                    moves.append((x, y, new_x, new_y))

        return moves

    def check_king(self, white):
        stop = False

        for x in range(8):
            for y in range(8):
                if type(self.board[y][x]) == King and self.board[y][x].white == white:
                    stop = True
                    break

            if stop:
                break

        positions = [move[2:] for move in self.possible_moves]

        if (x, y) in positions:
            return True

        return False

    def check(self, x, y):
        newPos = [item[2:] for item in self.get_possible_moves(not self.whites_turn, True)]
        if (x, y) in newPos:
            return True
        else:
            return False

    def __repr__(self):
        representation = []

        for row in self.board:
            representation.append(" ".join(map(repr, row)))

        if SHOW_MATERIAL:
            white, black = self.material()
            representation[4] += "   " + (" " if white - black < 0 else "+") + str(white - black)

        return "\n".join(representation)

    def __init__(self, generation=True):
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
        self.passent_possible = -1

        self.left_down_moved = False
        self.right_down_moved = False
        self.left_up_moved = False
        self.right_up_moved = False
        self.black_king_moved = False
        self.white_king_moved = False

        if generation:
            self.possible_moves = self.get_possible_moves(True)

        else:
            self.possible_moves = []


if __name__ == "__main__":
    board = Board()

    while True:
        eval(input(">>> "))
