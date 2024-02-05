import util
import engine
import ui
import player
import item
import enemies
import random

BOARD_WIDTH = 30
BOARD_HEIGHT = 25
NUMBER_OF_ENEMIES_BIG = 8
NUMBER_OF_ENEMIES_SMALL = 5


ITEMS = [
    ("Sword", "Weapon", 2),
    ("Axe", "Weapon", 3),
    ("Leather", "Armor", 2),
    ("Mail", "Armor", 3),
    ("Small potion", "Potion", 4),
    ("Medium potion", "Potion", 6),
]


def main():
    my_player = player.create_player(
        item.create_item("Fists", "weapon", 1), item.create_item("Clothing", "armor", 0)
    )
    main_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    engine.put_items_on_board(main_board, 1)
    engine.place_boss(main_board,BOARD_WIDTH,BOARD_HEIGHT)
    cave_1 = engine.create_cave(BOARD_WIDTH, BOARD_HEIGHT)
    cave_1_position = engine.put_char_on_board(main_board, "o")
    cave_2 = engine.create_cave(BOARD_WIDTH, BOARD_HEIGHT)
    cave_2_position = engine.put_char_on_board(main_board, "O")
    cave_3 = engine.create_cave(BOARD_WIDTH, BOARD_HEIGHT)
    cave_3_position = engine.put_char_on_board(main_board, "Q")
    engine.put_char_on_board(cave_3, "H", False, len(cave_3[0]) - 2, len(cave_3) - 2)
    engine.put_items_on_board(cave_1, 1)
    engine.put_items_on_board(cave_2, 1)

    cave_4 = engine.create_cave(BOARD_WIDTH, BOARD_HEIGHT)
    cave_4_position = engine.put_char_on_board(main_board, "0")
    engine.put_char_on_board(cave_3, "H")

    item_pool = []

    for i in ITEMS:
        item_pool.append(item.create_item(i[0], i[1], i[2]))

    random.shuffle(item_pool)

    util.clear_screen()
    difficulty = 1
    is_running = True
    displayed_board = main_board
    enemies.enemies_placement(
        displayed_board, NUMBER_OF_ENEMIES_BIG, enemies.MAIN_ROOM_ENEMIES
    )

    while is_running:
        match difficulty:
            case 1:
                enemies_pool = enemies.EASY_ROOM_ENEMIES
            case 2:
                enemies_pool = enemies.MEDIUM_ROOM_ENEMIES
            case [3, 4]:
                enemies_pool = enemies.HARD_ROOM_ENEMIES
        engine.put_player_on_board(displayed_board, my_player)
        ui.new_board(displayed_board, my_player)
        key = util.key_pressed()
        x = 0
        y = 0
        if key == "q":
            is_running = False
        elif key in ["w", "s", "a", "d"]:
            match key:
                case "w":
                    y -= 1
                case "s":
                    y += 1
                case "a":
                    x -= 1
                case "d":
                    x += 1
            movement = (x, y)
            if engine.collision_check(displayed_board, my_player["position"], movement):
                match engine.check_collision_type(
                    displayed_board, my_player["position"], movement
                ):
                    case item.ITEM_ICON:
                        item.pickup(my_player, item_pool.pop())
                        player.player_move(my_player, movement)
                    case "H":
                        if displayed_board == cave_1:
                            my_player["position"] = cave_1_position
                        elif displayed_board == cave_2:
                            my_player["position"] = cave_2_position
                        elif displayed_board == cave_3:
                            my_player["position"] = cave_3_position
                        elif displayed_board == cave_4:
                            my_player["position"] = cave_4_position
                        difficulty += 1
                        displayed_board = main_board
                    case "o":
                        displayed_board = cave_1
                        my_player["position"] = (1, 1)
                        enemies.enemies_placement(
                            displayed_board, NUMBER_OF_ENEMIES_SMALL, enemies_pool
                        )
                    case "O":
                        displayed_board = cave_2
                        my_player["position"] = (1, 1)
                        enemies.enemies_placement(
                            displayed_board, NUMBER_OF_ENEMIES_SMALL, enemies_pool
                        )
                    case "Q":
                        displayed_board = cave_3
                        my_player["position"] = (1, 1)
                    case "0":
                        displayed_board = cave_4
                        my_player["position"] = (1, 1)
                        enemies.enemies_placement(
                            displayed_board, NUMBER_OF_ENEMIES_SMALL, enemies_pool
                        )

                if engine.check_collision_type(
                    displayed_board, my_player["position"], movement
                ) in list(enemies.MONSTERS_ICONS_AND_TYPES.keys()):
                    monster_type = enemies.check_monster_type(
                        displayed_board, my_player["position"], movement
                    )
                    player_win = enemies.survive_fight(
                        my_player, monster_type, displayed_board
                    )
                    if not player_win:
                        print("\nYOU LOSE")
                        is_running = False
                    else:
                        player.player_move(my_player, movement)
                    ui.pause()
            else:
                player.player_move(my_player, movement)
        if (
            displayed_board == cave_1
            and any("@" in i for i in cave_1)
            and not any("R" in i for i in cave_1)
            and not any("S" in i for i in cave_1)
            and not any("Z" in i for i in cave_1)
            and not any("G" in i for i in cave_1)
            and not any("H" in i for i in cave_1)
        ):
            engine.put_char_on_board(cave_1, "H")
        elif (
            displayed_board == cave_2
            and any("@" in i for i in cave_2)
            and not any("R" in i for i in cave_2)
            and not any("S" in i for i in cave_2)
            and not any("Z" in i for i in cave_2)
            and not any("G" in i for i in cave_2)
            and not any("H" in i for i in cave_2)
        ):
            engine.put_char_on_board(cave_2, "H")

        if displayed_board == cave_3:
            engine.put_char_on_board(cave_3, "M")
            engine.put_char_on_board(cave_3, "M")
        util.clear_screen()


if __name__ == "__main__":
    main()
