from Board2 import Board
from convert import to_text, to_coordinates
from random import randint


def next_move():
    move = board.minimax(3, True)
    # moves = board.get_filter_moves()
    # move = moves[randint(0, len(moves) - 1)]
    board.make_move(*move)
    return f"move {to_text(*move)}"


try:
    board = Board()
    should_play = True
    while True:
        s = input()
        command = s.split()[0]
        if command == 'xboard':
            print()
        elif command == 'new':
            board = Board()
            print('Gutes Spiel')
        elif command == 'protover':
            print('feature usermove=1 done=1')
        elif command == 'usermove':
            move = s.split()[1]
            board.make_move(*to_coordinates(move))
            if should_play:
                print(next_move())
        elif command == 'go':
            should_play = True
            print(next_move())

        elif command == 'force':
            should_play = False

except Exception as e:
    print(e)
    print(board)
