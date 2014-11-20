__author__ = 'Pat McClernan'
#used for testing of RPS player
import PatAndDansPlayer

player = PatAndDansPlayer.PatDansPlayer()


past_moves = [1,2,1,1,1,1,]

move = player.play(past_moves)


print(move)

#past_moves = [0,0,1,1]

#move = player.play(past_moves)
#print(past_moves)
#print(move)