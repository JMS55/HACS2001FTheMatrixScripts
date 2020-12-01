import parser


out = open("durations.txt", "a")

attacks = parser.getAllAttacks(".")

date_format = "%Y-%m-%d %H:%M:%S"

for Attack in attacks:
	
	Lines = Attack.data.splitlines()
	start_time = ""
	end_time = ""
	
	for line in Lines:
		
		if "Attacker connected" in line:
			start_time = line.split()[0] + " " + (line.split()[1]).split(".")[0]
			
		if "Attacker closed connection" in line:
			end_time = line.split()[0] + " " + (line.split()[1]).split(".")[0]
				
	if start_time != "" && end_time != "":
		end = datetime.strptime(end_time, date_format)
		start = datetime.strptime(start_time, date_format)
		out.write((end - start).seconds)
	
	
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
