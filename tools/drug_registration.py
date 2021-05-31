import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_registration.html"):
    os.remove("./testfile_drug_registration.html")
if os.path.exists("../processed/drug_registration.txt"):
    os.remove("../processed/drug_registration.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_registration.html", "a")
    for line in html:
        if "Registration" in line:
            newline = line.replace("<br>", "")
            file.write('<div class="applieddate">' +
                       newline.strip() + "</div>\n")


with open("testfile_drug_registration.html", "r") as html:
    file = open("../processed/drug_registration.txt", "a")
    for line in html:
        soup = BeautifulSoup(line, "html.parser")
        for div in soup.findAll("div", attrs={"class": "applieddate"}):
            if div.text.split("Registration number:")[1].split()[0] == "Withdrawal":
                file.write("  \n")
            else:
                file.write(div.text.split("Registration number:")
                           [1].split()[0] + "\n")
