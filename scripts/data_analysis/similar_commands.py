import parser
import re
import pprint

reg = re.compile(r'\n|\|\||;')
pp = pprint.PrettyPrinter()

def calc(with_cat):
    results_control = {}
    results_experimental = {}

    attacks = parser.getAllAttacks(".", with_cat)
    for attack in attacks:
        commands = reg.split(attack.noninteractiveCommand)
        while ("" in commands):
            commands.remove("")

        for command in commands:
            if attack.template == "201":
                if command in results_control:
                    results_control[command] += 1
                else:
                    results_control[command] = 1
            else:
                if command in results_experimental:
                    results_experimental[command] += 1
                else:
                    results_experimental[command] = 1

    print("With Cat?: " + str(with_cat))
    pp.pprint("Control Results:")
    pp.pprint(results_control)
    print("")
    pp.pprint("Experimental Results:")
    pp.pprint(results_experimental)
    print("")

calc(True)
print("")
calc(False)
