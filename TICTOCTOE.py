# Display board
def display_board(positions):
    print(f'\n     |     |\n  {positions[6]}  |  {positions[7]}  |  {positions[8]}\n_____|_____|_____')
    print(f'     |     |\n  {positions[3]}  |  {positions[4]}  |  {positions[5]}\n_____|_____|_____')
    print(f'     |     |\n  {positions[0]}  |  {positions[1]}  |  {positions[2]}\n     |     |     ')
    
def player_input():
    valid_input = False
    while not valid_input:   
        player1 = input('\nWhat You choose X or O : ')
        player1 = player1.upper()
        valid_input = True
        if player1 == 'X':
            player2 = 'O'
            print(f'\nPlayer 1 : {player1}\nPlayer 2 : {player2}')
        elif player1 == 'O':
            player2 = 'X'
            print(f'\nPlayer 1 : {player1}\nPlayer 2 : {player2}')
        else:
            valid_input = False
            print('Error: You can choose X or O')
    return {1:player1,2:player2}      

def user_move():
    got_valid_input = False
    while not got_valid_input:
            inp = input(f'Player {turn} Where you Want to put {players[turn]} : ')
            if inp in ['1','2','3','4','5','6','7','8','9']:
                inp = int(inp)
                if board[inp-1] == ' ':
                    board[inp-1] = players[turn] 
                    got_valid_input = True
                else:
                    print('\nCant Place there! Position Already Full!!')
            else:
                print('\n'*100)
                print('\nGive valid Input!!')
                display_board(board)

def win_check():
    if (board[0]==board[1]==board[2]==players[turn]) or (board[3]==board[4]==board[5]==players[turn]) or (board[6]==board[7]==board[8]==players[turn]):
        return True
    if (board[0]==board[3]==board[6]==players[turn]) or (board[1]==board[4]==board[7]==players[turn]) or (board[2]==board[5]==board[8]==players[turn]):
        return True    
    if (board[0]==board[4]==board[8]==players[turn]) or (board[2]==board[4]==board[6]==players[turn]):
        return True
    return False
        
#Main Program
#from IPython.display import clear_output
flag = True
while flag:
    print('\nLets Start New Game!!')
    game_over = False
    turn = 2
    board = [' ']*9
    players = player_input()
    while not game_over:
        turn = 3 -  turn #Toggle between player 1 & 2
        print('\n'*100)
        display_board(board)
        user_move()
        if win_check():
            game_over = True
            print('\n'*100)
            print(f'\nPlayer {turn} Wins The Game!!!')
            display_board(board)
        elif ' ' not in board:    #Check if board is Full
            game_over = True
            print('\n'*100)
            print('Its a DRAW!!!')
            display_board(board)
    while flag:
        ask = input('Would You like to play it Again?').upper()
        print('\n'*100)
        if ask == 'N':
            print('\nFuck off!!')
            flag = False
        elif ask == 'Y':
            break
        else: 
            print('\nError: Type Y for Yes & N for No')