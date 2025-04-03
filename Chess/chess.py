def generatePseudoLegalMoves(self,board):
    from src.PseudolegalMoves import PseudoLegalMoves
    all_pseudo_moves    = {} 
    turn                = board[-1]
    PseudoLegal         = PseudoLegalMoves()
    for i,j in enumerate(board):
        if (j != self.EMPTY):
            if (turn == self.BLACK):
                if (j == self.BKNIGHT):
                    all_pseudo_moves.update({'black-knight': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.BKING):                     
                    all_pseudo_moves.update({'black-king': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.BROOK):
                    all_pseudo_moves.update({'black-rook': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.BBISHOP): 
                       all_pseudo_moves.update({'black-bishop': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.BPAWN): 
                    all_pseudo_moves.update({'black-pawn': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.BQUEEN):              
                    all_pseudo_moves.update({'black-queen': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
            else:
                if (j == self.WKNIGHT):                     
                    all_pseudo_moves.update({'white-knight': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.WKING):              
                    all_pseudo_moves.update({'white-king': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.WROOK):
                    all_pseudo_moves.update({'white-rook': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.WBISHOP): 
                    all_pseudo_moves.update({'white-bishop': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.WPAWN): 
                    all_pseudo_moves.update({'white-pawn': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
                if (j == self.WQUEEN):             
                    all_pseudo_moves.update({'white-queen': f'{PseudoLegal._knight(self.board_sqs[i], board)}'})
    return str(all_pseudo_moves)
