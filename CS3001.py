import random, sys

def board():
    '''Make matrix board of random numbers'''
    list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    random.shuffle(list1)
    matrix = []
    while list1 !=[]:
        matrix.append(list1[:4])
        list1 = list1[4:]
    return matrix
def zero(board):
    '''function to find where the zero is'''
    empty_space = None
    for x,item in enumerate(board):
        for y,item in enumerate(board):
            if board[x][y] == 0:
                empty_space = (x,y)
    return empty_space
def draw_board(board):
    '''function to draw the board'''
    print('\n\t+-------+-------+-------+-------|')
    for x,item in enumerate(board):
        for y,item in enumerate(board):
            if board[x][y] == 0:
                print('\t|  XX' , end='')
            else:
                 print('\t|  ' + '{:02d}' .format(board[x][y]), end=' ')
        print('\n\t+-------+-------+-------+-------|')
def ask_number(board):
    ''' function to ask for the number to move'''
    num = input('\nplease type the number of the piece to move : ( q ) to quit  ')
    if num in ['q','Q']:
        print('\n\ngame over  ')
        sys.exit()
    num = int(num)
    piece = ()
    for i,item in enumerate(board):
        for j,item in enumerate(board):
            if num == board[i][j]:
                piece = (i,j)
    return piece , num
def game():
    '''Run the game logic'''
    matrix = board()
    empty_space = zero(matrix)
    game_on = True
    move = 0
    while game_on:
        draw_board(matrix)
        piece,num = ask_number(matrix)
        if num > 15:
            print('illegal move , try again  ')
        else:
            if(empty_space==(piece[0]-1,piece[1]))\
               or(empty_space==(piece[0]+1,piece[1]))\
               or(empty_space==(piece[0],piece[1]-1))\
               or(empty_space==(piece[0],piece[1]+1)):
                matrix[empty_space[0]][empty_space[1]]=num
                matrix[piece[0]][piece[1]]=0
                empty_space=(piece[0],piece[1])
                move = move +1
                print()
                print('you have made ',move , 'moves so far ')
                print(2*'\n')
            else:
                print('illegal move , try again ')
if __name__ == '__main__':
    game()