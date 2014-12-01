from game_framework import PatAndDansPlayer

__author__ = 'Pat McClernan'
#used for testing of RPS player

player = PatAndDansPlayer.PatDansPlayer()


past_moves = [1,2,1,1,1,1,]

move = player.play(past_moves)


print(move)

#past_moves = [0,0,1,1]

#move = player.play(past_moves)
#print(past_moves)
#print(move)