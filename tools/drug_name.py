import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_name.html"):
    os.remove("./testfile_drug_name.html")
if os.path.exists("../processed/drug_name.txt"):
    os.remove("../processed/drug_name.txt")

with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_name.txt", "a")
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.find_all("h2",
                             # attrs={
                             #   'cellspacing': '0',
                             #   'cellpadding': '0',
                             #   'width': '798',
                             #  "border": "0"}
                             ):
        file.write(div.text + "\n")


with open("testfile_drug_name.txt", "r") as name:
    file = open("../processed/drug_name.txt", "a")
    for line in name:
        if ":" in line and "-" in line:
            file.write(line)
