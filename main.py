import random
initial_adjective = ["Agent", "Brave", "Captain", "Detective", "Evil", "Flying", "Great", "Harrowing", "Invisible", "Jumping", "Kinetic", "Lanky", "Mighty", "Night", "Outlandish", "Professor", "Quick", "Rebellious", "Super", "Thunder", "Ultra", "Viscious", "Wonder", "X-Ray", "Youthful", "Zany"]

second_adjective = ["Knight", "Shock", "Bandit", "Thunderbolt", "Avenger", "Justice", "Master", "Falcon", "Shield", "Ninja", "Mutant", "Hero"]

random_first = random.choice(initial_adjective)
random_second = random.choice(second_adjective)

print(f"You're Superhero name is {random_first} {random_second}!")