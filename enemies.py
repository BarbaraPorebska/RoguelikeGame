import random
from player import *
import ui
import util
from engine import *

RAT = {"HP" : 5, "ATK" : 3, "name": "RAT", "icon": "R"}
SKELETON = {"HP" : 8, "ATK" : 4, "name": "SKELETON", "icon": "S"}
ZOMBIE = {"HP" : 12, "ATK" : 5, "name": "ZOMBIE", "icon": "Z"}
GHOST = {"HP" : 15, "ATK" : 10, "name": "GHOST", "icon": "G"}
VAMPIRE = {"HP" : 20, "ATK" : 10, "name": "VAMPIRE", "icon": "V"}

MONSTERS_ICONS_AND_TYPES = {"R" : RAT, "S": SKELETON, "Z": ZOMBIE, "G": GHOST, "V": VAMPIRE}

MAIN_ROOM_ENEMIES = [RAT["icon"], SKELETON["icon"], ZOMBIE["icon"], GHOST["icon"]]
EASY_ROOM_ENEMIES = [RAT["icon"], SKELETON["icon"], ZOMBIE["icon"]]
MEDIUM_ROOM_ENEMIES = [SKELETON["icon"], ZOMBIE["icon"], GHOST["icon"]]
HARD_ROOM_ENEMIES = [ZOMBIE["icon"], GHOST["icon"], VAMPIRE["icon"]]

def enemies_placement(board, number_of_enemies, enemies_pool):
    enemy_id = 0
    while enemy_id < number_of_enemies:
        enemy = random.choice(enemies_pool)
        x = random.randint(1, len(board[0]) - 1)
        y = random.randint(1, len(board) - 1)
        if board[y][x] == " ":
            board[y][x] = enemy
            enemy_id += 1

def check_monster_type(board, position, movement):
    monster_icon = check_collision_type(board, position, movement)
    return MONSTERS_ICONS_AND_TYPES[monster_icon]
    

def survive_fight(player, enemy_type, board):
    player_attack = player["attack"]
    player_defense = player["armor"]["stat"]
    player_bonus_attack = player["weapon"]["stat"]
    enemy_name = str(enemy_type["name"])
    max_enemy_health = random.randint(round(enemy_type["HP"]/2), enemy_type["HP"])
    enemy_health = max_enemy_health
    enemy_attack = random.randint(round(enemy_type["ATK"]/2), enemy_type["ATK"])
    exp_reward = round((enemy_attack + enemy_health) / 2)
    util.clear_screen()
    print(f"You approach {enemy_name}!")
    fight_stop, escape_attempt = escape_or_fight(player, board, enemy_name, enemy_health, max_enemy_health)
    while not fight_stop and enemy_health > 0:
        if not escape_attempt:
            player_hit = random.randint(round(player_attack/2), player_attack)
            player_hit_total = player_hit + player_bonus_attack
            enemy_health -= player_hit_total
            print(f"You deal {player_hit} damage + {player_bonus_attack} from weapon ({player_hit_total} total)")
            if enemy_health <= 0:
                print(f"{enemy_name} dies. You get {exp_reward} experience.\n")
                player["exp"] += exp_reward
                ui.new_board(board, player)
                player_xp_gain(player, board)
                break
            fight_stop, escape_attempt = escape_or_fight(player, board, enemy_name, enemy_health, max_enemy_health)
        if not fight_stop:
            enemy_hit = random.randint(round(enemy_attack/2), enemy_attack)
            enemy_hit_total = enemy_hit - player_defense
            enemy_hit_total = max(enemy_hit_total, 0)
            player["health"] -= enemy_hit_total
            print(f"{enemy_name} deals {enemy_hit} damage and you defend {player_defense} ({enemy_hit_total} damage dealt total)")
            if player["health"] <= 0:
                print("...and kills you\n")
                ui.new_board(board, player)
                return False
            fight_stop, escape_attempt = escape_or_fight(player, board, enemy_name, enemy_health, max_enemy_health)
    return True


def escape_or_fight(player, board, enemy_name, enemy_health, max_enemy_health):
    fight_stop = None
    escape_attempt = None
    while True:
        print(f"{enemy_name}'s health: {enemy_health} \ {max_enemy_health}\n")
        ui.new_board(board, player)
        print("\tDo you want to ESCAPE [E] or FIGHT [F]? ")
        key = util.key_pressed()
        util.clear_screen()
        if key == "f":
            fight_stop = False
            escape_attempt = False
            break
        elif key == "e":
            escape_chance = random.choice([True, False])
            if escape_chance:
                fight_stop = True
                print("You escaped\n")
                ui.new_board(board, player)
            else:
                fight_stop = False
                print("You didn't manage to escape\n")
            escape_attempt = True
            break
    return fight_stop, escape_attempt