import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_manufacture.txt"):
    os.remove("./testfile_drug_manufacture.txt")
if os.path.exists("../processed/drug_manufacture.txt"):
    os.remove("../processed/drug_manufacture.txt")

with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_manufacture.txt", "w")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll(text=lambda t: "Manufacturer:" in t):
        file.write(div.find_next("a").text)

with open("testfile_drug_manufacture.txt", "r") as name:
    file = open("../processed/drug_manufacture.txt", "a")
    for line in name:
        file.write(line.strip() + "\n")
