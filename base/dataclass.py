class Country:
    def __init__(self, name: str, population: int, continent: str, official_lang: str):
        self.name = name
        self.population = population
        self.continent = continent
        self.official_lang = official_lang


smallestEurope = Country("Monaco", 37623, "Europe")
smallestAsia= Country("Maldives", 552595, "Asia")
smallestAfrica= Country("Gambia", 2521126, "Africa")


from dataclasses import dataclass, field

@dataclass
class Country:
     name: str
     population: int
     continent: str
     official_lang: str = field(init=False) #Do not pass in this attribute in the constructor argument


smallestEurope = Country("Monaco", 37623, "Europe", "English") #But you did, so error!

print(smallestEurope)