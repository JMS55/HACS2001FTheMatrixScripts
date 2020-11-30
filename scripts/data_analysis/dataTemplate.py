import re
import copy

class Attack:
    def __init__(self):
        self.template = None
        self.data = ''
        self.ip = ''
        self.success = False
        self.noninteractiveCommand = ''
        self.shell = False

def getAttacks(logFile):
    # Parses the log10_.txt file
    file = open(logFile)
    attacks = []
    attack = Attack()
    inAttack = False
    for line in file:
        if (line.find('Using template') != -1):
            temp = re.match(r'Using [T|t]emplate: (\d{3})', line)
            if temp != None:
                inAttack = False
                attacks.append(copy.copy(attack))
                attack = Attack()
                attack.template = temp.groups()[0]
        elif (line.find ('Attacker connected') != -1 and inAttack == False):
            ip = re.search(r'Attacker connected: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line)
            if ip != None:
                attack.ip = ip.groups()[0]
                inAttack = True
        elif (line.find("Attacker authenticated and is inside container") != -1):
            attack.success = True
        elif (line.find("Attacker closed the connection") != -1 and attack.success == False):
            attack.ip = ''
            attack.data = ''
            inAttack = False
        elif (line.find("Noninteractive mode") != -1):
            command = re.search(r'Noninteractive mode attacker command: (.*)$',line)
            if command != None:
                attack.noninteractiveCommand = command
        elif (line.find("SHELL") != -1):
            attack.shell = True
        if inAttack:
            attack.data += line + '\n'
    return attacks

def printData(attacks):
    for attack in attacks:
        print(attack.data)

attacksTest = getAttacks('./testFile.txt')
printData(attacksTest)
