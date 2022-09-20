from classes.Character import Character


class Player:
    name: str
    main: Character
    alt: int

    def __init__(self, name, main, alt = 0):
        self.name = name
        self.main = main
        self.alt = alt
