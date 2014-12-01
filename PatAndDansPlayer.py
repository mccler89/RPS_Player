

__author__ = 'Pat McClernan and Dan Wegmann'

#will soon implement frameworks player class
#this class is the adaptor from the underlying
#playing logic to the framework

from my_rps_player import my_rps_player
import Player
from Message import Message

class PatDansPlayer(Player.Player):


    def __init__(self):
        # Call super class constructor
        Player.Player.__init__(self)
        self.name = "Pat and Dan"
        self.my_player = my_rps_player()
        self.reset()

    def reset(self):
        self.my_player.reset_moves()

    def get_name(self):
        return self.name

    def set_name(self, playername):
        name = playername

    def play(self):
        return self.my_player.my_rps_play()

    def notify(self, msg):
        if msg.is_match_start_message():
            self.my_player.reset_moves()
        elif msg.is_round_end_message():
            players = msg.get_players()
            if (players[0] == self) or (players[1] == self):
                moves, result = msg.get_info()
                self.my_player.add_moves(moves)
