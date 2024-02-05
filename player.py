import util
import ui

PLAYER_ICON = "@"
PLAYER_START_X = 3
PLAYER_START_Y = 3
STATS_MULTIPLIER = 1.25


def create_player(weapon, armor, x=PLAYER_START_X, y=PLAYER_START_Y):
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    """
    player = {
        "icon": PLAYER_ICON,
        "position": (x, y),
        "health": 10,
        "max_health": 10,
        "attack": 5,
        "level": 1,
        "exp": 0,
        "level_exp_threshold": 10,
        "weapon": weapon,
        "armor": armor,
    }

    return player


def player_move(player: dict, movement: tuple):
    """
    Moves the player based on the given tuple (x, y)

    Returns:
    None
    """
    X = 0
    Y = 1

    player["position"] = (
        player["position"][X] + movement[X],
        player["position"][Y] + movement[Y],
    )


def player_xp_gain(player, board):
    if player["exp"] >= player["level_exp_threshold"]:
        player["level_exp_threshold"] = round(
            player["level_exp_threshold"]
            + player["level_exp_threshold"] * STATS_MULTIPLIER
        )
        player["level"] += 1
        player["attack"] = round(player["attack"] * STATS_MULTIPLIER)
        player["max_health"] = round(player["max_health"] * STATS_MULTIPLIER)
        player["health"] = player["max_health"]
        util.clear_screen()
        print("LEVEL UP! YOU'RE NOW LEVEL " + str(player["level"]) + "!\n")
        ui.new_board(board, player)
