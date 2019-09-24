#!/usr/bin/env python

import socket
import select
import random 

winning_moves = []
orig_moves = []
moves = ['8<', 'O', '__']

def read_response(sock):
	ready = select.select([sock], [], [], 0.05)
	response = ''
	while(ready[0]):
		data = sock.recv(4096)
		if(len(data) > 0):
			response += str(data);
			ready = select.select([sock], [], [], 0.05)
		else:
			break
	return response

def winning_move(move):
	win_moves = {
	"_" : "8<",
	"8" : "O",
	"O" : "__"
	}
	return win_moves[move]

def next_move(iter):
	if (len(winning_moves) > iter):
		return winning_moves[iter] + '\n'
	else:
		return moves[random.randint(0,2)] + '\n'


max_iter = 0;
while (len(winning_moves) <= 50):
	iter = 0
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('ecsc18.hack.cert.pl', 10021))
	read_response(sock)	#welcome message

	for i in range (0, max_iter+1):
		sock.send(str.encode(next_move(iter)))
		resp = read_response(sock)
		print(resp)
		
		if(resp.find('cheated') != -1):
			print('found!')
			sock.send(str.encode('313487\n'))
			resp2 = read_response(sock)
			print(resp2)
			break

		substr = resp.find('My move:')
		if (substr >= 0):
			iter = iter + 1
			move = resp[substr+9]
			print('move = ' + move)
			if (iter > max_iter): #unikalny iterator
				max_iter = iter
				winning_moves.append(winning_move(move))
				orig_moves.append(move)
		else:
			break
	sock.close()

	if (len(winning_moves) == 50):
		break

print('win_moves')
print(winning_moves)
print('orig_moves')
print(orig_moves)


sock.close()
print('done')

