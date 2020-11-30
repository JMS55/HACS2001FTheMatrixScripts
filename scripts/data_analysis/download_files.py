file1 = open("log101.txt", "r")
file2 = open("log102.txt", "r")
file3 = open("log103.txt", "r")
file4 = open("log104.txt", "r")
files = [file1, file2, file3]

total_attacks = 0
download_file_attacks = 0

for file in files:
    lines = file.readlines()
    # Find starting line of attack
    for start in range(len(lines)):
        if "Attacker authenticated and is inside container" in lines[start]:
            # Find ending line of attack
            for end in range(start + 1, len(lines)):
                if "Container's OpenSSH server closed connection" in lines[end]:
                    total_attacks += 1

                    # Check if each attack uses wget or curl
                    for i in range(start, end + 1):
                        if "wget" in lines[i] or "curl" in lines[i]:
                            download_file_attacks += 1
                            break

                    start = end + 1
                    break
    file.close()

print("Total: " + str(total_attacks))
print("Download files: " + str(download_file_attacks))
