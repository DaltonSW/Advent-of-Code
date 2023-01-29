import time


class Item:
    def __init__(self, name: str, cost: int, attack: int, defense: int) -> None:
        self.name = name
        self.cost = cost
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f"{self.name} - ${self.cost} for A +{self.attack}, D +{self.defense}"


class Fighter:
    def __init__(self, hp: int, attack: int, defense: int) -> None:
        self.HP = hp
        self.maxHP = hp
        self.attack = attack
        self.defense = defense
        self.items = []

    def reset(self, who: str):
        match who:
            case "Boss":
                self.HP = 109
                self.attack = 8
                self.defense = 2
            case "Hero":
                self.HP = 100
                self.attack = 0
                self.defense = 0

    def addItem(self, item: Item) -> None:
        self.items.append(item)
        self.attack += item.attack
        self.defense += item.defense

    # returns whether this hit killed the fighter
    def takeDamage(self, attacker, defenderName: str) -> bool:
        damage = attacker.attack - self.defense
        self.HP -= max(damage, 1)
        print(f"{defenderName} took {damage} damage, HP is now {self.HP}")
        return self.HP <= 0


def main():
    weapons = [
        Item("Dagger", 8, 4, 0),
        Item("Shortsword", 10, 5, 0),
        Item("Warhammer", 25, 6, 0),
        Item("Longsword", 40, 7, 0),
        Item("Greataxe", 74, 8, 0)
    ]

    armors = [
        Item("Leather", 13, 0, 1),
        Item("Chainmail", 31, 0, 2),
        Item("Splint Mail", 53, 0, 3),
        Item("Banded Mail", 75, 0, 4),
        Item("Platemail", 102, 0, 5)
    ]

    rings = [
        Item("Damage +1", 25, 1, 0),
        Item("Damage +2", 50, 2, 0),
        Item("Damage +3", 100, 3, 0),
        Item("Defense +1", 20, 0, 1),
        Item("Defense +2", 40, 0, 2),
        Item("Defense +3", 80, 0, 3)
    ]

    # Puzzle Input
    boss = Fighter(109, 8, 2)
    hero = Fighter(100, 0, 0)
    victories = []

    for weapon in weapons:
        for gettingArmor in [False, True]:
            if gettingArmor:
                for armor in armors:
                    for oneRing in [False, True]:
                        if oneRing:
                            for ringOne in rings:
                                for twoRings in [False, True]:
                                    if twoRings:
                                        for ringTwo in rings:
                                            if ringOne == ringTwo:
                                                continue
                                            elif fight(hero, boss, weapon, armor, ringOne, ringTwo):
                                                victories.append((weapon, armor, ringOne, ringTwo))
                                    else:
                                        if fight(hero, boss, weapon, armor, ringOne, None):
                                            victories.append((weapon, armor, ringOne, None))
                        else:
                            if fight(hero, boss, weapon, armor, None, None):
                                victories.append((weapon, armor, None, None))

            else:
                for oneRing in [False, True]:
                    if oneRing:
                        for ringOne in rings:
                            for twoRings in [False, True]:
                                if twoRings:
                                    for ringTwo in rings:
                                        if ringOne == ringTwo:
                                            continue
                                        elif fight(hero, boss, weapon, None, ringOne, ringTwo):
                                            victories.append((weapon, None, ringOne, ringTwo))
                                else:
                                    if fight(hero, boss, weapon, None, ringOne, None):
                                        victories.append((weapon, None, ringOne, None))
                    else:
                        if fight(hero, boss, weapon, None, None, None):
                            victories.append((weapon, None, None, None))

    # remaining code here

    bestCost = 400
    for victory in victories:
        cost = 0
        for item in victory:
            if item is not None:
                cost += item.cost
        if cost < bestCost:
            bestCost = cost

    print(bestCost)


def fight(hero: Fighter, boss: Fighter, weapon: Item, armor: Item | None, ring1: Item | None,
          ring2: Item | None) -> bool:
    items = [weapon]
    hero.reset("Hero")
    hero.addItem(weapon)
    if armor:
        items.append(armor)
        hero.addItem(armor)
    if ring1:
        items.append(ring1)
        hero.addItem(ring1)
    if ring2:
        items.append(ring2)
        hero.addItem(ring2)

    for item in items:
        print(item.name)

    boss.reset("Boss")

    while True:
        if boss.takeDamage(hero, "Boss"):
            print("\tWin!")
            return True
        elif hero.takeDamage(boss, "Hero"):
            print("\tLoss!")
            return False


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
