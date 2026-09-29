import random
import time

pokedex = []


class Pokemon:
    def __init__(self, name, type, hp, max_hp, attacks, evolutions, weakness, speed, xp, level, xp_to_next_level):
        self.name = name
        self.type = type
        self.hp = hp
        self.max_hp = max_hp
        self.attacks = attacks
        self.evolutions = evolutions
        self.weakness = weakness
        self.speed = speed
        self.xp = xp
        self.level = level
        self.xp_to_next_level = xp_to_next_level

    def attack(self, chosen_attack, target):
        if chosen_attack.type == target.weakness:
            temp_damage = chosen_attack.damage
            temp_damage *= 1.3
            temp_damage = int(temp_damage)
            target.hp -= temp_damage
            if target.hp < 0:
                target.hp = 0
            print("Its super effective!")
            print(
                f"{self.name} used {chosen_attack.name} and dealt {temp_damage} damage! Remaining HP: {target.hp} / {target.max_hp} ")
            print("")
            time.sleep(1)
        else:
            target.hp -= chosen_attack.damage
            if target.hp < 0:
                target.hp = 0
            print(
                f"{self.name} used {chosen_attack.name} and dealt {chosen_attack.damage} damage! {target.name}'s Remaining HP: {target.hp} / {target.max_hp} ")
            print("")
            time.sleep(1)

    def heal(self, chosen_ability):
        self.hp += chosen_ability.hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} used {chosen_ability.name} and healed {chosen_ability.hp}! {self.name}'s Remaining HP: {self.hp} / {self.max_hp}")

    def gain_xp(self, amount):
        xp += amount


class Attack:
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type
        self.damage = damage


class Ability:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def battle(player, enemy):
    player.hp = player.max_hp
    enemy.hp = enemy.max_hp
    counter = 1
    if player.speed > enemy.speed:
        first = player
    elif enemy.speed > player.speed:
        first = enemy
    else:
        first = random.choice([player, enemy])
    print(f"⚔️ {player.name} vs {enemy.name}!")
    print("🔥 The battle is about to begin!")
    print("")
    while enemy.hp > 0 and player.hp > 0:
        if counter > 1:
            if first == player:
                first = enemy
            elif first == enemy:
                first = player
        if first == player:
            print("""Your Pokémon is ready! 
Pick an attack and strike:""")
            count = 1
            for i in player.attacks:
                print(f"{count}. {i.name} (Type: {i.type}) (Damage = {i.damage})")
                count += 1
            print("=" * 40)
            time.sleep(1)
            while True:
                try:
                    attack_no = int(
                        input("Which attack do you choose? (number): "))
                    if attack_no >= 1 and attack_no <= len(player.attacks):
                        break
                    else:
                        print("Enter a valid number.")
                except ValueError:
                    print("Enter a number.")

            time.sleep(1)
            player.attack(player.attacks[attack_no - 1], enemy)
        else:
            enemy.attack(random.choice(enemy.attacks), player)
        counter += 1
    if enemy.hp == 0:
        print(f"""🏆  BATTLE WON!
{player.name} crushed the competition!""")
        print("=" * 40)
        print("")
        return "win"
    else:
        print(f""" ⚠️  BATTLE LOST!
{player.name} fainted… """)
        print("Train more and get stronger!")
        print("=" * 40)
        print("")
        return "loss"


