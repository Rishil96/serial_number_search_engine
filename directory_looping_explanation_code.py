import os

count = 1

for folder, sub_folders, files in os.walk("My_Big_Directory"):
    print(f"LOOP {count} START")
    print("*******************")
    print(folder)
    print("*******************\n")
    print(sub_folders)
    print("*******************\n")
    print(files)
    print("*******************\n")
    print(f"LOOP {count} END")
    count += 1