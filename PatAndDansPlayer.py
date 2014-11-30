__author__ = 'Pat McClernan and Dan Wegmann'

#will soon implement frameworks player class
#this class is the adaptor from the underlying
#playing logic to the framework

import my_rps_player
from game_framework import Player
from game_framework import Message


class PatDansPlayer(Player.Player):


    def __init__(self):
        name = "Pat and Dan"

        my_player = my_rps_player()


    def get_name(self):
        return self.name

    def set_name(self, playername):
        name = playername

    def play(self, past_moves):
        return self.my_player.my_rps_play(past_moves)


        #return  my_player.my_rps_play(self, past_moves = past_moves)


   Tournament_Start = 1
    Tournament_End = 2
    Match_Start = 3
    Match_End = 4
    Round_Start = 5
    Round_End = 6

    def notify(self, msg):
        my_player = self.my_player
        #on new round start, erase previous moves
        if msg[0] == 3:
            my_player.reset_moves()
        elif msg[0] == 6:
            my_player.add_moves(msg[1])
        else:
            print "unknown message"
