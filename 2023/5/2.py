import time
import aocd
import os
import re
import multiprocessing
from functools import partial

# Submitted Answers:
# 1159584779 -- Too high

# Locations Returned:
# 1159584779
# 3802688341

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

# 30 equally sized ranges
# 1. (20816377, 97208856)
# 2. (97208856, 173601335)
# 3. (173601335, 249993814)
# 4. (249993814, 326386293)
# 5. (326386293, 402778772)
# 6. (402778772, 479171251)
# 7. (479171251, 555563730)
# 8. (555563730, 617524635)
# 9. (763445965, 839838444)
# 10. (839838444, 842016187)
# 11. (950268560, 961719847)
# 12. (1047354752, 1067548613)
# 13. (1157620425, 1234012904)
# 14. (1234012904, 1310405383)
# 15. (1310405383, 1386797862)
# 16. (1386797862, 1463190341)
# 17. (1463190341, 1539582820)
# 18. (1539582820, 1615975299)
# 19. (1615975299, 1692367778)
# 20. (1692367778, 1693541361)
# 21. (1693788857, 1770181336)
# 22. (1770181336, 1840468927)
# 23. (2130924847, 2207317326)
# 24. (2207317326, 2283709805)
# 25. (2283709805, 2360102284)
# 26. (2360102284, 2404967104)
# 27. (3187993807, 3264386286)
# 28. (3264386286, 3340778765)
# 29. (3340778765, 3368066300)
# 30. (3503767450, 3686233401)

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

    stringMappings = [seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHumid, humidToLoc]

    pool = multiprocessing.Pool(processes=10)
    funcRun = partial(processRange, stringMappings=stringMappings)
    pool.map(funcRun, seedPairs)

def processRange(rangeData: list[int], stringMappings):
    startSeed, length = rangeData
    print(f"Checking {startSeed} -> {startSeed + length}")
    lowestLocation = -1
    for seed in range(startSeed, startSeed + length + 1):
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

    print(f"Range {startSeed} -> {startSeed + length} : {lowestLocation}")


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
