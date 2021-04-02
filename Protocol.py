from Board2 import Board
board=Board()
should_play=False
while True:
    s=input()
    command =s.split()[0]
    if command=='xboard':
        print()
    elif command=='new':
        board=Board()
        print('Gutes Spiel')
    elif command=='protover':
        print('feature usermove=1 done=1')
    elif command=='usermove':
        move=s.split()[1]       #Move ausführen
        if should_play:
            pass                #Move ausgeben
    elif command=='go':
        should_play=True        #Move ausgeben
    elif command=='force':
        should_play=False