class Character(object):
    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def attack(self,enemy):
        if enemy.type == 'Zombie':
            print "%s cannot damage %s" % (self.name, enemy.name)
        else:
            enemy.health -= self.power
            print "%s does %d damage to %s" % (self.name, self.power, enemy.name)
        if enemy.isAlive() == False:
            print "%s is dead." % enemy.name

    def status(self):
        if type(self.health) == int:
            printstring = "%s: %s has %d health and %d power." % (self.type,self.name, self.health, self.power)
        else:
            printstring = "%s: %s has %s health and %d power." % (self.type,self.name, self.health, self.power)
        print printstring


class Hero(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.type = 'Hero'

class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.type = 'Goblin'

class Zombie(Character):
    def __init__(self, name, power):
        self.name = name
        self.health = "infinite"
        self.power = power
        self.type = 'Zombie'

    def isAlive(self):
        return True

def main():
    player = Hero("Hero 1",10,5)
    enemy1 = Zombie("Zombie 1",2)

    while enemy1.isAlive() and player.isAlive():
        player.status()
        enemy1.status()
        print
        print "What do you want to do?"
        print "1. Fight %s: %s" % (enemy1.type, enemy1.name)
        print "2. Do nothing"
        print "3. Flee"
        print "> ",
        input = raw_input()
        if input == "1":
            player.attack(enemy1)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input
        if enemy1.isAlive():
            enemy1.attack(player)

main()
