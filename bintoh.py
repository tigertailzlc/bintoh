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
        """Take the current bit array and translate to corresponding game state.

        The rules of the simulation are as follows, and this function implements 
        these rules. 
        - The game begins with peg configuration O-M-D (origin-middle-destination). 
        - We are in zeromode if we are currently reading 0 bits, and not o.w.. 
        - In zeromode, we have pattern 0MDMD..MD, where the first 1 to appear is 
          placed on the [M]iddle or [D]est peg according to its position. 
        - Otherwise, we have pattern 1OMOM..OM, where the first 0 to appear is 
          placed on the [O]rigin or [M]iddle peg according to its position. 
        - We say that a 1-bit is even if its index is even, and odd o.w..
        - Shifting in to zeromode does not reconfigure pegs; shifting out does.  
        - Every even 1-bit is a Dest and sets an Origin to its LEFT. 
        - Every odd 1-bit is a Dest and sets an Origin to its RIGHT. 
        - If currbits[0]==1, that disc is placed on the Right peg.  
        """ 

        # Clear pegs from last call # 
        # Note: In an attempt to remain version-agnostic (between Python 2/3), 
        # I am using del s[:] instead of s.clear(), which is new to v3.3.  
        del self.left[:]
        del self.center[:]
        del self.right[:]

        # Initialize state according to first bit # 
        if (self.currbits[0]==1): 
            zeromode = False 
            destin = self.pegs[2] 
            origin = self.pegs[1] 
            middle = self.pegs[0] 
        else: 
            zeromode = True 
            origin = self.pegs[0]
            middle = self.pegs[1]
            destin = self.pegs[2]
        

        i = 0 
        # i is your current disc index. discs-i for intuition/rendering purposes. 
        while (i<self.discs): 
            if (zeromode):
                # This block should only be entered 0 or 1 times per call # 
                j = 0 
                while (i<self.discs and self.currbits[i]==0): 
                    origin.append(self.discs-i) 
                    i += 1 
                    j += 1 

                # Shifting out of zeromode: Update configs, in partic. dest # 
                if ((j%2)==1): 
                    # New dest peg is current middle peg 
                    middidx = self.pegs.index(middle) 
                    destin = self.pegs[middidx] 
                    # Else, dest peg remains same; we do nothing. 
                zeromode = False 
            else:
                # Not in zeromode! # 
                j = 0 
                while (i<self.discs and self.currbits[i]==1): 
                    destin.append(self.discs-i)
                    i += 1 
                    j += 1   

                # ***Naw dude you can't do this. 0010 need to update first*** # 
                # Now we are back in zeromode # 
                k = 0 
                if ((j%2)==0): 
                    # Stack 0-bits on middle peg #  
                    while (i<self.discs and self.currbits[i]==0): 
                        middle.append(self.discs-i) 
                        i += 1 
                        k += 1  
                else: 
                    # Stack 0-bits on origin peg # 
                    while (i<self.discs and self.currbits[i]==0): 
                        origin.append(self.discs-i) 
                        i += 1 
                        k += 1 

                # Shifting out of zeromode: Update configs, in partic. dest #
                if ((k%2)==1):
                    # New dest peg is current middle peg
                    middidx = self.pegs.index(middle)
                    destin = self.pegs[middidx]
                    # Else, dest peg remains same; we do nothing.

            destidx = self.pegs.index(destin) 

            if ((i%2)==0): 
                # We have an even 1-bit; set origin to LEFT of dest # 
                origin = self.pegs[(destidx-1)%3]
                middle = self.pegs[(destidx+1)%3]
            else: 
                # We have an odd 1-bit; set origin to RIGHT of dest #
                origin = self.pegs[(destidx+1)%3]
                middle = self.pegs[(destidx-1)%3]


    def render(self): 
        """Print current turn nbr/total turns req'd & a repr. of curr game state."""  
        # This is obviously not the actual final render function. #  
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
