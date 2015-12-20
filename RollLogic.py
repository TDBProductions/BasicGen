import GlobalOptions
import PlayerClass
import random
# Input = None
# Output = StatsArray[ "STR","DEX","INT","CON","WIS","CHA" ]
def RollStats():
    StatsArray = []
    mercyRule = True

    while(mercyRule):
        for i in range(0, 6):
            StatsArray[i] = random.randint(1, 6) + random.randint(1,6) + random.randint(1, 6)
            mercyRule = MercyRule(StatsArray)
        return StatsArray

def MercyRule(StatsArray, globalOptions):
    if globalOptions.gameEdition == "Holmes":
        mercyRule = holmesMercyRule(StatsArray)
    elif globalOptions.gameEdition == "Moldvay":
        mercyRule = moldvayMercyRule(StatsArray)
    elif globalOptions.gameEdition == "Mentzer":
        mercyRule = mentzerMercyRule(StatsArray)
    return mercyRule

def holmesMercyRule():
    # No mercy
    # Mercy is for the weak
    return False

def moldvayMercyRule():
    i = 0
    for element in StatsArray:
        if element < 6:
            i = i + 1
        if i >= 2:
            return True
    if max(StatsArray) < 9:
        return True
    return False
   

def mentzerMercyRule():
    i = 0
    for element in StatsArray:
        if element < 6:
            i = i + 1
        if i >= 2:
            return True
    if max(StatsArray) < 9:
        return True
    return False


def main():
    globalOptions = GlobalOptions("Moldvay")
    StatsArray = RollStats(globalOptions)
    print(StatsArray)


if __name__ == "__main__": main()
