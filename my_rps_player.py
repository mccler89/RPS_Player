__author__ = 'Pat McClernan and Dan Weggman'

#input
#0 for rock
#1 for paper
#2 for scissors
# past move is array of numbers
# our move followed by their move


#Our strategy is to look at all past moves
#In a large number of games, you would expect
#   each move to be seen an even amount of times
#So our strategy is to take the least seen move
#    and expect it to show up soon
#   so we will play to beat that move
class my_rps_player:

    def __init__(self):

        rock = 0
        paper = 0
        scissors = 0


    def my_rps_play(self):
        rock = self.rock
        paper = self.paper
        scissors = self.scissors

        #determine which move has been used least
        if (rock < paper) and (rock < scissors):
            move = 0
        elif paper < scissors:
            move = 1
        else: move = 2

        print(move)

        move = (move + 1 )% 3

        return move

    def add_moves(self, moves):
        for this_move in list(moves):
            if this_move == 0:
                self.rock += 1
            elif this_move == 1:
                self.paper += 1
            elif this_move == 2:
                self.scissors += 1

    def reset_moves(self):
        self.rock = 0
        self.paper = 0
        self.scissors = 0
