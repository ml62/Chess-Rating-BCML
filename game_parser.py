import chess.pgn


pgn = open("data.pgn")

def read_game(pgn):
	return chess.pgn.read_game(pgn)

game = read_game(pgn)

def game_in_uci(game):
	moves = []
	node = game
	while node.variations:
		node = node.variations[0]
		moves.append(node.move.uci())
	return moves