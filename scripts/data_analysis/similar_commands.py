import parser
import re
import pprint

reg = re.compile(r'\n|\|\||;')
pp = pprint.PrettyPrinter()

results = {}

attacks = parser.getAllAttacks(".")
for attack in attacks:
    commands = reg.split(attack.noninteractiveCommand)
    while ("" in commands):
        commands.remove("")

    for command in commands:
        if command in results:
            results[command] += 1
        else:
            results[command] = 1

pp.pprint(results)
