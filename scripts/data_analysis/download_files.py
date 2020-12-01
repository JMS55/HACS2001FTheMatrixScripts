import parser

total_attacks = 0
download_file_attacks = 0

attacks = parser.getAllAttacks(".")
for attack in attacks:
    total_attacks += 1
    if "curl" in attack.noninteractiveCommand or "wget" in attack.noninteractiveCommand:
        download_file_attacks += 1

print("Total: " + str(total_attacks))
print("Download files: " + str(download_file_attacks))
