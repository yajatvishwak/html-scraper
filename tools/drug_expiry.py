import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_expiry.html"):
    os.remove("./testfile_drug_expiry.html")
if os.path.exists("../processed/drug_expiry.txt"):
    os.remove("../processed/drug_expiry.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_expiry.html", "a")
    for line in html:
        if "Applied date:" in line:
            newline = line.replace("<br>", "")
            file.write('<div class="applieddate">' +
                       newline.strip() + "</div>\n")


with open("testfile_drug_expiry.html", "r") as html:
    file = open("../processed/drug_expiry.txt", "a")
    for line in html:
        soup = BeautifulSoup(line, "html.parser")
        for div in soup.findAll("div", attrs={"class": "applieddate"}):
            if not "Expiry" in div.text:
                file.write("  \n")
            else:
                file.write(div.text.split("Expiry date:")
                           [1].split()[0] + "\n")
