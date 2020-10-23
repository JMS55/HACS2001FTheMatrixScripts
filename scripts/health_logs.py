import subprocess

date = subprocess.run(["date"], capture_output=True, text=True).stdout.split()
day = '{} {}'.format(date[1], date[2])
time = date[3]

free = subprocess.run(["free", "--mega"], capture_output=True, text=True).stdout
host_RAM = free.splitlines()[1].split()[3]

df = subprocess.run(["df", "-BM", "/"], capture_output=True, text=True).stdout
host_disk = df.splitlines()[1].split()[3]

uptime = subprocess.run(["uptime"], capture_output=True, text=True).stdout
host_load = uptime.split(",")[4].strip()

vnstat = subprocess.run(["vnstat", "-i", "enp4s1"], capture_output=True, text=True).stdout
host_traffic = vnstat.splitlines()


print(host_traffic)
