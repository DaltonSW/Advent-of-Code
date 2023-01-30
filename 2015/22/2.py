import time
from copy import deepcopy


class Spell:
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost


spells = {
    "Magic Missile": Spell("Magic Missile", 53),
    "Drain": Spell("Drain", 73),
    "Shield": Spell("Shield", 113),
    "Poison": Spell("Poison", 173),
    "Recharge": Spell("Recharge", 229)
}


class Boss:
    def __init__(self, hp: int, attack: int) -> None:
        self.hp = hp
        self.attack = attack

        self.poisonTurns = 0


class Hero:
    def __init__(self, hp: int, mana: int) -> None:
        self.hp = hp
        self.mana = mana

        self.rechargeTurns = 0
        self.shieldTurns = 0


WINS = {}
BEST_SCORE = 999999999


def main():
    global WINS
    bossHealth = 51
    bossAttack = 9

    heroHealth = 50
    heroMana = 500

    for spell in spells.values():
        boss = Boss(bossHealth, bossAttack)
        hero = Hero(heroHealth, heroMana)

        print(f"Playing starting spell: {spell.name}")

        play(boss, hero, spell)

    wins = []
    for key in WINS.keys():
        wins.append(key)

    wins.sort()
    print(wins)


def play(boss: Boss, hero: Hero, spell: Spell, manaSpent: int = 0):
    global WINS, BEST_SCORE
    if manaSpent > BEST_SCORE:
        return

    # Hard Mode
    hero.hp -= 1
    if hero.hp <= 0:
        return

    # Apply Effects
    if hero.shieldTurns > 0:
        hero.shieldTurns -= 1

    if hero.rechargeTurns > 0:
        hero.mana += 101
        hero.rechargeTurns -= 1

    if boss.poisonTurns > 0:
        boss.hp -= 3
        if boss.hp <= 0:
            WINS[manaSpent] = 1
            if manaSpent < BEST_SCORE:
                BEST_SCORE = manaSpent
            return
        boss.poisonTurns -= 1

    # Cast spell
    manaSpent += spell.cost
    hero.mana -= spell.cost

    # Execute spell action
    match spell.name:
        case "Magic Missile":
            boss.hp -= 4
            if boss.hp <= 0:
                WINS[manaSpent] = 1
                if manaSpent < BEST_SCORE:
                    BEST_SCORE = manaSpent
                return

        case "Drain":
            hero.hp += 2
            boss.hp -= 2
            if boss.hp <= 0:
                WINS[manaSpent] = 1
                if manaSpent < BEST_SCORE:
                    BEST_SCORE = manaSpent
                return

        case "Shield":
            if hero.shieldTurns > 1:
                return
            hero.shielded = True
            hero.shieldTurns = 6

        case "Poison":
            if boss.poisonTurns > 1:
                return
            boss.poisoned = True
            boss.poisonTurns = 6

        case "Recharge":
            if hero.rechargeTurns > 1:
                return
            hero.recharging = True
            hero.rechargeTurns = 5

    if hero.shieldTurns > 0:
        hero.shieldTurns -= 1

    if hero.rechargeTurns > 0:
        hero.mana += 101
        hero.rechargeTurns -= 1

    if boss.poisonTurns > 0:
        boss.hp -= 3
        if boss.hp <= 0:
            WINS[manaSpent] = 1
            if manaSpent < BEST_SCORE:
                BEST_SCORE = manaSpent
            return
        boss.poisonTurns -= 1

    if hero.shieldTurns > 0:
        hero.hp -= max(boss.attack - 7, 1)
    else:
        hero.hp -= boss.attack

    if hero.hp <= 0:
        return

    for spell in spells.values():
        if spell.cost > hero.mana:
            continue
        heroState = deepcopy(hero)
        bossState = deepcopy(boss)
        play(boss, hero, spell, manaSpent)
        hero = deepcopy(heroState)
        boss = deepcopy(bossState)

    return


starttime = time.time()
main()
endtime = time.time()

print("Runtime: {} seconds".format(round(endtime - starttime, 3)))
