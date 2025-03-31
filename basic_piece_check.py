import src 
chess=src.chess.chess()
print("Pieces movements test")
print("Loading position: rnbqkbnr/pppppppp/8/8/8/8/P7/RNBQKBNR w KQkq - 0 1 ")
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/P7/RNBQKBNR w KQkq - 0 1")
if (board == -1):
    print("Loading position failed")

print("Generating Moves!")
PseudoLegalMove = src.PseudolegalMoves.PseudoLegalMoves()
generated_moves = [
        PseudoLegalMove._knight('b1', board), 
        PseudoLegalMove._bishop('c1', board), 
        PseudoLegalMove._queen('d1', board), 
        PseudoLegalMove._king('e1', board), 
        PseudoLegalMove._rook('a1', board), 
        PseudoLegalMove._pawn('a2', board), 
        ]
print("Checking Moves!")

correct_moves = [
        [40,42, 51],
        [40,49,51,44,37,30,23],
        [50,41,32,51,43,35,27,19,11,52,45,38,31],
        [51,52,53],
        [],
        [40,32],
        ]

for i in range(6):
    if (type(correct_moves[i]) != int):
        if (set(correct_moves[i]) == set(generated_moves[i])):
            pass 
        else:
            print(f"Test failed at i={i}" )
            print(f"Expected {correct_moves[i]} but got {generated_moves[i]}")
    else:
        if (correct_moves[i] == generated_moves[i]):
            pass
        else:
            print(f"Test failed at i={i}" )
            print(f"Expected {correct_moves[i]} but got {generated_moves[i]}")
