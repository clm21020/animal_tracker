from humane_society import HumaneSociety
from animal import Animal

lulz = Animal("Lulz", "cat", "female", [1,1], "medium", "Rofler", "adopted")
rofler = Animal("Rofler", "cat", "male", [1,0], "high", "Lulz", "adopted")
polly = Animal("Polly", "bird", "female", [4,0], "low", "birds", "available")
latte = Animal("Latte", "cat", "female", [2,0], "medium", "cats", "on hold")
non_latte = Animal("Non-Latte", "cat", "male", [2,0], "low", "cats", "on hold")
jordan = Animal("Jordan", "dog", "male", [5,0], "medium", "dogs and cats", "getting_ready")
emma = Animal("Emma", "dog", "female", [2,6], "high", "dogs and cats", "getting_ready")
floppy = Animal("Floppy", "rabbit", "female", [2,0], "low", "birds, rabbits, cats, and dogs", "available")
lone_wolf = Animal("Lone Wolf", "dog", "male", [6,0], "high", "none", "available")


palo_alto_hs = HumaneSociety("Palo Alto Humane Society", "Palo Alto", "CA")
palo_alto_hs.add_animals([lulz, rofler, polly, latte, non_latte, jordan, emma, floppy])
palo_alto_hs.add_animal(lone_wolf)


palo_alto_hs.find_companions("cat")

"""
for animal in palo_alto_hs.animals:
    print(animal.describe())

palo_alto_hs.get_species(["bird", "rabbit"])

print(lulz.describe())
print(rofler.describe())

"""