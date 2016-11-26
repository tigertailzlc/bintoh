# tigertailzlc November 2016 
# Usage: $ python bintoh.py <number of discs> 

class Game: 
    """A game/tutorial of Tower of Hanoi.""" 
    left = [] 
    center = [] 
    right = [] 
    pegs = [left, center, right] 
    discs = 0  
    currdisc = 0
    currbits = [] 
    terminated = False 

    def __init__(self, numdiscs):
        self.discs = numdiscs

    def createBits(self): 
        """Turn the decimal nbr discs into an array of bits.""" 

    def bitsToState(self): 
        """Take the current bit array and translate to corresponding game state.""" 

    def render(self): 
        """Print current turn nbr/total turns req'd & a repr. of curr game state"""  

    def playOneTurn(self): 
        """Check if terminated, set up bit array, set game state, render, update"""  





if __name__ == "__main__": 
    import sys 
    numdiscs = (int(sys.argv[1])) 
    game = Game(numdiscs)

    #If interactive: Render initial game state (0 moves in)! 

    #For i in range(numdiscs), run game.playOneTurn() 
    #Or better (pretty sure), while game.terminated==False, run game.playOneTurn() 

    #Then print "The End!" and exit. Or maybe make that part of render fn.  

    

#Extensions 
#Add functionality allowing user to step through the game via RETURN key 
#use argparse? https://docs.python.org/3/howto/argparse.html#id1 
#This would replace the for/while loop you have now 
#You'd just have to change verification (game.terminated==) step into "if" stmt 
#And if you can do this, you can probably allow user to start new game with n discs 
#in the same session by typing an integer instead of RETURN 
#Remember to free() the old game :P or del it or wtv you do in Python 
#And if you do that then you have to make an exit() command, too. 
