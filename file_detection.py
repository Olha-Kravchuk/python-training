import csv
import json
import os
from os import write

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")
else:
    print("The location doesn˜t exist")


#writing
txt_data = "I like tee"

file_path1 = "output.txt"

# try:
#     #with open(file_path1, "w") as file:
#     with open(file_path1, "x") as file:
#         file.write(txt_data)
#         print(f"txt file {file_path1} was created")
# except FileExistsError:
#     print("That file already exists!")

# try:
#     with open(file_path1, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file {file_path1} was created")
# except FileExistsError:
#     print("That file already exists!")

colegs = ["Eugene", "Bob", "Tom"]

try:
    with open(file_path1, "w") as file:
        for coleg in colegs:
            file.write(coleg + " ")
        print(f"txt file {file_path1} was created")
except FileExistsError:
    print("That file already exists!")

employee = {
    "name": "Lina",
    "age": 25,
    "job": "cook"
}
file_path2 = "output.json"
try:
    with open(file_path2, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file {file_path2} was created")
except FileExistsError:
    print("That file already exists!")

cooks = [
    ["Name", "Age"],
    ["Lika", 21],
    ["Pit", 42],
    ["Nico", 35]
]

file_path3 = "output.csv"
try:
    with open(file_path3, "w") as file:
        writer = csv.writer(file)
        for row in cooks:
            writer.writerow(row)
        print(f"csv file {file_path3} was created")
except FileExistsError:
    print("That file already exists!")

with open(file_path3, "r") as file:
    content = file.read()
    print(content)