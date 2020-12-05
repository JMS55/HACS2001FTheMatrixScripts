import re
import copy

template_re = re.compile(r'Using [T|t]emplate: (\d{3})')
ip_re = re.compile(r'Attacker connected: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
command_re = re.compile(r'Noninteractive mode attacker command: (.*)$')

class Attack:
    def __init__(self):
        self.template = None
        self.data = ''
        self.ip = ''
        self.success = False
        self.noninteractiveCommand = ''
        self.isCat = False

# Returns an array of attack objects
def getAttacks(logFile):
    # Parses the log10_.txt file
    file = open(logFile)
    attacks = []
    attack = Attack()
    inAttack = False
    for line in file:
        if (line.find('Using template') != -1):
            temp = template_re.match(line)
            if temp != None:
                if inAttack and attack.success:
                    inAttack = False
                    attacks.append(copy.copy(attack))
                attack = Attack()
                attack.template = temp.groups()[0]
        elif (line.find ('Attacker connected') != -1 and inAttack == False):
            ip = ip_re.search(line)
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
            command = command_re.search(line)
            if command != None:
                attack.noninteractiveCommand = command.group(1)
                attack.isCat = attack.noninteractiveCommand.find("/proc/cpuinfo") != -1
        elif (line.find("SHELL") != -1):
            inAttack = False
            attack.success = False
        if inAttack:
            attack.data += line + '\n'
    return attacks

# Returns an array of Attack Objects
def getAllAttacks(directory):
    attacks101 = getAttacks(directory+'/log101.txt')
    attacks102 = getAttacks(directory+'/log102.txt')
    attacks103 = getAttacks(directory+'/log103.txt')
    attacks104 = getAttacks(directory+'/log104.txt')
    return attacks101 + attacks102 + attacks103 + attacks104

#Use this method to collect data about attacks separated by template
def attacksByTemplate():
    attacks = getAllAttacks('./logs-11-10')
    for attack in attacks:
        if attack.template == "201":
            # call method that collects data about attack, print is placeholder
            print(attack.ip)
        elif attack.template == "202":
            # call method that collects data about attack, print is placeholder
            print(attack.ip)


def printData(attacks):
    for attack in attacks:
        print(attack.data)


if __name__ == "__main__":
    attacksTest = getAllAttacks('./directory')
    printData(attacksTest)
