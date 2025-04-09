import Chess
chess = Chess.Chess()

kasparov_v_veselin = moves = [
    ("e4", "d6"),
    ("d4", "Nf6"),
    ("Nc3", "g6"),
    ("Be3", "Bg7"),
    ("Qd2", "O-O"),
    ("Bh6", "Bxh6"),
    ("Qxh6", "Nbd7"),
    ("O-O-O", "e5"),
    ("a3", "a6"),
    ("Bh8", "Kxh8"),
    ("Qxh6", "e4"),
    ("Qh3", "d5"),
    ("Bf4+", "Nh5"),
    ("Be5", "d4"),
    ("Bxd4", "exd4"),
    ("Qxd4+", "f6"),
    ("Qxd5+", "Kg7"),
    ("Qxa5", "b6"),
    ("Qxc3+", "Qf6"),
    ("Qa1+", "Kf7"),
    ("Qd2", "Qb2+"),
    ("Kd1", "Kxf6"),
    ("Qc4+", "Ke1"),
    ("Qa4+", "Kd1"),
    ("f5", "Qc1"),
    ("Qd2", "Qa7")
]

board = chess.Board()
a = 0 
for i,j in enumerate(kasparov_v_veselin):
    if (a%2 == 0 ):
        board.Move(str(j[0])) 
        a+=1 
    else:
        print(board.Move(str(j[1])))
        a+=1

print(board())