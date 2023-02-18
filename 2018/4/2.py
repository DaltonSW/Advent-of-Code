import re
import time
import datetime
import aocd
import os


class Date:
    def __init__(self, month, day, guardNum, startHour, startMinute):
        self.month = int(month)
        self.day = int(day)
        self.guard = guardNum
        self.sleepRanges = []
        self.minutesAsleep = 0
        self.startHour = startHour
        self.startMinute = startMinute

    def calcMinutesAsleep(self) -> int:
        for sleep in self.sleepRanges:
            dur = sleep[1] - sleep[0]
            self.minutesAsleep += dur.total_seconds() // 60
        return self.minutesAsleep


class Elf:
    def __init__(self, num):
        self.num = num
        self.datesWorked = []
        self.totalMinutesAsleep = 0

    def calcTotalMinutesAsleep(self) -> int:
        for date in self.datesWorked:
            self.totalMinutesAsleep += date.calcMinutesAsleep()

        return self.totalMinutesAsleep

    def analyzeMinutesSlept(self) -> (int, int, int):
        minutes = {}
        for date in self.datesWorked:
            for timeRange in date.sleepRanges:
                for i in range(timeRange[0].minute, timeRange[1].minute):
                    if i in minutes:
                        minutes[i] += 1
                    else:
                        minutes[i] = 1

        largest = [-1, -1]
        for key in minutes.keys():
            if minutes[key] > largest[0]:
                largest[1] = key
                largest[0] = minutes[key]
        return largest[1], self.num, largest[0]


def main():
    cwd = os.getcwd().split('\\')
    data = aocd.get_data(None, int(cwd[-1]), int(cwd[-2]))

    testData = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

    notes = data.split('\n')
    notes.sort()

    elves = {}
    elvesSleeping = {}
    dates = []
    curDate = None

    i = 0
    while i < len(notes):
        note = notes[i]
        noteDate = re.search(r'\d\d\d\d-\d\d-\d\d', note).group(0)
        noteTime = re.search(r'\d\d:\d\d', note).group(0)
        noteYear, noteMonth, noteDay = noteDate.split('-')
        noteHour, noteMinute = noteTime.split(':')
        if "begins" in note:
            guardNum = re.search(r'#\d+', note).group(0)[1:]
            newDate = Date(noteMonth, int(noteDay) + 1 if noteHour == '23' else noteDay, int(guardNum), noteHour, noteMinute)
            dates.append(newDate)
            curDate = newDate
            i += 1

        else:
            sleepStart = datetime.datetime(day=int(noteDay), month=int(noteMonth), year=int(noteYear), hour=int(noteHour), minute=int(noteMinute))
            i += 1
            newNote = notes[i]
            newNoteDate = re.search(r'\d\d\d\d-\d\d-\d\d', newNote).group(0)
            newNoteYear, newNoteMonth, newNoteDay = newNoteDate.split('-')
            newNoteTime = re.search(r'\d\d:\d\d', newNote).group(0)
            newNoteHour, newNoteMinute = newNoteTime.split(':')
            sleepEnd = datetime.datetime(day=int(newNoteDay), month=int(newNoteMonth), year=int(newNoteYear), hour=int(newNoteHour), minute=int(newNoteMinute))
            curDate.sleepRanges.append((sleepStart, sleepEnd))
            i += 1

    del cwd, data, note, notes, curDate
    del guardNum, newDate, newNote, noteDay, noteDate, noteTime, noteHour
    del noteMinute, noteMonth, sleepStart, sleepEnd, i

    for date in dates:
        if date.guard not in elves:
            elf = Elf(date.guard)
            elf.datesWorked.append(date)
            elves[date.guard] = elf

        else:
            elves[date.guard].datesWorked.append(date)

    mostTimes = 0
    biggestOverall = [-1, -1]
    for elf in elves.values():
        biggest, elf, numTimes = elf.analyzeMinutesSlept()
        elvesSleeping[biggest] = elf
        if numTimes > mostTimes:
            mostTimes = numTimes
            biggestOverall = [biggest, elf]

    print(biggestOverall[0] * biggestOverall[1])


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
