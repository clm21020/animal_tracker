class HumaneSociety(object):
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state
        self.animals = []

    def add_animal(self, solo_animal): #solo_animal should be a variable 
        self.animals.append(solo_animal)

    def add_animals(self, animal_list): #animal_list should be a list  
        self.animals.extend(animal_list)

    def get_species(self, desired_species): #species can be string or a list of strings
        for animal in self.animals:
            if animal.species in desired_species:
                print(animal.describe())

    def find_companions_for_species(self, species_to_match):
        matches = []
        for animal in self.animals:
            if species_to_match in animal.companions:
                matches.append(animal)
        return matches

    def find_companions_for_name(self, name):
        matches = []
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                animal_to_match = animal
                break
        for animal in self.animals:
            if animal.name.lower() != name.lower() and animal_to_match.species in animal.companions and animal.species in animal_to_match.companions:
                matches.append(animal)
        return matches


    def find_companions(self, species_or_name): #species_or_name is a string
        if species_or_name in ("cat", "cats", "dog", "dogs","rabbit", "rabbits", "bird", "birds"):
           matches = self.find_companions_for_species(species_or_name)
        else:
            matches = self.find_companions_for_name(species_or_name)
        if matches == []:
            print("The search returned no exact matches.")
        else:
            print("Potential matches for " + species_or_name + " include...")
            for match in matches:
                print(match.describe()) 

                

