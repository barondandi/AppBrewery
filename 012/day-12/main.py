################### Scope ####################

# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Local Scope
# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)
#
# drink_potion()
# print(potion_strenght)

#Global Scope
player_health = 10

#def game():
#    def drink_potion():
#        potion_strenght = 2
#        print(player_health)
#    drink_potion()
#print(player_health)

#game_level = 3
#enemies = ["Skeleton", "Zombie", "Alien"]
#if game_level < 5:
#    new_enemy = enemies[0]
#print(new_enemy)

# Modifying global variables
enemies = 1
def increase_enemies():
   global enemies
   enemies += 1
   print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")
