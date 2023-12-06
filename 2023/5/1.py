import time
import aocd
import os
import re

def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

#     data = \
# """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""

    # print(data)

    dataLines: list[str] = data.split('\n\n')

    seedsString = dataLines[0]
    seedToSoil = stringToList(dataLines[1])
    soilToFert = stringToList(dataLines[2])
    fertToWater = stringToList(dataLines[3])
    waterToLight = stringToList(dataLines[4])
    lightToTemp = stringToList(dataLines[5])
    tempToHumid = stringToList(dataLines[6])
    humidToLoc = stringToList(dataLines[7])

    del dataLines, data, cwd

    seeds = map(int, re.findall('\\d+', seedsString))

    seedLocs: dict[int, int] = {}

    for seed in seeds:
        soil = mapSourceToDest(seed, seedToSoil)
        fert = mapSourceToDest(soil, soilToFert)
        water = mapSourceToDest(fert, fertToWater)
        light = mapSourceToDest(water, waterToLight)
        temp = mapSourceToDest(light, lightToTemp)
        humid = mapSourceToDest(temp, tempToHumid)
        loc = mapSourceToDest(humid, humidToLoc)
        seedLocs[seed] = loc

    lowestLocation = -1

    for seed in seedLocs:
        location = seedLocs[seed]
        if lowestLocation == -1:
            lowestLocation = location
        else:
            if location < lowestLocation:
                lowestLocation = location
        print(f"Seed {seed} -> loc {location}")

    print(f"Lowest location: {lowestLocation}")

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

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
