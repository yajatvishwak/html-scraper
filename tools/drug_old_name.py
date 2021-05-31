from bs4 import BeautifulSoup
import os
if os.path.exists("./testfile_drug_old_name.txt"):
    os.remove("./testfile_drug_old_name.txt")
if os.path.exists("../processed/drug_old_name.txt"):
    os.remove("../processed/drug_old_name.txt")


file = open("../htmlFile/index.html", "r")
data = file.readlines()
data2 = []
for lineno, line in enumerate(data, 0):
    if "Ingredients" in line:
        if "Datum:" not in data[lineno-5]:
            data2.append("Datum: "+"\n")
            continue
        else:
            data2.append(data[lineno-5].strip() + "\n")
            continue


with open("../processed/drug_old_name.txt", "a") as file1:
    for listitem in data2:
        file1.write(listitem.strip().replace(
            "<br>", "").replace(" ", "") + "\n")
# need to process

# with open("testfile_drug_old_name.txt", "r") as name:
#     file = open("../processed/drug_old_name.txt", "a")
#     for line in name:
#         if line.strip().isalnum:
#             file.write(line.strip() + "\n")
