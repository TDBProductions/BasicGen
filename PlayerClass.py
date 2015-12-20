class PlayerClass:
    def __init__(self, StatArray):
        self.STR = StatArray[0]
        self.DEX = StatArray[1]
        self.INT = StatArray[2]
        self.CON = StatArray[3]
        self.WIS = StatArray[4]
        self.CHA = StatArray[5]

class Fighter(PlayerClass):
    pass

class Thief(PlayerClass):
    pass

class Cleric(PlayerClass):
    pass

class MagicUser(PlayerClass):
    pass

class Elf(PlayerClass):
    pass

class Dwarf(PlayerClass):
    pass

class Halfling(PlayerClass):
    pass
