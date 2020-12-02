from datetime import datetime
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
				
	if start_time != "" and end_time != "":
		end = datetime.strptime(end_time, date_format)
		start = datetime.strptime(start_time, date_format)
		out.write(str((end - start).seconds) + "\n")
	
	
out.close()
