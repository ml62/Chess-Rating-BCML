import chess.pgn
import subprocess, time

multipv = 5
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

engine = subprocess.Popen(
	'stockfish-x64.exe',
	universal_newlines=True,
	stdin=subprocess.PIPE,
	stdout=subprocess.PIPE,
)

def put(command):
	engine.stdin.write(command+"\n")

def get():
	engine.stdin.write('isready\n')
	while True:
		text=engine.stdout.readline().strip()
		if text == 'readyok':
			break
		if text != "":
			print('\t' + text)

def run_game(moves):
	for i in range(len(moves)):		
		get()
		put('uci')
		get()
		put('setoption name multipv value ' + multipv)
		get()
		put('ucinewgame')
		get()
		put('position startpos moves' + moves[0:i].join(" "))
		get()
		put('go infinite')
		time.sleep(3)
		get()
		put('stop')
