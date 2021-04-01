from Board import Figure
class Pawn(Figure):
    def __repr__(self):
        return "P" if self.white else "p"

    def __init__(self, white):
        Figure.__init__(self)

        self.empty = False
        self.white = white

    def get_moves(self, board, x, y):
        moves=[]
        if board[y+1,x]==0:
            moves.append(x,y+1)

        if y==1 and board[y+2,x].empty:
            moves.append(x,y+2)

        if board[y+1,x+1].white != self.write:
            moves.append(x,y+2)
