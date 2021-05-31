import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_atc_code.html"):
    os.remove("./testfile_drug_atc_code.html")
if os.path.exists("../processed/drug_atc_code.txt"):
    os.remove("../processed/drug_atc_code.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_atc_code.html", "a")
    for line in html:
        if "Applied date:" in line:
            newline = line.replace("<br>", "")
            file.write('<div class="applieddate">' +
                       newline.strip() + "</div>\n")


with open("testfile_drug_atc_code.html", "r") as html:
    file = open("../processed/drug_atc_code.txt", "a")
    for line in html:
        soup = BeautifulSoup(line, "html.parser")
        for div in soup.findAll("div", attrs={"class": "applieddate"}):
            if not "ATC-code:" in div.text:
                file.write("  \n")
            else:
                file.write(div.text.split("ATC-code:")
                           [1].split()[0] + " " + div.text.split("ATC-code:")
                           [1].split()[1] + " " + div.text.split("ATC-code:")
                           [1].split()[2] + "\n")
