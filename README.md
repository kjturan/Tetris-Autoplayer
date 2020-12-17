# Source code for the Tetris game.

To run:
`python3 tetris.py`

## Your task
Write a better AutoPlayer than the one included with this source.

## Rules
 * THIS IS AN ASSESSED COURSEWORK.  THE CODE YOU SUBMIT MUST BE ENTIRELY YOUR OWN.  If in doubt, ask.
 * The TAs can help you.  They won't give you the answer, but if you're stuck, they may give you some hints.  They will not debug your code for you, but they can *help you* debug your code if they think it's appropriate and will help you learn.
 * You will only hand in your version of `te_autoplayer.py`, so don't depend on any changes you make to any other files.
 * You can only call functions in `te_gamestate.py`
 * Your code will be automatically marked by submitting to gitlab.  Instructions for this will follow in due course.  We will run your code for five games with five different random seeds.  We will take the median mark of the five runs as being representative of what your code can achieve.
 * To pass (earn 40%), you have to beat the score achieved by the random autoplayer supplied.
 * To get higher marks, you need to beat the score achieved by successively smarter implementations I have written.  These scores will be published in due course.
 * Don't try to cheat, such as by directly changing the score, or affecting the random sequence of pieces.  Our marking code will check for this, and anyone found cheating will receive zero marks for the coursework.

## Controls

See the source code in te_controller.py

 * **a** - move left
 * **s** - move right
 * **k** - rotate left
 * **l** - rotate right
 * *space* - drop
 * **y** - toggle autoplay
 * **q** - quit
 * **r** - restart
 
## Hints

You can enable autoplay by default by editing te_settings.py

You can beat the included random strategy with some pretty dumb solutions.  You only have to beat random to achieve a pass mark.

Exhaustive search won't work for this problem.  Searching all the positions and rotations for the only current tetronimo can do quite well, if you can come up with a good way to score the position.  Searching all the positions and rotations for the current and next tetronimo can do a bit better, but only if you've a good way to score the final position.
