class Animal(object):
    def __init__(self, name, species, gender, age, energy, companions, status):
        self.name = name #string
        self.species = species #string: cat/dog/rabbit/bird
        self.gender = gender #string: male/female
        self.age = age #list of floats: [years, months]
        self.energy = energy #string: hign/medium/low
        self.companions = companions #list of strings:cat/dog/rabbit/bird
        self.status = status # string: "getting ready"/"available"/"on hold"/"adopted"

    def list_age(self):
        if self.age[0] > 0 and self.age[1] > 0:
            return str(self.age[0]) + " year and " + str(self.age[1]) + " month old"
        elif self.age[0] > 0:
            return str(self.age[0]) + " year old"
        else:
            return str(self.age[1]) + " month old"

    def recommend_companions(self):
        if self.companions == "none":
            return "prefers to live in a house with only human companions"
        else:
            return "gets along with " + self.companions


    def describe(self):
        description = self.name
        description += " is a " + self.energy + "-energy, " 
        description += self.list_age() + " " + self.gender + " " + self.species 
        description += ", who " + self.recommend_companions() + "."
        return description
