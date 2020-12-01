import parser


out = open("durations.txt", "a")

attacks = parser.getAllAttacks(".")

for Attack in attacks:
	
	Lines = Attack.data.splitlines()
	start_time, end_time
	
	for line in Lines:
		
		if "Attacker connected" in line:
			start_time = line.split()[1]
			
		if "Attacker closed the connection" in end_line:
					end_time = end_line.split()[1]
				
	out.write(end_time - start_time)
	
	
out.close()

#files = [file1, file2, file3, file4]
#
#for file in files:
#
#	Lines = file.readlines()
#
#	for i in range(len(Lines)):
#		
#		line = Lines[i]
#		if "Attacker connected" in line:
#			start_time = line.split()[1]
#
#			for j in range(len(Lines) - i):
#				end_line = Lines[j + i]
#				if "Attacker closed the connection" in end_line:
#					end_time = end_line.split()[1]
#					out.write(end_time - start_time)
#					break
#
#
#	file.close()
#
#out.close()		
