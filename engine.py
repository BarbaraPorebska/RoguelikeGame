import random


def create_board(width, height):
    """
    Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    """

    board = []

    for i in range(height):
        if i == 0:
            row = []
            for k in range(width):
                row.append("#")
        elif i == height - 1:
            row = []
            for l in range(width):
                row.append("#")
        else:
            row = []
            row.append("#")
            for j in range(width - 2):
                row.append(" ")
            row.append("#")
        board.append(row)

    return board


def put_player_on_board(board, player):
    """
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    """

    for y, row in enumerate(board):
        for x, column in enumerate(row):
            if column == player["icon"]:
                board[y][x] = " "

    x, y = player["position"]
    board[y][x] = player["icon"]


def enemies_placement(board, enemy, width, height):
    board = create_board(width, height)
    y = random.randint(1, height - 1)
    x = random.randint(1, width - 1)
    if board[y][x] == " ":
        board[y][x] = enemy
    else:
        enemies_placement(board, enemy, width, height)
    return board


def put_items_on_board(board, count):
    for _ in range(count):
        put_char_on_board(board, "?")


def collision_check(board, position, movement):
    X = 0
    Y = 1

    new_position = (
        position[X] + movement[X],
        position[Y] + movement[Y],
    )

    return board[new_position[Y]][new_position[X]] != " "


def check_collision_type(board, position, movement):
    X = 0
    Y = 1

    new_position = (
        position[X] + movement[X],
        position[Y] + movement[Y],
    )

    return board[new_position[Y]][new_position[X]]


def put_char_on_board(board, char, rand=True, x=0, y=0):
    if rand:
        x = random.randint(1, (len(board[0]) - 2))
        y = random.randint(1, len(board) - 2)
    board[y][x] = char
    return (x, y)


def create_cave(width, height):
    random_width = random.randint(10, int(width * 0.7) - 1)
    random_height = random.randint(10, int(height * 0.7) - 1)
    board = create_board(random_width, random_height)
    return board

def boss_placement_validation(board,width,height,row,column):
    board = create_board(width, height)
    placement_validation = True
    if board[row][column] == " ":
        for i in range(5):
            for j in range(5):
                if board[row + i][column + j] != " ":
                    placement_validation = False
    return placement_validation

def place_boss(board,width,height):
    if (
    any("@" in i for i in board)
    and not any("R" in i for i in board)
    and not any("S" in i for i in board)
    and not any("Z" in i for i in board)
    and not any("G" in i for i in board)
    and not any("H" in i for i in board)
    ):
        while True:
            row = random.randint(1, height-5) 
            column = random.randint(1, width-5)
            if boss_placement_validation(board,width,height,row,column):
                break
        for i in range(5):
            for j in range(5):
                put_char_on_board(board, "N", False, column +j, row + i)
