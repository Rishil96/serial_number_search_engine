# Serial Number Search Engine
import os
import re
from pathlib import Path
import time


serial_numbers = []
serial_pattern = r"N[a-z]{3}-\d{5}"

start_time = time.perf_counter()

for folder, sub_folders, files in os.walk("My_Big_Directory"):

    for file in files:
        file_path = Path(folder, file)
        with open(file_path, "r") as text:
            text = text.read()
            serial_match = re.search(serial_pattern, text)
            if serial_match:
                serial_numbers.append((file, serial_match.group()))

end_time = time.perf_counter()

execution_time = end_time - start_time

print("----------------------------------------------")
print("FILE\t\t\tSERIAL NO.")
print("----\t\t\t----------")
for serial_num in serial_numbers:
    print(f"{serial_num[0]}\t\t{serial_num[1]}")
print("----------------------------------------------")
print(f"\nNumbers found : {len(serial_numbers)}")
print(f"Search duration: {round(execution_time, 1)} seconds.")
