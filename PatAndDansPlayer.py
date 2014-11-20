__author__ = 'Pat McClernan and Dan Wegmann'

#will soon implement frameworks player class
#this class is the adaptor from the underlying
#playing logic to the framework

from my_rps_player import my_rps_player


class PatDansPlayer:#(Player):

    #previous_moves = [1, 0, 2, 1]


    def play(self, past_moves):
        print(past_moves)

        return  my_rps_player.my_rps_play(self, past_moves = past_moves)