import gspread, subprocess
from oauth2client.service_account import ServiceAccountCredentials

def to_KB(val, unit):
  if unit == "KB":
    return val
  elif unit == "MB":
    return val * 1000
  elif unit == "GB":
    return val * 1000 * 1000

def get_host_info():
    date = subprocess.run(["date"], stdout=subprocess.PIPE).stdout.decode().split()
    day = '{} {}'.format(date[1], date[2])
    time = date[3]
    
    free = subprocess.run(["free", "--mega"], stdout=subprocess.PIPE).stdout.decode()
    host_RAM = free.splitlines()[1].split()[3]
    
    df = subprocess.run(["df", "-BM", "/"], stdout=subprocess.PIPE).stdout.decode()
    host_disk = df.splitlines()[1].split()[3]
    
    uptime = subprocess.run(["uptime"], stdout=subprocess.PIPE).stdout.decode()
    host_load = uptime.split(",")[4].strip()
    
    vnstat = subprocess.run(["vnstat", "-i", "enp4s1", "-ru"], stdout=subprocess.PIPE).stdout.decode()
    host_traffic = vnstat.splitlines()[4].split()
    
    host_traffic_in = to_KB(float(host_traffic[1]), host_traffic[2])
    host_traffic_out = to_KB(float(host_traffic[4]), host_traffic[5])

    return [day, time, host_RAM, host_disk, host_load, host_traffic_in, host_traffic_out]

def get_container_info(container):
    free = subprocess.run(["pct", "exec", container, "--", "free", "-m"], stdout=subprocess.PIPE).stdout.decode()
    cont_RAM = free.splitlines()[1].split()[3]
        
    df = subprocess.run(["pct", "exec", container, "--", "df", "--block-size=1m"], stdout=subprocess.PIPE).stdout.decode()
    cont_disk = df.splitlines()[1].split()[3]
        
    uptime = subprocess.run(["pct", "exec", container, "uptime"], stdout=subprocess.PIPE).stdout.decode()
    cont_load = uptime.split(",")[4].strip()
        
    # vnstat = subprocess.run(["pct", "exec", container, "--", "vnstat", "-i", "enp4s1", "-ru"], stdout=subprocess.PIPE).stdout.decode()
    # cont_traffic = vnstat.splitlines()[4].split()
        
    # cont_traffic_in = to_KB(float(cont_traffic[1]), cont_traffic[2])
    # cont_traffic_out = to_KB(float(cont_traffic[4]), cont_traffic[5])
    
    return [cont_RAM, cont_disk, cont_load, "", ""]

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('../configs/health_log_creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Health Logs").get_worksheet(0)

row = get_host_info() + get_container_info("101") + get_container_info("101") + get_container_info("103")
index = sheet.row_count
sheet.insert_row(row, index)
