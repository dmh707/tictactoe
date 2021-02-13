
#initialize a globalVars function that contains the board
def globalVars():
    globalVars.players=['X',"O"]
    globalVars.active_player = 0
    globalVars.winning_sets = {
        0 : [
            [0,1,2],
            [0,3,6]
            ],
        4 :[
            [3,4,5],
            [1,4,7],
            [0,4,8],
            [2,4,6]
            ],

        8 : [
            [6,7,8],
            [2,5,8],
            ]
        }
#    initialize a globalVars.board_list variable which is an empty list
    globalVars.board_list = []
#    initialize a list_range variable which is a range of 9
    list_range = range(9)
#    start a for loop for the list_range
    for x in list_range:
#        append the item to the globalVars.board_list
        globalVars.board_list.append(x)
#run the globalVars function
globalVars()


#initialize a function that displays the board
def display_board():
#    initialize a board_list variable equal to the globalVars version, for ease of typing
    board_list = globalVars.board_list
#    initialize a vertical line variable as a string
    vert_line = "|"
#    initialize a horizontal line variable as a string
    horz_line = "\n-----------\n"
#    initialize a print_str variable as an empty string
    print_str=''
#    start a for loop for all items in board_list
    y = 0
    for x in board_list:
#        if it is at locations 0,1,3,4,6,7
        if y in [0,1,3,4,6,7]:
#            add a space, the item, a space, and the vertical variable to the print_str variable
            print_str = print_str + ' ' + str(x) + ' ' + vert_line
#        otherwise if it at loctaions 2 or 5
        elif y in [2,5]:
#            add a space, the item, and the horizontal line variable to the print_str variable
            print_str = print_str + ' ' + str(x) + ' ' + horz_line
#        otherwise if it at location 8
        elif y == 8:
#            add a space and the item to the print_str variable
            print_str = print_str + ' ' + str(x)
#        otherwise
        else:
#            print("unable to display board. The board_list variable has too many elements")
            print("unable to display board. The board_list variable has too many elements")
#            return
            return
        y=y+1
#    print the print_str
    print(print_str)
display_board()

#initialize a function that allows you to select a spot on the board, taking the spot and the player "x" or "o" as arguments
def play(spot):
    player=active_player()
    #initialize a board_list variable equal to the globalVars version, for ease of typing
    board_list = globalVars.board_list
    #if board_list[spot] is the same as spot
    if board_list[spot] == spot:
        #set board_list[spot] to the player character
        board_list[spot]=player
        
        #set the globalVars version of board_list equal to the local one
        globalVars.board_list = board_list
        #display the board
        display_board()
        #check if you have won
        check_winner()
        

    else:
        print("Play not counted. It is still %s's turn.\n" % player)

def check_winner():
    player_spots= get_active_player_spots()
    
    win_sets_all = globalVars.winning_sets
    the_ints = [0,4,8]
    for the_int in the_ints:
        if the_int in player_spots:
            win_sets_0 = win_sets_all[the_int]
            for win_set in win_sets_0:
                i=0
                for integer in win_set:
                    if integer in player_spots:
                        i=i+1
                    if i==3:
                        print("you win.")
                        return
    cycle_active_player()
def get_active_player_spots():
    player = active_player()
    player_spots_list = []
    board = globalVars.board_list
    for i in range(len(board)):
        if board[i]==player:
            player_spots_list.append(i)
    player_spots_list.sort()
    return player_spots_list
    

def active_player():
    return globalVars.players[globalVars.active_player]
    
'''
initialize a function that cycles through the players
    
'''
def cycle_active_player():
    active = globalVars.active_player
    if active == 0:
        active =1
    else:
        active = 0
    globalVars.active_player = active
    player = globalVars.players[active]
    print("It is %s's turn" % player)

'''
initialize function that runs the game
    initialize a variable for active player from the globalVars
    initialize a variable for all players from globalVars
    
'''