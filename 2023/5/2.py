import time
import aocd
import os
import re
import multiprocessing
from functools import partial
from numba import jit, cuda


# Submitted Answers:
# 1159584779 -- Too high
# 566850516 --- Too high
#
# 79753136
# 63179500 !!!!!!! LET'S GOOOOOOOO

# (20816377,617524635)    -- 596,708,258
# (763445965,842016187)   -- 78,570,222
# (950268560,961719847)   -- 11,451,287 ---> 1159584779
# (1047354752,1067548613) -- 20,193,861 ---> 3802688341
# (1157620425,1693541361) -- 535,920,936
# (1693788857,1840468927) -- 146,680,070
# (2130924847,2404967104) -- 274,042,257
# (3187993807,3368066300) -- 180,072,493
# (3503767450,3686233401) -- 182,465,951
# (3760349291,4026018332) -- 265,669,041

# (20816377,617524635)
# (763445965,842016187)
# (950268560,961719847)
# (1047354752,1067548613)
# (1157620425,1693541361)
# (1693788857,1840468927)
# (2130924847,2404967104)
# (3187993807,3368066300)
# (3503767450,3686233401)
# (3760349291,4026018332)

def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    # print(data)

    dataLines: list[str] = data.split('\n\n')

    # seedsString = dataLines[0]
    seedToSoil = stringToList(dataLines[1])
    soilToFert = stringToList(dataLines[2])
    fertToWater = stringToList(dataLines[3])
    waterToLight = stringToList(dataLines[4])
    lightToTemp = stringToList(dataLines[5])
    tempToHumid = stringToList(dataLines[6])
    humidToLoc = stringToList(dataLines[7])

    del dataLines, data, cwd

    seedPairs = [
        [763445965, 78570222],
        [1693788857, 146680070],
        [1157620425, 535920936],
        [3187993807, 180072493],
        # [1047354752, 20193861],
        [2130924847, 274042257],
        [20816377, 596708258],
        # [950268560, 11451287],
        [3503767450, 182465951],
        [3760349291, 265669041]
    ]

    seedRanges = [(20816377, 43734120),
                  (43734120, 66651863),
                  (66651863, 89569606),
                  (89569606, 112487349),
                  (112487349, 135405092),
                  (135405092, 158322835),
                  (158322835, 181240578),
                  (181240578, 204158321),
                  (204158321, 227076064),
                  (227076064, 249993807),
                  # (249993807, 272911550), --> 896826631
                  (272911550, 295829293),
                  (295829293, 318747036),
                  (318747036, 341664779),
                  (341664779, 364582522),
                  (364582522, 387500265),
                  (387500265, 410418008),
                  (410418008, 433335751),
                  (433335751, 456253494),
                  (456253494, 479171237),
                  (479171237, 502088980),
                  (502088980, 525006723),
                  # (525006723, 547924466), --> 63179500
                  (547924466, 570842209),
                  # (570842209, 593759952), --> 2851229369
                  (593759952, 616677695),
                  # (616677695, 617524635), --> 2965934053
                  # (763445965, 786363708), --> 79753136
                  # (786363708, 809281451), --> 98314674
                  (809281451, 832199194),
                  # (832199194, 842016187), --> 566850516
                  # (950268560, 961719847),
                  # (1047354752, 1067548613),
                  (1157620425, 1180538168),
                  # (1180538168, 1203455911), --> 2792767328
                  (1203455911, 1226373654),
                  # (1226373654, 1249291397), --> 3296297795
                  (1249291397, 1272209140),
                  (1272209140, 1295126883),
                  (1295126883, 1318044626),
                  (1318044626, 1340962369),
                  (1340962369, 1363880112),
                  # (1363880112, 1386797855), --> 3181277378
                  (1386797855, 1409715598),
                  (1409715598, 1432633341),
                  (1432633341, 1455551084),
                  # (1455551084, 1478468827), --> 231223663
                  (1478468827, 1501386570),
                  (1501386570, 1524304313),
                  (1524304313, 1547222056),
                  (1547222056, 1570139799),
                  (1570139799, 1593057542),
                  (1593057542, 1615975285),
                  (1615975285, 1638893028),
                  (1638893028, 1661810771),
                  (1661810771, 1684728514),
                  (1684728514, 1693541361),
                  (1693788857, 1716706600),
                  (1716706600, 1739624343),
                  (1739624343, 1762542086),
                  (1762542086, 1785459829),
                  (1785459829, 1808377572),
                  (1808377572, 1831295315),
                  (1831295315, 1840468927),
                  (2130924847, 2153842590),
                  (2153842590, 2176760333),
                  (2176760333, 2199678076),
                  (2199678076, 2222595819),
                  (2222595819, 2245513562),
                  (2245513562, 2268431305),
                  (2268431305, 2291349048),
                  (2291349048, 2314266791),
                  (2314266791, 2337184534),
                  (2337184534, 2360102277),
                  (2360102277, 2383020020),
                  (2383020020, 2404967104),
                  (3187993807, 3210911550),
                  (3210911550, 3233829293),
                  (3233829293, 3256747036),
                  (3256747036, 3279664779),
                  (3279664779, 3302582522),
                  (3302582522, 3325500265),
                  (3325500265, 3348418008),
                  (3348418008, 3368066300),
                  (3503767450, 3526685193),
                  (3526685193, 3549602936),
                  (3549602936, 3572520679),
                  (3572520679, 3595438422),
                  (3595438422, 3618356165),
                  (3618356165, 3641273908),
                  (3641273908, 3664191651),
                  (3664191651, 3686233401),
                  (3760349291, 3783267034),
                  (3783267034, 3806184777),
                  (3806184777, 3829102520),
                  (3829102520, 3852020263),
                  (3852020263, 3874938006),
                  (3874938006, 3897855749),
                  (3897855749, 3920773492),
                  (3920773492, 3942691235)]

    stringMappings = [seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHumid, humidToLoc]

    pool = multiprocessing.Pool()
    funcRun = partial(processRange, stringMappings=stringMappings)
    pool.map(funcRun, seedRanges)


def processRange(rangeData: list[int], stringMappings):
    # startSeed, length = rangeData
    startSeed, endSeed = rangeData[0], rangeData[1]
    print(f"Checking {startSeed} -> {endSeed}")
    lowestLocation = -1
    for seed in range(startSeed, endSeed + 1):
        soil = mapSourceToDest(seed, stringMappings[0])
        fert = mapSourceToDest(soil, stringMappings[1])
        water = mapSourceToDest(fert, stringMappings[2])
        light = mapSourceToDest(water, stringMappings[3])
        temp = mapSourceToDest(light, stringMappings[4])
        humid = mapSourceToDest(temp, stringMappings[5])
        loc = mapSourceToDest(humid, stringMappings[6])
        if lowestLocation == -1:
            lowestLocation = loc
        else:
            if loc < lowestLocation:
                lowestLocation = loc

    print(f"Range {startSeed} -> {endSeed} : {lowestLocation}")


def mapSourceToDest(source: int, mappings: list[str]) -> int:
    for mapping in mappings:
        destStart, sourceStart, rangeLen = map(int, re.findall('\\d+', mapping))
        if source < sourceStart or source > (sourceStart + rangeLen):
            continue
        return destStart + source - sourceStart

    return source


def stringToList(mapString: str) -> list[str]:
    lines = mapString.split('\n')
    lines.pop(0)
    return lines


if __name__ == '__main__':
    starttime = time.time()
    main()
    endtime = time.time()

    print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
