## bintoh: Binary Tower of Hanoi 

This program will show you the shortest possible playthrough of a Tower of Hanoi 
game involving n discs. It exploits an interesting property of the game, which is 
that an n-disc instance of the game can be modeled via a series of bitstrings of 
length n.  


// Usage 

```
$ python bintoh.py <n> 
$ python3 bintoh.py <n> 
```

// Reading the output

The following slice of output represents the state of a 3-disc game after the first 
move has been made:

```
Current move: 2/8
Left   Peg = [3, 2]
Center Peg = []
Right  Peg = [1]
```

This translates to the following: 

```
    |       |       |    
  ==2==     |       |
 ===3===    |      =1=   
 ________________________

```

// Notes