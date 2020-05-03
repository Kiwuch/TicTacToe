#checks if its inside the module or just imported
if __name__ == '__main__': 
    print('Working inside module')
    input('Press Enter to end the program.')
else:
    #set of texts which are printed on the screen
    Beggining = """
Tic Tac Toe Game
Can you beat the computer?
    """
    WhichField = 'Where would you like to put your sign?'
    FieldTaken = 'That field is already taken! Choose another field (1-9)'
    WrongMove = 'Wrong Move! Choose another move (1-9):'
    WrongData = 'Wrong value! Choose anothe value (1-9):'
    NoInterrupt = 'You can\'t surrender!'
    Tie = 'Tie!'
    Victory = 'Victory for '
    PlayersTurn = 'Your move: '
    ComputersTurn = 'Computer\'s move: '
