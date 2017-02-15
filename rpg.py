"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

'''
Base Character class
'''
class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

'''
Playable Character Classes
'''
class Hero(Character):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.power = 5
        self.coins = 20

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        doubleCheck = random.random() < 0.2
        if doubleCheck:
            print "Critical strike!"
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

class Tallahassee(Character):
    def __init__(self):
        self.name = "Tallahassee"
        self.health = 10
        self.power = 5
        self.coins = 20

    def attack(self, enemy):
        if not self.alive():
            return
        if enemy.name != 'zombie':
            print "%s attacks %s" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
            time.sleep(1.5)
        else:
            print "It's time for the zombie kill of the week!"
            enemy.receive_damage(True)
            time.sleep(1.5)

class Achilles(Character):
    def __init__(self):
        self.name = "Achilles"
        self.health = 1
        self.power = 10
        self.coins = 20

    def receive_damage(self, points):
        doubleCheck = random.random() < 0.001
        if doubleCheck:
            self.health -= points
        else:
            points = 0
            print "The attack missed Achilles' heel!"
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

'''
Enemy character Classes
'''
class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.recuperate_amount = 2

    def recuperate(self):
        self.health += self.recuperate_amount
        print "%s recuperated %d health." % (self.name, self.recuperate_amount)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        doubleCheck = random.random() < 0.2
        if doubleCheck:
            self.recuperate()
        if self.health <= 0:
            print "%s is dead." % self.name

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        if not self.alive():
            return
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5

    def receive_damage(self, points):
        doubleCheck = random.random() < 0.1
        if doubleCheck:
            self.health -= points
        else:
            points = 0
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 1
        self.power = 1
        self.isDead = False

    def receive_damage(self,points):
        if type(points) == bool:
            self.isDead = True
            print "%s is dead." % self.name
        else:
            print "%s didn't take any damage!" % self.name

    def alive(self):
        return not self.isDead

'''
Battle Engine
'''
class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

'''
Store Engine
'''
class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

'''
Setup and Main Loop
'''
heroType = raw_input("What is your hero's name?")
if heroType == "Tallahassee":
    hero = Tallahassee()
elif heroType == "Achilles":
    hero = Achilles()
else:
    hero = Hero(heroType)
enemies = [Zombie(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    if enemies.index(enemy) < len(enemies)-1:
        shopping_engine.do_shopping(hero)

print "YOU WIN!"
