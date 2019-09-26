>On your journey across the cyberspace you come across a legendary gamemaster. In order to prove yourself and get the flag beat >him in his ancient game.
>
>The program old_game.py is running at:
>
>nc ecsc18.hack.cert.pl 10021

We are presented a game of rock-paper-scissors (RPS), in which we have to win 50 times, and after that guess a "random" number from one to million. Brute-forcing it would take ages, so we're not even going to try that.

The flag is used to generate a seed for pseudo random number generator, but it's hashed with CRC32 function, and modified with bitwise AND operation with number 0xffff. That means we won't get the flag from reversing the CRC32 function, but it leaves us with "only" 65536 possibilities for "magic number". 

First, we need to win RPS tournament. After every loss we have to reconnect to the server. Each time we make a move, no matter if a winning one, we are given our opponents move. That allows us to use its countermove during next connection. Getting whole sequence requires 50 connections. 

Having the sequence figured out, we could use it to guess the seed that was used for generating them. Checking those 65536 possibilities would take at most a few seconds.
Here comes the major problem I encountered - none of the possibilities worked. That's because all the time I was using Python 3.7, whereas the program is running using Python 2.x (Mind the hint in the filename!). Turns out, versions 2.x and 3.x have incompatible random number generators.

After switching to its predecesor, Python has shown me only one possibility of a seed number. 
I used it to generate the whole sequence again, and finally, 51st number - the answer to gamemasters question, which rewarded me with a flag:

>ecsc{I_am_the_4th_grade_champion_of_rock_paper_scissors}
