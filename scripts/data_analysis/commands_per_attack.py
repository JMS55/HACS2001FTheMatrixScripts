import parser
import re

reg = re.compile(r'\n|\|\||;')

def calc(with_cat):
    results_control = {}
    results_experimental = {}

    attacks = parser.getAllAttacks(".", with_cat)
    for attack in attacks:
        commands = reg.split(attack.noninteractiveCommand)
        while ("" in commands):
            commands.remove("")
        commands = len(commands)

        if attack.template == "201":
            if commands in results_control:
                results_control[commands] += 1
            else:
                results_control[commands] = 1
        else:
            if commands in results_experimental:
                results_experimental[commands] += 1
            else:
                results_experimental[commands] = 1

    print("With Cat?: " + str(with_cat))
    print("Control Results:")
    print(results_control)
    print("")
    print("Experimental Results:")
    print(results_experimental)
    print("")

calc(True)
print("")
calc(False)
