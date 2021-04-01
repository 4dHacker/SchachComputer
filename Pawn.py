class Pawn:
    def __repr__(self):
        return "P" if self.white else "p"
    def __init__(self):
        self.white

    def get_moves(self, board, x, y):
        moves=[]
        if board[x,y+1]==0:
            moves.append(x,y+1)

        if y==