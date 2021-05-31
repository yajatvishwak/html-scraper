import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_applied_date.html"):
    os.remove("./testfile_drug_applied_date.html")
if os.path.exists("../processed/drug_applied_date.txt"):
    os.remove("../processed/drug_applied_date.txt")

string_arr = []


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_applied_date.html", "a")
    for line in html:
        if "Applied date" in line:
            file.write('<div class="applieddate">' + line + "</div>\n")


with open("testfile_drug_applied_date.html", "r") as html:
    soup = BeautifulSoup(html, 'html.parser')
    file = open("../processed/drug_applied_date.txt", "a")
    for div in soup.find_all("div",
                             attrs={
                                 "class": "applieddate"}
                             ):
        file.write(div.text.split(":")[1].split()[0] + "\n")
