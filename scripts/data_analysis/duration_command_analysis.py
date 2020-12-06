with open("duration_vs_number_commands.txt", "r") as input:
    Lines = input.readlines()

with open("duration_vs_number_commands.txt", "w") as out:

    for line in Lines:
        if (int(line.strip().split(",")[0]) <= 10000):
            out.write(line)


out.close()
