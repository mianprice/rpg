"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character(object):
    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def attack(self,enemy):
        enemy.health -= self.power
        print "%s does %d damage to %s" % (self.name, self.power, enemy.name)
        if enemy.isAlive() == False:
            print "%s is dead." % enemy.name

    def status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):
    def __init__(self, name, health, power):
        self.name = "Hero: %s" % name
        self.health = health
        self.power = power

class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = "Goblin: %s" % name
        self.health = health
        self.power = power

def main():
    hero1 = Hero("Hero 1",10,5)
    goblin1 = Goblin("Goblin 1",6,2)

    '''
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    '''

    while goblin1.isAlive() and hero1.isAlive():
        hero1.status()
        goblin1.status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            hero1.attack(goblin1)
            '''
            goblin1.health -= hero1.power
            print "You do %d damage to the goblin." % hero1.power
            if goblin1.health <= 0:
                print "The goblin is dead."
            '''
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin1.health > 0:
            # Goblin attacks hero
            goblin1.attack(hero1)
            '''
            hero1.health -= goblin1.power
            print "The goblin does %d damage to you." % goblin1.power
            if hero1.health <= 0:
                print "You are dead."
            '''

main()
