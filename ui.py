import os

def display_board(board):
    """
    Displays complete game board on the screen

    Returns:
    Nothing
    """
    for row in board:
        for column in row:
            print(column, end=" ")
        print()


def show_stats(player):
    print("\nLEVEL: " + str(player["level"]), end="    ")
    print(
        "HEALTH: " + str(player["health"]) + " \ " + str(player["max_health"]),
        end="    ",
    )
    print(
        "ARMOR: " + str(player["armor"]["stat"]),
        end="    ",
    )
    print("MAX ATTACK: " + str(player["attack"]) + " (+" + str(player["weapon"]["stat"]) + ")", end="    ")
    print(
        "EXP: " + str(player["exp"]) + " \ " + str(player["level_exp_threshold"]) + "\n"
    )
    print("WEAPON: " + str(player["weapon"]["name"]) + " (+" + str(player["weapon"]["stat"]) + ")", end="    ")
    print("ARMOR: " + str(player["armor"]["name"]) + " (+" + str(player["armor"]["stat"]) + ")" + "\n")


def new_board(board, player):
    display_board(board)
    show_stats(player)


def display_inventory(player):
    pass

def pause():
    if os.name == 'nt': 
        os.system('pause') 
    else: 
        input("Press the Enter key to proceed")