# You can use this workspace to write and submit your adventure game project.
import time
import random
import enum
global character
enemy = ["troll", "gorgon", "pirate", "wicked fairie", "dragon"]
weapon = []


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)


def enemy_character():
    global character
    character = random.choice(enemy)


def intro_print():
    # Things that happen at the beginning of the game.
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.", 2)
    print_pause(f"Rumor has it that a {character} is somewhere around here, "
                "and has been terrifying the nearby village.", 2)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n", 2)


def house_print():
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door "
                f"opens and out steps a {character}.", 2)
    print_pause(f"Eep! This is the {character}'s house!", 2)
    print_pause(f"The {character} attacks you!", 2)
    if "sword" not in weapon:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n", 2)


def cave_print():
    # Things that happen to the player goes in the cave
    if "sword" not in weapon:
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.", 2)
        print_pause("You walk back out to the field.\n", 2)
    else:
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.", 2)
        print_pause("You walk back out to the field.\n", 2)


def fight_print():
    # Things that happen when the player fights
    if "sword" not in weapon:
        print_pause("You do your best...", 2)
        print_pause(f"but your dagger is no match for the {character}.", 2)
        print_pause("You have been defeated!", 2)
    else:
        print_pause(f"As the {character} moves to attack, "
                    "you unsheath your new sword.", 2)
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.", 2)
        print_pause(f"But the {character} takes one look at "
                    "your shiny new toy and runs away!", 2)
        print_pause(f"You have rid the town of the {character}. "
                    "You are victorious!", 2)


def field_print():
    # Things that happen when the player runs back to the field
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n", 2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!', 2)


def fight():
    # Things that happen when the player fights or runs back to the field
    _ = valid_input("Would you like to (1) fight or (2) run away?", ["1", "2"])
    if _ == "1":
        fight_print()
        return True
    else:
        field_print()
        return False


def weapon_append():
    if "sword" not in weapon:
        weapon.append("sword")


def weapon_remove():
    if "sword" in weapon:
        weapon.remove("sword")


def play_again():
    play_again = valid_input("Would you like to play again? (y/n)", ["y", "n"])
    if play_again == "n":
        print_pause("Thanks for playing! See you next time.", 2)
        exit(0)
    else:
        print_pause("Excellent! Restarting the game...\n", 2)


def play_game():
    # Infinite loop
    while True:
        print_pause("Enter 1 to knock on the door of the house.", 2)
        print_pause("Enter 2 to peer into the cave.", 2)
        print_pause("What would you like to do?", 2)
        game_choice = valid_input("(Please enter 1 or 2.)\n", ["1", "2"])
        if game_choice == "1":
            house_print()
            if fight():
                break
        else:
            cave_print()
            weapon_append()


def game():
    # Infinite loop
    while True:
        # All logic to play
        weapon_remove()
        enemy_character()
        intro_print()
        play_game()
        # The stop condition.
        play_again()


if __name__ == '__main__':
    game()
