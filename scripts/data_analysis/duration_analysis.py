snoopy = open("durations_snoopy.txt", "r")
control = open("durations_control.txt", "r")

snoopy_sum = 0
snoopy_count = 0
snoopy_outlier = 0
control_sum = 0
control_count = 0
control_outlier = 0


for line in snoopy:
    time = int(line.rstrip())
    if time > 10000:
        snoopy_outlier += 1
    else:
        snoopy_sum += time
        snoopy_count += 1


for line in control:
    time = int(line.rstrip())
    if time > 10000:
        control_outlier += 1
    else:
        control_sum += time
        control_count += 1

snoopy.close()
control.close()



print("Snoopy number of outliers: ")
print(snoopy_outlier)
print("\n")
print("Snoopy count: ")
print(snoopy_count)
print("\n")
print("Snoopy sum: ")
print(snoopy_sum)
print("\n")


print("Control number of outliers: ")
print(control_outlier)
print("\n")
print("Control count: ")
print(control_count)
print("\n")
print("Control sum: ")
print(control_sum)
print("\n")
