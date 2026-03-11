import re
from collections import defaultdict

log_file = "sample_log.txt"

ip_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1

print("\n=== Security Log Analysis Report ===\n")

for ip, attempts in ip_attempts.items():
    print(f"IP Address: {ip}")
    print(f"Failed Attempts: {attempts}")

    if attempts >= 5:
        print("⚠ Possible Brute Force Attack Detected")

    print("-------------------------")