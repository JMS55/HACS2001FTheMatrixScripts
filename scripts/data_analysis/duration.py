from datetime import datetime
import parser


out1 = open("durations_control.txt", "a")
out2 = open("durations_snoopy.txt", "a")

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
		if Attack.template == 201:
			out1.write(str((end - start).seconds) + "\n")
		else:
			out2.write(str((end - start).seconds) + "\n")
	
	
out1.close()
out2.close()
