spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = []
    for items in spicy_foods:
        name = [value for key, value in items.items()]
        names.append(name[0])
    return names


get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for items in spicy_foods:
        if items["heat_level"] > 5:
            spiciest_foods.append(items)

    return spiciest_foods


get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    for items in spicy_foods:
        spicy_food = [value for key, value in items.items()]
        pepper = '🌶'*spicy_food[2]
        print(f'{spicy_food[0]} ({spicy_food[1]}) | Heat Level: {pepper}')


print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass


def print_spiciest_foods(spicy_foods):
    for items in spicy_foods:
        if (items['heat_level']) >5:
            spicy_food = [value for key, value in items.items()]
        pepper = '🌶'*spicy_food[2]
        print(f'{spicy_food[0]} ({spicy_food[1]}) | Heat Level: {pepper}')


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass


# [item for item in my_dict.items()]
# # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# [key for key, value in my_dict.items()]
# # ['a', 'b', 'c', 'd']
# [value for key, value in my_dict.items()]
