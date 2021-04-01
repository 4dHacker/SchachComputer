class Bishop:
    def __repr__(self):
        return "B" if self.white else "b"
    def __init__(self):
        self.white

    def get_moves(self,board,x,y):
        moves=[]
        pos_x,pos_y=x,y

        for dx, dy in ((1,1),(1,-1),(-1,1),(-1,-1)):

            while board[pos_x,pos_y]==0 and pos_x<8 and pos_y<8:
                pos_x+=dx
                pos_y+=dy
                moves.append((pos_x, pos_y))

            del moves[-1]



