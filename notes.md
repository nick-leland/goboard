# Go Board

## Board Sizes
The game board is comprised of 3 sizes, 9 x 9, 13 x 13 and 19 x 19.
We must poll the user at the beginning of the program to determine which board to generate.

### White Circle
Unicode 25CB: ○

### Black Circle
Unicode 25CF: ●

To insert Unicode into vim use ctrl + v in insert mode and then press 'u'. 

### Board Generation
Based on the size of the board we will need to generate the squares whcih will occupy the board 

 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x O x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x

The game will be created ideally in this order:

 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 x x x x x x x x x
 9 x x x x x x x x
 0 1 2 3 4 5 6 7 8


All boards have a center point.  We can label this point [0,0], above it is displayed as O.  From here we can view the game as a cartesian board.  

We will create a modifier using the (size of the board \ 2). If a point uses *one* of these modifiers as a coordinate, it will be marked as an edge.  If it uses *two* of these points, it will be then marked as a corner.  

This also means we will be able to create points up to the maximum board size and then shrink down to the user determined board size after. 

## Class Definition
We will need to define 3 different types of classes.  The basic board space, the edge, and the corner.  

## Game Operation
Every turn, a player will place a piece and then the game will poll the remaining pieces on the board to determine groups and whether the group is captured or not.  A captured group will updated during this polling period and add to the players score.  

## Coordinate System
There are various ways of recording game coordinates on the Go Board.  American standards, known as Style A1, record the bottom right of the board as A1 while japanese standards of recording is known as Style 1-1, which records the upper left corner as 1-1 and the bottom right as 19-19.  I believe there is one more method for recording game coordinates. This could be something to poll for and determine if the user would prefer for game recording.  
