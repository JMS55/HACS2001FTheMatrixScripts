import parser

total_attacks_control = 0
download_file_attacks_control = 0
total_attacks_experimental = 0
download_file_attacks_experimental = 0

attacks = parser.getAllAttacks(".")
for attack in attacks:
    if attack.template == "201":
        total_attacks_control += 1
        if "curl" in attack.noninteractiveCommand or "wget" in attack.noninteractiveCommand:
            download_file_attacks_control += 1
    else:
        total_attacks_experimental += 1
        if "curl" in attack.noninteractiveCommand or "wget" in attack.noninteractiveCommand:
            download_file_attacks_experimental += 1

print("Total (Control): " + str(total_attacks_control))
print("Download files (Control): " + str(download_file_attacks_control))
print("")
print("Total (Experimental): " + str(total_attacks_experimental))
print("Download files (Experimental): " + str(download_file_attacks_experimental))
