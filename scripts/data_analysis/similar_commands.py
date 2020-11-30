import re

file1 = open("log101.txt", "r")
file2 = open("log102.txt", "r")
file3 = open("log103.txt", "r")
file4 = open("log104.txt", "r")
files = [file1, file2, file3]

for file in files:
    lines = file.readlines()
    # Find starting line of attack
    for start in range(len(lines)):
        if "Attacker authenticated and is inside container" in lines[start]:
            # Find ending line of attack
            for end in range(start + 1, len(lines)):
                if "Container's OpenSSH server closed connection" in lines[end]:
                    # TODO: Group commands by similarity
                    for i in range(start, end + 1):
                        if "line from reader" in lines[i] or "Noninteractive mode attacker command" in lines[i]:
                            command = re.split("(line from reader:)|(Noninteractive mode attacker command:) ", lines[i])
                            command = command[3].strip()
                            print(command)

                    start = end + 1
                    break
    file.close()
