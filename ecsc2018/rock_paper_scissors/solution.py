#!/usr/bin/env python

import socket
import select
import random 

winning_moves = []
orig_moves = []
moves = ['O', '__', '8<']

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
	"__" : "8<",
	"8<" : "O",
	"O" : "__"
	}
	return win_moves[move]

def next_move(iter):
	if (len(winning_moves) > iter):
		return winning_moves[iter] + '\n'
	else:
		return moves[random.randint(0,2)] + '\n'

resp = ''
max_iter = 0;
while (len(winning_moves) <= 50):
	iter = 0
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('ecsc18.hack.cert.pl', 10021))
	read_response(sock)	#welcome message

	for i in range (0, max_iter+1):
		sock.send(str.encode(next_move(iter)))
		resp = read_response(sock)
		
		if(resp.find('cheated') != -1):
			sock.send(str.encode('313487\n'))
			resp = read_response(sock)
			#print(resp)
			break

		substr = resp.find('My move:')
		if (substr >= 0):
			iter = iter + 1
			if (resp[substr+9] == 'O'):
				move = resp[substr+9]
			else:
				move = resp[substr+9:substr+11]

			if (iter > max_iter): #unikalny iterator
				print('iteration #' + str(iter))
				print('move = ' + move)
				max_iter = iter
				winning_moves.append(winning_move(move))
				orig_moves.append(move)
		else:
			break
	sock.close()

	if (len(winning_moves) == 50):
		break


print(resp)
print('winning moves:')
print(winning_moves)
print('original moves: ')
print(orig_moves)

moves_int = []

for i in orig_moves:
	moves_int.append(moves.index(i))
print(moves_int)

seeds = {}
for s in range(0,65536):
	random.seed(s)
	ctr = 0
	for i in moves_int:
		move = random.randint(0, 2)
		if (i != move):
			break
		ctr += 1
		if (ctr == 50):
			print('suspected seed: ' + str(s))
			seeds[str(s)] = str(random.randint(0, 10**6))
			print('Random number: ' + seeds[str(s)])

for seed_key in seeds.keys():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('ecsc18.hack.cert.pl', 10021))
	print(read_response(sock))	#welcome message

	for i in winning_moves:
		sock.send(str.encode(i + '\n'))
		resp = read_response(sock)
		print(resp)

		if(resp.find('cheated') != -1):
			print('magic num: ' + str(seeds[seed_key]))
			sock.send(str.encode(str(seeds[seed_key]) + '\n'))
			resp = read_response(sock)
			print(resp)
			break
	sock.close()


print('done')
