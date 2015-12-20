import GlobalOptions
import PlayerClass
import random
# Input = None
# Output = StatsArray[ "STR","DEX","INT","CON","WIS","CHA" ]
def RollStats(globalOptions):
    mercyRule = True

    while(mercyRule):
        StatsArray = []
        for i in range(0, 6):
            StatsArray.append( (random.randint(1, 6) + random.randint(1,6) + random.randint(1, 6)) )
            mercyRule = MercyRule(StatsArray, globalOptions)
        return StatsArray

def MercyRule(StatsArray, globalOptions):
    if globalOptions.GameEdition == "Holmes":
        mercyRule = holmesMercyRule(StatsArray)
    elif globalOptions.GameEdition == "Moldvay":
        mercyRule = moldvayMercyRule(StatsArray)
    elif globalOptions.GameEdition == "Mentzer":
        mercyRule = mentzerMercyRule(StatsArray)
    return mercyRule

def holmesMercyRule(StatsArray):
    # No mercy
    # Mercy is for the weak
    return False

def moldvayMercyRule(StatsArray):
    i = 0
    for element in StatsArray:
        if element < 6:
            i = i + 1
        if i >= 2:
            return True
    if max(StatsArray) < 9:
        return True
    return False
   

def mentzerMercyRule(StatsArray):
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
    globalOptions = GlobalOptions.GlobalOptions("Moldvay")
    StatsArray = RollStats(globalOptions)
    print(StatsArray)


if __name__ == "__main__": main()
