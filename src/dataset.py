import pandas as pd

# List of CSV files
csv_files = [
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Friday-WorkingHours-Morning.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Monday-WorkingHours.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Tuesday-WorkingHours.pcap_ISCX.csv",
    "CIC-IDS- 2017-20250117T181829Z-001/CIC-IDS- 2017/Wednesday-workingHours.pcap_ISCX.csv"
]


# Read each CSV file and store in individual variables
df_friday_afternoon_ddos = pd.read_csv(csv_files[0])
df_friday_afternoon_portscan = pd.read_csv(csv_files[1])
df_friday_morning = pd.read_csv(csv_files[2])
df_monday = pd.read_csv(csv_files[3])
df_thursday_afternoon_infiltration = pd.read_csv(csv_files[4])
df_thursday_morning_webattacks = pd.read_csv(csv_files[5])
df_tuesday = pd.read_csv(csv_files[6])
df_wednesday = pd.read_csv(csv_files[7])

print(df_friday_afternoon_ddos.columns.tolist())