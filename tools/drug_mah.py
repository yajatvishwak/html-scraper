import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_mah.txt"):
    os.remove("./testfile_drug_mah.txt")
if os.path.exists("../processed/drug_mah.txt"):
    os.remove("../processed/drug_mah.txt")

with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_mah.txt", "w")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.findAll(text=lambda t: "MAH:" in t):
        file.write(div.find_next("a").text)

with open("testfile_drug_mah.txt", "r") as name:
    file = open("../processed/drug_mah.txt", "a")
    for line in name:
        file.write(line.strip() + "\n")
