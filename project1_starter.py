"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage:
AI (ChatGPT) assisted with file read/write structure and stat formula design.
All code was reviewed and understood by the student.
"""

import os  # used to check if file exists or directory validity

# =============================
# Character Creation Functions
# =============================

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)
    """
    character_class = character_class.lower()

    if character_class == "warrior":
        strength = 10 + (level * 3)
        magic = 3 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "mage":
        strength = 4 + (level * 1)
        magic = 12 + (level * 3)
        health = 80 + (level * 8)
    elif character_class == "rogue":
        strength = 7 + (level * 2)
        magic = 7 + (level * 2)
        health = 70 + (level * 7)
    elif character_class == "cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 2)
        health = 90 + (level * 9)
    else:
        strength = 0
        magic = 0
        health = 0

    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns a dictionary or None if invalid class.
    """
    valid_classes = ["warrior", "mage", "rogue", "cleric"]
    if character_class is None or name is None or name == "":
        print("Error: Invalid name or class.")
        return None
    if character_class.lower() not in valid_classes:
        print("Error: Invalid class. Choose Warrior, Mage, Rogue, or Cleric.")
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

    character = {
        "name": name,
        "class": character_class.capitalize(),
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


# =============================
# File Operations
# =============================

def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns True if successful, False otherwise.
    """
    if character is None or filename == "":
        return False

    # Check if directory exists before trying to write
    directory = os.path.dirname(filename)
    if directory != "" and not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return False

    with open(filename, "w") as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")

    return True


def load_character(filename):
    """
    Loads character from text file.
    Returns character dictionary if successful, or None if file missing.
    """
    if not os.path.isfile(filename):
        print("Error: File not found.")
        return None

    with open(filename, "r") as f:
        lines = f.readlines()

    character = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(": ", 1)
            key = key.lower().replace(" ", "_")
            character[key] = value

    # Convert numeric values
    for stat in ["level", "strength", "magic", "health", "gold"]:
        if stat in character:
            character[stat] = int(character[stat])

    return {
        "name": character.get("character_name", "Unknown"),
        "class": character.get("class", "Unknown"),
        "level": character.get("level", 1),
        "strength": character.get("strength", 0),
        "magic": character.get("magic", 0),
        "health": character.get("health", 0),
        "gold": character.get("gold", 0)
    }


# =============================
# Display & Level Up
# =============================

def display_character(character):
    """
    Prints formatted character sheet.
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("========================")


def level_up(character):
    """
    Increases character level and recalculates stats.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"{character['name']} leveled up to level {character['level']}!")


# =============================
# Optional Testing Area
# =============================

if __name__ == "__main__":
    print("=== CHARACTER CREATOR TEST ===")
    hero = create_character("Aria", "Mage")
    if hero:
        display_character(hero)
        save_character(hero, "aria.txt")
        loaded = load_character("aria.txt")
        print("\nLoaded from file:")
        display_character(loaded)
        level_up(hero)
        display_character(hero)

