ITEM_ICON = "?"


def create_item(name: str, type: str, stat: int):
    """
    Creates an 'item' dictionary for storing an item's information i.e. item icon, item position.

    Returns:
    dictionary
    """
    item = {
        "icon": ITEM_ICON,
        "name": name,
        "type": type,
        "stat": stat,
    }

    return item


def equip_message(item):
    pass


def pickup(player, item):
    match item["type"]:
        case "Weapon":
            if item["stat"] > player["weapon"]["stat"]:
                player["weapon"] = item
        case "Armor": 
            if item["stat"] > player["armor"]["stat"]:
                player["armor"] = item
        case "Potion":
            if item["stat"] + player["health"] >= player["max_health"]:
                player["health"] = player["max_health"]
            else:
                player["health"] += item["stat"]
