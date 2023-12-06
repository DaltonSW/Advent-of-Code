import time
import aocd
import os
import re


def main():
    cwd = os.getcwd().split('\\')
    data: str = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))
    # print(data)

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

    dataLines: list[str] = data.split('\n\n')

    seedsString = dataLines[0]
    seedToSoilString = dataLines[1]
    soilToFertString = dataLines[2]
    fertToWaterString = dataLines[3]
    waterToLightString = dataLines[4]
    lightToTempString = dataLines[5]
    tempToHumidString = dataLines[6]
    humidToLocString = dataLines[7]

    del dataLines, data, cwd

    seeds = map(int, re.findall('\\d+', seedsString))

    print("Beginning mapping...")
    seedToSoilMap = parseMapping(seedToSoilString)
    print("Mapped seeds to soil")
    soilToFertMap = parseMapping(soilToFertString)
    print("Mapped soil to fertilizer")
    fertToWaterMap = parseMapping(fertToWaterString)
    print("Mapped fertilizer to water")
    waterToLightMap = parseMapping(waterToLightString)
    print("Mapped water to light")
    lightToTempMap = parseMapping(lightToTempString)
    print("Mapped light to temp")
    tempToHumidMap = parseMapping(tempToHumidString)
    print("Mapped temp to humidity")
    humidToLocMap = parseMapping(humidToLocString)
    print("Mapped humidity to location")

    del seedToSoilString, soilToFertString, fertToWaterString, waterToLightString, lightToTempString, tempToHumidString, humidToLocString

    for seed in seeds:
        soil = seedToSoilMap[seed] if seed in seedToSoilMap else seed
        fert = soilToFertMap[soil] if soil in soilToFertMap else soil
        water = fertToWaterMap[fert] if fert in fertToWaterMap else fert
        light = waterToLightMap[water] if water in waterToLightMap else water
        temp = lightToTempMap[light] if light in lightToTempMap else light
        humid = tempToHumidMap[temp] if temp in tempToHumidMap else temp
        loc = humidToLocMap[humid] if humid in humidToLocMap else humid

        print(f"Seed {seed} goes in location {loc}")

def parseMapping(mapping: str) -> dict[int, int]:
    lines = mapping.split('\n')
    lines.pop(0)
    mappingDict = {}
    for line in lines:
        destStart, sourceStart, rangeLen = map(int, re.findall('\\d+', line))
        dest = destStart
        source = sourceStart
        while rangeLen > 0:
            mappingDict[source] = dest
            rangeLen -= 1
            dest += 1
            source += 1

    return mappingDict

starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
