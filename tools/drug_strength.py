from bs4 import BeautifulSoup
import os
if os.path.exists("./testfile_drug_strength.txt"):
    os.remove("./testfile_drug_strength.txt")
if os.path.exists("../processed/drug_strength.txt"):
    os.remove("../processed/drug_strength.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_strength.txt", "a")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll(text=lambda t: "Strength:" in t):
        file.write(div)

with open("testfile_drug_strength.txt", "r") as name:
    file = open("../processed/drug_strength.txt", "a")
    for line in name:
        if line.strip().isalnum:
            file.write(line.strip() + "\n")
