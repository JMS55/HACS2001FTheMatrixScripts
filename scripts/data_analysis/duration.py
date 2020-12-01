# this doesnt fully work yet....
import parser

#file1 = open("log101.txt", "r")
#file2 = open("log102.txt", "r")
#file3 = open("log103.txt", "r")
#file4 = open("log104.txt", "r")
out = open("durations.txt", "a")

files = [file1, file2, file3, file4]

for file in files:

	Lines = file.readlines()

	for i in range(len(Lines)):
		
		line = Lines[i]
		if "Attacker connected" in line:
			start_time = line.split()[1]

			for j in range(len(Lines) - i):
				end_line = Lines[j + i]
				if "Attacker closed the connection" in end_line:
					end_time = end_line.split()[1]
					out.write(end_time - start_time)
					break


	file.close()

out.close()		
