# tigertailzlc November 2016 
# Usage: $ python bintoh.py <number of discs> 

class Game: 
    """A game/tutorial of Tower of Hanoi.""" 

    def __init__(self, numdiscs):
        self.Verbose = False # for debugging purposes

        self.terminated = False 
        self.discs = numdiscs
        self.currmove = 0
        self.lastmove = 2**numdiscs
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
            print("currbits = " + str(self.currbits)) 

    def bitsToState(self): 
        """Take the current bit array and translate to corresponding game state.

        This function implements the rules of the simulation, which are the following:
        - The game begins with peg configuration O-M-D (origin-middle-destination). 
        - We say that a 1-bit is even if its index is even, and odd otherwise. 
        - Every even 1-bit sets a Dest and sets an Origin to its LEFT.    
        - Every odd 1-bit sets a Dest and sets an Origin to its RIGHT. 
        - 0-bits do not update the peg configuration. 
        - If we are stacking discs represented by 1-bits onto the Dest peg, 
          the position of the first disc represented by a 0-bit is determined 
          by the following pattern: DOMOM..OM. Similarly, stacking 0-bit discs 
          onto Origin or Middle pegs follows patterns OMDMD..MD and MODOD..OD 
          respectively. A string of equal-valued bits represents a stack of 
          consecutive discs on the same peg. 
        - If currbits[0]==1, the largest disc is placed on the Right peg.  
        """ 

        # Clear pegs from last call # 
        # Note: In an attempt to remain version-agnostic (between Python 2/3), 
        # I am using del s[:] instead of s.clear(), which is new to v3.3.  
        del self.left[:]
        del self.center[:]
        del self.right[:]

        # Initialize state according to first bit # 
        if (self.currbits[0]==1): 
            destin = 2 
            origin = 1 
            middle = 0 
            anchor = origin 
        else: 
            origin = 0
            middle = 1
            destin = 2
            anchor = origin 
        
        i = 0 
        # i is your current disc index. discs-i for intuition/rendering purposes. 

        while (i<self.discs): 
            # Setting down 0-bits # 
            j = 0
            while (i<self.discs and self.currbits[i]==0): 
                self.pegs[anchor].append(self.discs-i)
                i += 1
                j += 1

            # About to set down a leading 1-bit, so update configs, in partic. dest # 
            if ((j%2)==1):
                if (anchor==origin): 
                   destin = middle 
                else: 
                   destin = origin 

            if ((i%2)==0):
                # We have an even 1-bit; set origin to LEFT of dest #     
                origin = (destin-1)%3
                middle = (destin+1)%3
            else:
                # We have an odd 1-bit; set origin to RIGHT of dest #       
                origin = (destin+1)%3
                middle = (destin-1)%3

            # Now setting down 1-bits # 
            j = 0
            while (i<self.discs and self.currbits[i]==1):
                self.pegs[destin].append(self.discs-i)
                i += 1
                j += 1

            if ((j%2)==0): 
                anchor = middle 
            else: 
                anchor = origin 


    def render(self): 
        """Print current turn nbr/total turns req'd & a repr. of curr game state."""  
        # This is not the actual final render function. #  
        print("Current move: " + str(self.currmove+1) +"/"+ str(self.lastmove)) 
        print("Left   = " + str(self.left))
        print("Center = " + str(self.center))
        print("Right  = " + str(self.right))

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
            if (self.currmove==self.lastmove): 
                self.terminated = True  
        else: 
            print("The game is over! It took " + str(self.currmove) + " moves. ") 




if __name__ == "__main__": 
    import sys 
    numdiscs = (int(sys.argv[1])) 
    game = Game(numdiscs)

    game.Verbose = True 

    if (numdiscs==0 or numdiscs>100): 
        # This upper bound is pretty arbitrary. # 
        print("Please choose a number in [1,100].") 
    else: 
        while (game.terminated==False): 
            game.playOneTurn()
        print("The game is over. It took " + str(game.currmove) + " moves. ") 

    #If interactive: Immediately render initial game state (0 moves in)! 

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
#And if you do that then you have to make a quit command, too. 
