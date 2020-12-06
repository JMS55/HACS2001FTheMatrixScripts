import parser
import re
import pprint

reg = re.compile(r'\n|\|\||;')
pp = pprint.PrettyPrinter()

results_control = {}
results_experimental = {}

attacks = parser.getAllAttacks(".", True)
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

results_control = sorted(results_control.items(), key=lambda x: x[1], reverse=True)
results_experimental = sorted(results_experimental.items(), key=lambda x: x[1], reverse=True)

pp.pprint("Control Results:")
pp.pprint(results_control)
print("")
pp.pprint("Experimental Results:")
pp.pprint(results_experimental)
