import random
first_name = ["Agent", "Brave", "Captain", "Detective", "Emerald", "Flying", "Great", "Harrowing", "Invisible", "Shadow", "Kinetic", "Doctor", "Mighty", "Night", "Wave", "Professor", "Quick", "Rebellious", "Super", "Thunder", "Ultra", "Mega", "Wonder", "Water", "Astro", "Steel", "Dark"]

second_name = ["Knight", "Shock", "Bandit", "Thunderbolt", "Avenger", "Justice", "Master", "Falcon", "Shield", "Ninja", "Mutant", "Hero", "Witch", "Rider", "Shark", "Thunder", "Slider", "Guardian", "Phanthom", "Surfer", "Oracle"]

super_power = ["Flight", "Invisibility", "Armor", "Gadgets", "Speed", "Genius", "Stretching", "Strength", "Teleportation", "Invincibility", "Shapeshifting", "X-Ray Vision", "Energy", "Telekinesis", "Robotics", "Fire Power", "Water Power"]

random_first = random.choice(first_name)
random_second = random.choice(second_name)
random_power = random.choice(super_power)

print(f"Your Superhero name is {random_first} {random_second} and your super power is {random_power}!")