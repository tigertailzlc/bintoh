# tigertailzlc November 2016 
# Usage: $ python bintoh.py <number of discs> 

class Game: 
    """A game/tutorial of Tower of Hanoi.""" 

    def __init__(self, numdiscs):
        self.Verbose = False # for testing/debugging purposes

        self.terminated = False 
        self.discs = numdiscs
        self.currmove = 0
        self.currbits = [] 
        
        self.left = [] 
        self.center = [] 
        self.right = [] 
        self.pegs = [self.left, self.center, self.right] 

    def createBits(self): 
        """Turn the decimal number currmove into an array of bits.

        The array is stored as currbits[], which has length = discs. 
        The largest disc is represented by currbits[0].   
        """ 
        self.currbits = [] 
        binmove = bin(self.currmove)         # binary repr:  bin(-37) --> '-0b100101'
        binmove = binmove.lstrip('-0b')      # remove leading zeros and minus sign 
        ldzeros = self.discs-len(binmove)    # number of leading zeros 
        for i in range(self.discs): 
            if (i<ldzeros): 
                self.currbits.append(0) 
            else: 
                self.currbits.append(int(binmove[i-ldzeros])) 

        if (self.Verbose): 
            print("currbits = " + str(self.currbits) + " currmove = " + str(self.currmove)) 

    def bitsToState(self): 
        """Take the current bit array and translate to corresponding game state.""" 
        pass

    def render(self): 
        """Print current turn nbr/total turns req'd & a repr. of curr game state."""  
        pass

    def playOneTurn(self): 
        """Check if terminated, set up bit array, set game state, render, update.

        NOTE: The termination checking here is currently redundant. 
        I am keeping it because I think it will be better for stepthrough mode 
        to check here instead of in the main function. 
        """  
        if (self.terminated==False): 
            self.createBits()
            self.bitsToState()
            self.render()
            self.currmove += 1 
            if (self.currmove==2**self.discs): 
                self.terminated = True  
        else: 
            print("The game is over! It took " + str(self.currmove) + " moves. ") 




if __name__ == "__main__": 
    import sys 
    numdiscs = (int(sys.argv[1])) 
    game = Game(numdiscs)

    game.Verbose = True 
    print("Discs = " + str(game.discs))

    while (game.terminated==False): 
        game.playOneTurn()
    print("The game is over. It took " + str(game.currmove) + " moves. ") 

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
