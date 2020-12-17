from te_settings import MAXCOL, MAXROW, Direction

class AutoPlayer(): #Kaan Turan, UCL 2018
    finalMove = None
    finalRotation = None

    def __init__(self, controller):
        self.controller = controller

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        reset = True
        if reset:
            finalMove, finalRotation = self.best_move(gamestate)
            reset = False
        self.make_move(gamestate,finalMove,finalRotation)
        if gamestate.update():
            reset = True

    def best_move(self, gamestate):
        bestMove = 0
        bestRotation = 0
        highScore = None
        for i in range(0, MAXCOL*2):
            for j in range(0, 4):
                model = gamestate.clone(True)
                counter = j
                landed = False
                if i < MAXCOL: #checks every condition going right to left
                    for a in range(0, i):
                        model.move(Direction.LEFT)
                        if counter != 0: #if the block must rotate, do it in the same move
                            model.rotate(Direction.RIGHT)
                            counter -= 1
                        landed = model.update() 
                        if landed: #check to see if the block landed
                            counter = 0
                            break
                    for b in range(0, counter): #any remaining rotations are done seperatly
                        model.rotate(Direction.RIGHT)
                        landed = model.update()
                        if landed:
                            break

                elif i > MAXCOL: #checks every condition going left to right
                    for a in range(MAXCOL, i):
                        model.move(Direction.RIGHT)
                        if counter != 0:
                            model.rotate(Direction.RIGHT)
                            counter -= 1
                        landed = model.update()
                        if landed:
                            counter = 0
                            break
                    for b in range(0, counter):
                        model.rotate(Direction.RIGHT)
                        landed = model.update()
                        if landed:
                            break

                while landed is False: #the block is in the correct position and orientation, drop
                    landed = model.update()

                score = self.get_Score(model) #score the arena, including dropped block
                if highScore is None or score > highScore:
                    highScore = score
                    bestMove = i
                    bestRotation = j
        return (bestMove, bestRotation)

    def make_move(self,gamestate,finalMove,finalRotation):
        if finalMove < MAXCOL and finalMove != 0:
            gamestate.move(Direction.LEFT)
            finalMove -= 1
        elif finalMove > MAXCOL and finalMove != MAXCOL:
            gamestate.move(Direction.RIGHT)
            finalMove -= 1
        if finalRotation != 0:
            gamestate.rotate(Direction.RIGHT)
            finalRotation -= 1
            
    def get_Score(self, gamestate):
        modelTiles = gamestate.get_tiles()
        agregateHeight = 0
        completeLines = 0
        holes = 0
        bumpiness = 0
        wallTouch = 0

        for x in range(0, MAXCOL): #agregateHeight
            for y in range(0, MAXROW):  
                if modelTiles[y][x] != 0: 
                    agregateHeight += (MAXROW - y) 
                    break

        for y in range(0, MAXROW): #completeLines
            rowCheck = 0
            for x in range(0, MAXCOL):
                if modelTiles[y][x] != 0:
                    rowCheck += 1
            if rowCheck == MAXROW:
                completeLines += 1

        for x in range(0, MAXCOL): #holes
            for y in range(0, MAXROW):  
                if modelTiles[y][x] != 0:
                    for a in range(y, MAXROW):
                        if modelTiles[a][x] == 0:
                            holes += 1
                    break   
                    
        heightA = 0 
        heightB = 0
        for y in range(0, MAXROW): #bumpiness
            if modelTiles[y][0] != 0: 
                heightA = MAXROW - y
        for x in range(1, MAXCOL): 
            for z in range(0, MAXROW): 
                if modelTiles[z][x] != 0: 
                    heightB = MAXROW - z
                    break
            bumpiness += abs(heightA - heightB)
            heightA = heightB
            heightB = 0
        
        return ((-0.1)*agregateHeight + (10)*completeLines + (-100)*holes + (-20)*bumpiness)
        
        