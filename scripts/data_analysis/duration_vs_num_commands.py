from datetime import datetime
import parser
import re

out = open("duration_vs_number_commands.txt", "w")

reg = re.compile(r'\n|\|\||;')
date_format = "%Y-%m-%d %H:%M:%S"


attacks = parser.getAllAttacks(".")
for attack in attacks:
    commands = reg.split(attack.noninteractiveCommand)
    while ("" in commands):
        commands.remove("")
    commands = len(commands)

    Lines = attack.data.splitlines()
    start_time = ""
    end_time = ""

    for line in Lines:

        if "Attacker connected" in line:
            start_time = line.split()[0] + " " + (line.split()[1]).split(".")[0]

        if "Attacker closed connection" in line:
            end_time = line.split()[0] + " " + (line.split()[1]).split(".")[0]

    if start_time != "" and end_time != "":
        end = datetime.strptime(end_time, date_format)
        start = datetime.strptime(start_time, date_format)

    out.write(str((end - start).seconds) + "," + str(commands) + "\n")


out.close()
