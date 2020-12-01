import parser
import re

reg = re.compile(r'\n|\|\||;')

results = {}

attacks = parser.getAllAttacks(".")
for attack in attacks:
    commands = reg.split(attack.noninteractiveCommand)
    while ("" in commands):
        commands.remove("")
    commands = len(commands)

    if commands in results:
        results[commands] += 1
    else:
        results[commands] = 1

print(results)
