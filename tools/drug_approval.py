import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_approval.html"):
    os.remove("./testfile_drug_approval.html")
if os.path.exists("../processed/drug_approval.txt"):
    os.remove("../processed/drug_approval.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_approval.html", "a")
    for line in html:
        if "Applied date:" in line:
            newline = line.replace("<br>", "")
            file.write('<div class="applieddate">' +
                       newline.strip() + "</div>\n")


with open("testfile_drug_approval.html", "r") as html:
    file = open("../processed/drug_approval.txt", "a")
    for line in html:
        soup = BeautifulSoup(line, "html.parser")
        for div in soup.findAll("div", attrs={"class": "applieddate"}):
            if not "Approval" in div.text:
                file.write("  \n")
            else:
                file.write(div.text.split("Approval date:")
                           [1].split()[0] + "\n")
