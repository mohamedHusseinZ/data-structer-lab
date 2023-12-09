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
    for food in spicy_foods:
        print(food["name"])

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        print(food["name"])

        get_spiciest_foods(spicy_foods)


    
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"])

        print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    matching_foods = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return matching_foods

    pass

def print_spiciest_foods(spicy_foods):
    
    spiciest_food = max(spicy_foods, key=lambda food: food["heat_level"])
    print(f"The spiciest food is {spiciest_food['name']} with a heat level of {spiciest_food['heat_level']}.")

    pass

def get_average_heat_level(spicy_foods):
    
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat

    pass

def create_spicy_food(spicy_foods, spicy_food):
    
    spicy_foods.append(ugali)
    print(ugali)
    return spicy_foods

    pass
