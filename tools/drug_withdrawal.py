import os
from bs4 import BeautifulSoup
if os.path.exists("./testfile_drug_withdrawal.html"):
    os.remove("./testfile_drug_withdrawal.html")
if os.path.exists("../processed/drug_withdrawal.txt"):
    os.remove("../processed/drug_withdrawal.txt")


with open("../htmlFile/index.html", "r") as html:
    file = open("testfile_drug_withdrawal.html", "a")
    for line in html:
        if "Applied date:" in line:
            newline = line.replace("<br>", "")
            file.write('<div class="applieddate">' +
                       newline.strip() + "</div>\n")


with open("testfile_drug_withdrawal.html", "r") as html:
    file = open("../processed/drug_withdrawal.txt", "a")
    for line in html:
        soup = BeautifulSoup(line, "html.parser")
        for div in soup.findAll("div", attrs={"class": "applieddate"}):
            if not "Withdrawal" in div.text:
                file.write("  \n")
            else:
                file.write(div.text.split("Withdrawal date:")
                           [1].split()[0] + "\n")
