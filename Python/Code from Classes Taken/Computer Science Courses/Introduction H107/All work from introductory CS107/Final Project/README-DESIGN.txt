Design of Checkers_Game



In order to play checkers, I created a board class that holds a checkers board as well as the count of 
the pieces of each player. 

It has 13 (technically 14 counting method 5.5) methods. Each of which is explained.

I use these to implement my three main functions:
game(), game_ai() and ai_input()

Game and game_ai are quite similar. In both I nest a while loop of one person's turn inside another while loop
to alternate turns and keep the game going. Then, when the game is over and we are out of the while loop
I print the winner (or if it was a draw).

The important difference is that in game() I allow the input to either be as many stored inputs were in 
the list input_list or the user's input. So, one could, if one was storing their game with a friend
play from where one left off by running game(b) where b is the list of inputs given the last game.
On the other hand, in game_ai(), I allow the input for player 1 to be given by the user and player 2's input 
to be given by the ai_input function.


I explain how I implement ai_input with comments. The general idea is that my ai is a pacificst and 
tries to avoid conflict at all costs by trying to walk in manners that don't allow the opponent to 
capture his pieces.








