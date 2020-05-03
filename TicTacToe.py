from text import *
from datetime import datetime

#initiates and checks if its inside the module or just imported
if __name__ == '__main__': 
    print('Working inside module')
    input('Press Enter to end the program.')
else:

    class TicTacToe():

        def __init__(self):
            #creates board at initiation
                self.Board = self.DefineBoard()
                self.FlatBoard = self.DefineFlatBoard()
                self.MovesDictionary = self.CreateMovesDictionary()
        #creates 3x3 board
        def DefineBoard(self):
            #board goes from 1 to 9
            return [[i+j for i in range(1,4)] for j in range(0,9,3)]

        #creates moves dictionarty with tuples of coordinates eg. '1':(0,0)
        def CreateMovesDictionary(self):
            TempDictionary = {}
            for j in range(3):    
                for i in range(3):
                    TempDictionary.update({str(3*j+i+1):(j, i)})
            return TempDictionary
        #creates flat list of moves, which is used for pritning
        def DefineFlatBoard(self):
            #flattens the 3x3 list
            return [item for sublist in self.Board for item in sublist]

        #returns tuples with coordinates available to move
        def ListOfFreeFields(self):
            #define empty list
            Free = []
            for i in range(3):
                for j in range(3):
                    if type(self.Board[i][j]) == int:
                        #append coordinates tuple if field is free
                        Free.append(self.MovesDictionary[str(self.Board[i][j])])
            return Free
        #asks user to enter his move, checks if data is correct
        def EnterMove(self, sign):
            while True:
                try:
                    #creates list of free moves
                    Free = self.ListOfFreeFields()
                    #prints text on which field user wants to move
                    print(WhichField)
                    #gets move
                    Move = input()
                    #1 checks if move in range 1-9
                    if int(Move) in range(1,10):
                        #2 checks if field is taken
                        if self.MovesDictionary.get(Move) not in Free:
                            print(FieldTaken)
                        else: break
                    else: print(WrongMove)
                #3 exception handling: Value Error
                except ValueError:
                    print(WrongData)
                #4 No surrender exception
                except KeyboardInterrupt:
                    print(NoInterrupt)
            #makes the move
            self.ApplyMove(Move, sign)

            
        #applies move to the board, gets move 1-9 and sign ("O", "X", but can be also other string)
        def ApplyMove(self, Move, sign):    
            # temp variable that points to tuple with coordinates of move
            DictionaryTarget =  self.MovesDictionary.get(Move)
            # Prints "sign" to given number on the field
            self.Board[DictionaryTarget[0]][DictionaryTarget[1]] = sign
        
        #prints board to user
        def PrintBoard(self):
            #updates flat board
            self.FlatBoard = self.DefineFlatBoard()
            #1-13
            for k in range(1,14):
                    #prints  1st, 5th, 9th, 13th line
                    if k%4 == 1:
                        print('+','+','+','+', sep='-'*7)
                    #prints even number of line
                    elif k%2 == 0:
                        print('|','|','|','|', sep = ' '*7)
                    #prints lines with numbers and signs on board
                    else:
                        for i in range(3):
                            #prints 1st element every time and then pops it
                            print('|',self.FlatBoard[0], sep=' '*3, end = ' '*3)
                            self.FlatBoard.pop(0)
                        print('|')
        
        #returns pseudorandom number in range (1-ran)
        def RandomMove(self, ran):
            return str(int(datetime.now().timestamp()*10000000)%ran+1)

        #computer makes move
        def ComputerMove(self):
            #pseudorandom move in range (1-9)
            Move = self.RandomMove(9)
            #checks if there are any moves, if there are no more moves, returns nothing
            if self.ListOfFreeFields() == []: 
                return None
            #loop checking whether field is available
            while self.MovesDictionary.get(Move) not in self.ListOfFreeFields():
                #if field is taken, chooses another psuedorandom number
                Move = self.RandomMove(9)
                continue
            #applies move to the board
            self.ApplyMove(Move, "X")

        def VictoryFor(self, sign):
            for i in range(3):
                #checks vertically
                if self.Board[0][i] == self.Board[1][i] == self.Board[2][i] == sign:
                    return True
                #checks horizontally
                elif self.Board[i][0] == self.Board[i][1] == self.Board[i][2] == sign:
                    return True
            #checks diagonally right to left
            if self.Board[0][0] == self.Board[1][1] == self.Board[2][2] == sign:
                return True
            #checks diagonally left to right
            elif self.Board[0][2] == self.Board[1][1] == self.Board[2][0] == sign:
                return True
            else: 
                return False

    #plays the game
    def Play():
        #prints initial message about the game
        print(Beggining)
        #creates object
        game = TicTacToe()
        #iterator used for turns
        i = 0
        #loop
        while not game.VictoryFor("X") and not game.VictoryFor("O"):
            #creates list of available moves
            MovesAvailable = game.ListOfFreeFields()
            #if there are no moves, prints message about tie and breaks the loop
            if MovesAvailable == []:
                print(Tie)
                break
            #computers move for even "i"
            if i % 2 == 0:
                print(ComputersTurn)
                game.ComputerMove()
                i += 1
            #players move for odd "i"
            elif i % 2 != 0:
                print(PlayersTurn)
                game.EnterMove('O')
                i += 1
            #prints the board
            game.PrintBoard()
            #checks victory for "X" and "O"
            if game.VictoryFor('X'): print(Victory, end = 'X! \n')
            elif game.VictoryFor('O'): print(Victory, end = 'O! \n')
        input('Press Enter to end the game.')