def capture(battle, pokemon):
    if battle == "win":
        while True:
            store1 = input(f"Do you want to capture {pokemon.name}? (y/n) : ")
            if store1 == "y":
                success = random.choice([True, False])
                if success == True:
                    time.sleep(1)
                    print(("🎯 You throw a Pokéball at the wild Pokémon!"))
                    time.sleep(3)
                    print("✨ The Pokéball opens with a flash of light...")
                    time.sleep(3)
                    print("⚡ The wild Pokémon is pulled inside!")
                    time.sleep(3)
                    print("The Pokéball starts to shake...")
                    time.sleep(3)
                    print("🎉 Gotcha! The Pokémon was caught!")
                    time.sleep(3)
                    pokedex.append(pokemon)
                    return "caught"
                else:
                    print(("🎯 You throw a Pokéball at the wild Pokémon!"))
                    time.sleep(3)
                    print("✨ The Pokéball opens with a flash of light...")
                    time.sleep(3)
                    print("⚡ The wild Pokémon is pulled inside!")
                    time.sleep(3)
                    print("The Pokéball starts to shake...")
                    time.sleep(3)
                    print("💥 Oh no! The Pokémon broke free!")
                    time.sleep(3)
                    return "escaped"
            elif store1 == "n":
                time.sleep(1)
                print(
                    f"You chose not to capture {pokemon.name}. It escapes back into the wild.")
                return "not attempted"
            else:
                print("invalid input.")


Tail_Whip = Attack("Tail Whip", "Normal", 5)
Zap = Attack("Zap", "Electric", 8)
Scratch = Attack("Scratch", "Normal", 6)
Ember = Attack("Ember", "Fire", 9)
Tackle = Attack("Tackle", "Normal", 3)
Ripple = Attack("Ripple", "Water", 7)
Rock_Tomb = Attack("Rock Tomb", "Ground", 10)

Natures_Embrace = Ability("Nature's Embrace", 4)

Pichu = Pokemon("Pichu", "Electric", 15, 15, [Tail_Whip, Zap], [
                "Pichu", "Pikachu", "Raichu"], "Ground", 5, 0, 1, 10)
Charmander = Pokemon("Charmander", "Fire", 20, 20, [Scratch, Ember], [
                     "Charmander", "Charmeleon", "Charizard"], "Water", 3, 0, 1, 10)
Squirtle = Pokemon("Squirtle", "Water", 25, 25, [Tackle, Ripple], [
                   "Squirtle", "Wartortle", "Blastoise"], "Electric", 2, 0, 1, 10)
Pebbit = Pokemon("Pebbit", "Ground", 22, 22, [Tackle, Rock_Tomb], [
                 "Pebbit", "Gravit", "Seismite"], "Fire", 1, 0, 1, 10)

time.sleep(3)
print("=" * 40)
print("WELCOME TO POKÉMON: TEXT EDITION")
print("=" * 40)
time.sleep(1)
print("Choose your starter Pokémon:\n")

print("1. Pichu  (Electric)")
time.sleep(1)
print("2. Charmander  (Fire)")
time.sleep(1)
print("3. Squirtle  (Water)")
time.sleep(1)
print("4. Pebbit  (Ground)\n")
time.sleep(1)

while True:
    try:
        choice = int(input("Enter the number of your choice: "))
        break
    except ValueError:
        print("Enter a number.")

starters = {
    1: Pichu,
    2: Charmander,
    3: Squirtle,
    4: Pebbit
}

if choice in starters:
    player = starters[choice]
    pokedex.append(player)
else:
    print("Invalid input. You get Pichu by default.")
    player = Pichu

print("\n" + "-" * 40)
print(f"You chose {player.name}!")
print(f"Type: {player.type}")
print(f"HP: {player.hp}")
print("-" * 40)

enemy_pool = [Pichu, Charmander, Squirtle, Pebbit]
enemy_pool.remove(player)
enemy = random.choice(enemy_pool)

print(f"A wild {enemy.name} appeared!")
print(f"Type: {enemy.type}")
print(f"HP: {enemy.hp}")
print("-" * 40)

if player.weakness == enemy.type:
    print(
        f"⚠️  Careful! {enemy.name}'s {enemy.type} type is strong against {player.name}!")

while True:
    first_battle = battle(player, enemy)
    capture(first_battle, enemy)
    if first_battle == "win":
        break
    else:
        print("")
        print("=" * 40)
        print("TRY AGAIN!")
        print("=" * 40)
        print("")


lets_see = input("Did you like the game?")
